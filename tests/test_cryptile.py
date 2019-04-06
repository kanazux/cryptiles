#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""Tests for spl_pd_message"""


from unittest import TestCase, main, mock
from cryptiles.cryptile import crypt_data


class testCryptile(TestCase):
    """Test Class crypt_data."""

    _crypt = crypt_data('teste')

    def test_encrypt(self):
        self.assertIsInstance(self._crypt.encrypt('teste').decode(), str)

    def test_decrypt(self):
        mock_decrypt = mock.create_autospec(self._crypt.decrypt,
                                            return_value="Mock Test")
        self.assertEqual(mock_decrypt(self._crypt.encrypt('teste').decode()), "Mock Test")


if __name__ == "__main__":
    main()