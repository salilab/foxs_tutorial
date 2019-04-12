#!/usr/bin/env python

from __future__ import print_function
import unittest
import sys
import os
import re
import subprocess
import util
import shutil

TOPDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',
                                      '..', 'multi_foxs', 'rpa'))

DOCDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',
                                      '..', 'doc'))


class Tests(unittest.TestCase):
    def test_rpa(self):
        """Test the MultiFoXS RPA example"""
        with util.temporary_directory() as td:
            testdir = os.path.join(td, 'rpa')
            shutil.copytree(TOPDIR, testdir)
            cmds = list(util.get_shell_commands(os.path.join(DOCDIR,
                                                             'multifoxs.md')))
            for c in cmds:
                print(c)
                subprocess.check_call(c, shell=True, cwd=testdir)
            expected = ['cluster_representatives.txt',
                        'multi_state_model_1_1_1.dat',
                        'multi_state_model_1_2_1.dat',
                        'multi_state_model_1_3_1.dat',
                        'ensembles_size_1.txt',
                        'multi_state_model_2_1_1.dat',
                        'multi_state_model_2_2_1.dat',
                        'ensembles_size_2.txt',
                        'multi_state_model_3_1_1.dat',
                        'ensembles_size_3.txt']
            for e in expected:
                os.unlink(os.path.join(testdir, e))


if __name__ == '__main__':
    unittest.main()
