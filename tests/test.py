#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
import pytest

from langdetect import detect_langs
from langdetect import DetectorFactory

from polyglot.detect import Detector
from polyglot.utils import pretty_list


class TestLanguageDetector(unittest.TestCase):

    def setUp(self):
        print('All looks good')

    def test_polyglot_setup(self):
        input_text = "This is a sample string"
        detector = Detector(input_text)
        self.assertEqual('en', detector.language.code)

    def test_langdetect_setup(self):
        input_text = "This is a sample string"
        detected_language = str(detect_langs(input_text))
        self.assertEqual('en', detected_language[1:3])


if __name__ == '__main__':
    unittest.main()
