#!/usr/bin/env python

from __future__ import print_function
import unittest
import sys
import os
import re
import subprocess
import util
import shutil

FOXSDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',
                                       '..', 'foxs', 'nup133'))

TOPDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


class Tests(unittest.TestCase):
    def test_nup133(self):
        """Test the FoXS Nup133 example"""
        with util.temporary_directory() as td:
            topdir = os.path.join(td, 'top')
            testdir = os.path.join(topdir, 'foxs', 'nup133')
            shutil.copytree(TOPDIR, topdir)
            subprocess.check_call("./foxs.sh", shell=True, cwd=topdir)
            with open(os.path.join(testdir, '3KFO_23922_merge.dat')) as fh:
                lines = fh.readlines()
            self.assertIn('Chi^2 = 8.76', lines[1])
            with open(os.path.join(testdir,
                              '3KFO-fill.B99990005_23922_merge.dat')) as fh:
                lines = fh.readlines()
            self.assertIn('Chi^2 = 1.31', lines[1])
            expected = ['3KFO_23922_merge.dat',
                        '3KFO-fill.B99990005_23922_merge.dat', 'fit.plt',
                        'profiles.plt', 'fit.png']
            for e in expected:
                os.unlink(os.path.join(testdir, e))

    def test_nup133_modeller(self):
        """Test the Nup133 example Modeller script"""
        with util.temporary_directory() as td:
            testdir = os.path.join(td, 'nup133')
            shutil.copytree(TOPDIR, testdir)
            c = [sys.executable, 'add-missing-residues.py']
            print(" ".join(c))
            subprocess.check_call(c, shell=False, cwd=testdir)
            expected = ['3KFO-fill.ini', '3KFO-fill.rsr', '3KFO-fill.sch']
            for i in range(1,6):
                for pattern in ('3KFO-fill.D0000000%d', '3KFO-fill.V9999000%d',
                                '3KFO-fill.B9999000%d.pdb'):
                    expected.append(pattern % i)
            for e in expected:
                os.unlink(os.path.join(testdir, e))

if __name__ == '__main__':
    unittest.main()
