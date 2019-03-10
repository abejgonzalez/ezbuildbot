#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  ezbuildbot_config.py
#  Configuration classes for the ezbuildbot configuration.

from typing import Any, Dict, List, NamedTuple, Optional, Tuple
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


class Worker(NamedTuple):
    name: str
    password: str

    @staticmethod
    def from_dict(in_dict: Dict[str, Any]) -> "Worker":
        return Worker(
            name=str(in_dict['name']),
            password=str(in_dict['password'])
        )


class GitHubIncomingWebhook(NamedTuple):
    """
    Represents a GitHub PR webhook configuration.
    """

    name: str
    description: str
    builders: List[str]
    # In the GitHub hook, the project is the github project name.
    # e.g. "ucb-bar/hammer"
    filter_project: Optional[str]

    @staticmethod
    def from_dict(in_dict: Dict[str, Any]) -> "GitHubIncomingWebhook":
        builders = list(in_dict['builders'])
        for b in builders:
            assert isinstance(b, str)
        filter_project: Optional[str] = None
        if 'filter_project' in in_dict:
            filter_project = str(in_dict['filter_project'])
        return GitHubIncomingWebhook(
            name=str(in_dict['name']),
            description=str(in_dict['description']),
            builders=builders,
            filter_project=filter_project
        )


class GitHubStatusCommentPush(NamedTuple):
    token: str
    context: str
    builders: List[str]

    @staticmethod
    def from_dict(in_dict: Dict[str, Any]) -> "GitHubStatusCommentPush":
        builders = list(in_dict['builders'])
        for b in builders:
            assert isinstance(b, str)
        return GitHubStatusCommentPush(
            token=str(in_dict['token']),
            context=str(in_dict['context']),
            builders=builders
        )

    def __hash__(self):
        # Work around the non-hashable list
        # This is used a temporary name when generating functions since
        # this class doesn't have a name.
        return hash(str(self._asdict()))


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
        self._workers = list(map(Worker.from_dict, raw['workers']))

        self.hostname: str = "localhost" if 'hostname' not in raw else str(
            raw['hostname'])
        self.github_webhook_secret: Optional[str] = None if 'github_webhook_secret' not in raw else str(
            raw['github_webhook_secret'])

        self._github_incoming_webhooks = list(
            map(GitHubIncomingWebhook.from_dict, raw['github_incoming_webhooks']))
        self._github_status_pushes = list(
            map(GitHubStatusCommentPush.from_dict, raw['github_status_pushes']))
        self._github_comment_pushes = list(
            map(GitHubStatusCommentPush.from_dict, raw['github_comment_pushes']))

    @property
    def builders(self) -> List[Builder]:
        return self._builders

    @property
    def workers(self) -> List[Worker]:
        return self._workers

    @property
    def github_incoming_webhooks(self) -> List[GitHubIncomingWebhook]:
        return self._github_incoming_webhooks

    @property
    def github_status_pushes(self) -> List[GitHubStatusCommentPush]:
        return self._github_status_pushes

    @property
    def github_comment_pushes(self) -> List[GitHubStatusCommentPush]:
        return self._github_comment_pushes

    @staticmethod
    def from_filename(filename: str) -> "BuildbotConfig":
        with open(filename, 'r') as f:
            contents = str(f.read())

        is_yaml = os.path.splitext(filename)[1] in {".yml", ".yaml"}

        return BuildbotConfig(contents, is_yaml=is_yaml)
