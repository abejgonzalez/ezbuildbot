#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  ast_utils.py
#  Utils/helpers in manipulating the Python AST.
#
#  Copyright 2019 Edward Wang <edward.c.wang@compdigitec.com>

import ast
import astor
import copy
from typing import Any, Dict, List, Optional, Set

# TODO(edwardw): write unit tests for everything in this file


class GetFunction(ast.NodeVisitor):
    def __init__(self, function: str) -> None:
        """
        Get the named function from the AST.
        """
        self.function = function
        self.result: Optional[ast.FunctionDef] = None

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        if node.name == self.function:
            self.result = node


def get_function(name: str, module: ast.Module) -> ast.FunctionDef:
    """
    Get the given function from the given module.
    """
    visitor = GetFunction(name)
    visitor.visit(module)
    if visitor.result is not None:
        return visitor.result
    else:
        raise ValueError(f"Function {name} not found")


def parse_const_from_object(obj: Any) -> ast.expr:
    """
    Parse a single Python constant into an expr.
    e.g. "15" or "[1, 2, 3]"
    """
    body = ast.parse(repr(obj)).body
    assert len(body) == 1
    assert isinstance(body[0], ast.Expr)
    return body[0].value


def parse_statement(stmt: str) -> ast.stmt:
    """
    Parse a single Python statement.
    e.g. "x = 15" or "y += [1, 2, 3]"
    """
    body = ast.parse(stmt).body
    assert len(body) == 1
    assert isinstance(body[0], ast.stmt)
    return body[0]


def sanitize_name(name: str) -> str:
    """
    Sanitize the given name so that it can be a Python identifier.
    """
    # No empty names
    if name == "":
        return "empty_"

    # No dashes
    name = name.replace('-', '_')

    # No leading digits
    if name.isdigit() or name[0].isdigit():
        return "_" + name

    return name


class SubstituteVariables(ast.NodeTransformer):
    """
    Transformation to replace a set of variable references to another.
    """

    def __init__(self, mapping: Dict[str, str]) -> None:
        self.mapping: Dict[str, str] = mapping

    def visit_Name(self, node: ast.Name) -> Any:
        # Replace id if a mapping for it exists.
        return ast.Name(id=self.mapping.get(node.id, node.id), ctx=node.ctx)


class SubstituteVariablesExpr(ast.NodeTransformer):
    """
    Transformation to replace a set of variable references with arbitrary
    expressions.
    """

    def __init__(self, mapping: Dict[str, ast.expr]) -> None:
        for v in mapping.values():
            assert isinstance(v, ast.expr)
        self.mapping: Dict[str, ast.expr] = mapping

    def visit_Name(self, node: ast.Name) -> Any:
        # If mapping exists, return it; otherwise return the same node.
        return self.mapping.get(node.id, node)


class ReplaceFunction(ast.NodeTransformer):
    """
    Transformation that replaces a set of functions with another.
    """

    def __init__(self, functions: Dict[str, ast.FunctionDef]) -> None:
        self.functions: Dict[str, ast.FunctionDef] = functions

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        return self.functions.get(node.name, node)


class RemoveFunction(ast.NodeTransformer):
    """
    Transformation that removes a set of functions.
    """

    def __init__(self, functions: Set[str]) -> None:
        self.functions: Set[str] = functions

    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        if node.name in self.functions:
            return None
        else:
            return node


def check_signature(sig: str, func: ast.FunctionDef) -> None:
    """
    Check that the signature of the function matches the one given as a
    string.
    """
    reference_def = ast.parse(sig).body[0]
    assert isinstance(reference_def, ast.FunctionDef)

    if astor.to_source(func.args) != astor.to_source(reference_def.args):
        raise ValueError(
            f"The function signature is incorrect - got {astor.to_source(func.args)} instead of {astor.to_source(reference_def.args)}")


def apply_templated_function_with_return(template: ast.FunctionDef, signature: str, arguments: Dict[str, Any], new_name: str) -> ast.FunctionDef:
    """
    Apply a templated function and return a function with a new name and
    no arguments.
    :param template: Function to use as template
    :param signature: Check that this function signature matches
    :param arguments: Arguments to substitute
    :param new_name: New function name
    :return: New function
    """
    assert isinstance(template, ast.FunctionDef)
    assert isinstance(signature, str)
    assert isinstance(new_name, str)

    check_signature(signature, template)

    # Create ast.expr for arguments
    arguments = dict(
        map(lambda kv: (kv[0], parse_const_from_object(kv[1])), arguments.items()))

    new_template = SubstituteVariablesExpr(
        arguments).visit(copy.deepcopy(template))

    new_body: List[ast.stmt] = new_template.body

    # Return a new function with no arguments
    return ast.FunctionDef(
        name=new_name,
        # No arguments
        args=ast.arguments(args=[], vararg=None, kwonlyargs=[],
                           kwarg=None, defaults=[], kw_defaults=[]),
        body=new_body,
        decorator_list=[],
        returns=None)
