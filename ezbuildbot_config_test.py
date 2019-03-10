#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  ezbuildbot_config.py
#  Tests for ezbuildbot_config.

from typing import Dict, Tuple, List, Optional, Union

from ezbuildbot_config import *

import unittest


class BuildbotConfigTest(unittest.TestCase):
    with open("test.yml", 'r') as f:
        sample_config_str = str(f.read())

    def test_parse_yaml(self) -> None:
        """
        Test that parsing a config in YAML works.
        """
        config = BuildbotConfig(self.sample_config_str, is_yaml=True)

    def test_get_builders(self) -> None:
        """
        Test that builders are parsed correctly.
        """
        config = BuildbotConfig(self.sample_config_str, is_yaml=True)
        self.assertEqual(len(config.builders), 2)
        self.assertEqual(config.builders[0].name, "myrepo-build")
        self.assertEqual(
            config.builders[0].git_url, "git@github.com:myorg/myrepo.git")
        self.assertEqual(config.builders[0].steps, [
                         ("test1", "./test1.sh"),
                         ("test2", "./test2.sh")
        ])

    def test_workers(self) -> None:
        """
        Test that workers are parsed correctly.
        """
        config = BuildbotConfig(self.sample_config_str, is_yaml=True)
        self.assertEqual(len(config.workers), 1)
        self.assertEqual(config.workers[0].name, "testworker")
        self.assertEqual(config.workers[0].password, "testpassword")

    def test_github_webhook_secret(self) -> None:
        """
        Test that github_webhook_secret is parsed correctly.
        """
        config = BuildbotConfig(self.sample_config_str, is_yaml=True)
        self.assertEqual(config.github_webhook_secret, "my_webhook_secret")

    def test_github_incoming_webhooks(self) -> None:
        """
        Test that GitHub incoming webhooks are parsed correctly.
        """
        config = BuildbotConfig(self.sample_config_str, is_yaml=True)
        self.assertEqual(len(config.github_incoming_webhooks), 1)
        self.assertEqual(config.github_incoming_webhooks[0].name, "incoming-webhook")
        self.assertEqual(config.github_incoming_webhooks[0].description, "PR webhooks from GitHub")
        self.assertEqual(config.github_incoming_webhooks[0].builders, ["myrepo-build"])
        self.assertEqual(config.github_incoming_webhooks[0].filter_project, "myorg/myrepo")

    def test_github_status_pushes(self) -> None:
        """
        Test that GitHub status pushes are parsed correctly.
        """
        config = BuildbotConfig(self.sample_config_str, is_yaml=True)
        self.assertEqual(len(config.github_status_pushes), 1)
        self.assertEqual(config.github_status_pushes[0].token, "MY_SECRET_TOKEN")
        self.assertEqual(config.github_status_pushes[0].context, "buildbot")
        self.assertEqual(config.github_status_pushes[0].builders, ["myrepo-build"])

    def test_github_comment_pushes(self) -> None:
        """
        Test that GitHub comment pushes are parsed correctly.
        """
        config = BuildbotConfig(self.sample_config_str, is_yaml=True)
        self.assertEqual(len(config.github_comment_pushes), 1)
        self.assertEqual(config.github_comment_pushes[0].token, "MY_SECRET_TOKEN")
        self.assertEqual(config.github_comment_pushes[0].context, "buildbot")
        self.assertEqual(config.github_comment_pushes[0].builders, ["myrepo-build"])

if __name__ == '__main__':
    unittest.main()
