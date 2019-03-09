import ast

__version__: str

def to_source(m: ast.AST, indent_with: str = "    ", add_line_information: bool = False, pretty_string=None, pretty_source=None) -> str: ...
