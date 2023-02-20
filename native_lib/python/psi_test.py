#!/usr/bin/env python3
'''Test APIs'''

import sys
import unittest

import native_lib.python
import native_lib.python.mypsi as pypsi
from native_lib.python.mypsi import psiRun, psiRun1

if __debug__:
    print(f'python path: {sys.path}')

    print(f'foo.python: ${dir(native_lib.python)}')

    print(f'foo.python.mypsi: ${dir(native_lib.python.mypsi)}')


class TestPsi(unittest.TestCase):
    '''Test Psi'''

    # def test_psiRun(self):
    #     self.assertEqual(3, psiRun(1, 2))
    
    def test_psiRun1(self):
        self.assertEqual(-1, psiRun1(1, 2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
