# -*- coding: utf-8 -*-

from .context import qrcode
from .helpers import read_qr_code

import unittest
import os


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_test(self):
        assert True

    def test_simple(self):

        test_string = "https://shiftcreator.space/"
        output_file = "./tests/tmp/test_simple.png"

        # Generate the QR Code
        qr = qrcode.QRCode(
            version=7,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
            image_factory = qrcode.image.pure.PyPNGImage,
            mask_pattern=7)
        qr.add_data(test_string)

        # Save the image in the tmp folder
        img = qr.make_image()
        with open(output_file, 'wb') as my_file:
            img.save(my_file)

        # Retrive the encoded data
        encoded_data = read_qr_code(output_file) 

        # Delete the image
        os.remove(output_file)

        # check that it is correct
        assert encoded_data == test_string

if __name__ == '__main__':
    unittest.main()
