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


if __name__ == '__main__':
    unittest.main()
