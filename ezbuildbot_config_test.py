#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  ezbuildbot_config.py
#  Tests for ezbuildbot_config.

from typing import Dict, Tuple, List, Optional, Union

from ezbuildbot_config import *

import unittest


class BuildbotConfigTest(unittest.TestCase):
    sample_config_str = """
builders:
- name: "myrepo-build"
  git_url: "git@github.com:myorg/myrepo.git"
  steps:
  - ["test1", "./test1.sh"]
  - ["test2", "./test2.sh"]
- name: "otherepo-build"
  git_url: "git@github.com:myorg/otherepo.git"
  steps:
  - ["mytest", "./test.py"]
"""

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


if __name__ == '__main__':
    unittest.main()
