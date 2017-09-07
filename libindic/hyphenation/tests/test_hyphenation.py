#! /usr/bin/python
# -*- coding: utf-8 -*-

from testtools import TestCase

from .. import Hyphenator


class HyphenationTest(TestCase):

    def setUp(self):
        super(HyphenationTest, self).setUp()
        self.hyphenator = Hyphenator()

    def test_hyphenation(self):
        self.assertEqual(self.hyphenator.hyphenate(u"ഒഴിച്ചുകൂടാനാവാത്ത", hyphen = "-"),u"ഒഴി-ച്ചു-കൂ-ടാ-നാ-വാ-ത്ത ")
