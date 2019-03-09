#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  ezbuildbot_config.py
#  Configuration classes for the ezbuildbot configuration.

from typing import Any, Dict, List, NamedTuple, Tuple
import os
import json
import yaml


class Builder(NamedTuple):
    name: str
    git_url: str
    # List of (name, command)
    # The command is run from the root of the repo
    steps: List[Tuple[str, str]]

    @staticmethod
    def from_dict(in_dict: Dict[str, Any]) -> "Builder":
        steps_in = list(in_dict['steps'])
        steps = []  # type: List[Tuple[str, str]]
        for s in steps_in:
            assert isinstance(s, list)
            assert len(s) == 2
            steps.append((str(s[0]), str(s[1])))
        return Builder(
            name=str(in_dict['name']),
            git_url=str(in_dict['git_url']),
            steps=steps
        )


class BuildbotConfig:
    """
    Represents a buildbot config.
    """

    def __init__(self, contents: str, is_yaml: bool = True) -> None:
        """
        Create a buildbot config from the given string.
        """
        if is_yaml:
            raw = yaml.safe_load(contents)
        else:
            raw = json.loads(contents)

        self._builders = list(map(Builder.from_dict, raw['builders']))

    @property
    def builders(self) -> List[Builder]:
        return self._builders

    @staticmethod
    def from_filename(filename: str) -> "BuildbotConfig":
        with open(filename, 'r') as f:
            contents = str(f.read())

        is_yaml = os.path.splitext(filename)[1] in {".yml", ".yaml"}

        return BuildbotConfig(contents, is_yaml=is_yaml)
