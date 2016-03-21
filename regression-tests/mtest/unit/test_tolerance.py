#!/usr/bin/env python
"""
Unit test suite for the betr regression test manager

"""
from __future__ import print_function

import logging
import os
import sys
import unittest

if sys.version_info[0] == 2:
    from ConfigParser import SafeConfigParser as config_parser
else:
    from configparser import ConfigParser as config_parser


from rtest_betr import Tolerances


class Tolerances_suite(unittest.TestCase):
    """
    """
    _LOG_FILENAME = 'dummy.testlog'

    def setUp(self):
        """
        """
        logging.basicConfig(filename=self._LOG_FILENAME,
                            filemode='w',
                            level=logging.INFO,
                            format='%(message)s')
        logging.info('mtest {0} unit test log.'.format(__name__))

    def tearDown(self):
        """
        """
        logging.shutdown()
        if os.path.isfile(self._LOG_FILENAME):
            os.remove(self._LOG_FILENAME)

    # ------------------------------------------------------

    def test_tolerances_default(self):
        """Test basic initialization of a tolerance object and return of a
        default value.

        """
        tolerances = Tolerances()
        expected = Tolerances._DEFAULT_EPSILON
        received = tolerances.get(Tolerances.CONC, 'value')

        self.assertEqual(expected, received)


if __name__ == '__main__':
    # unittest.main(buffer=True)
    unittest.main()
