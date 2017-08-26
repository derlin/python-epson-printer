import unittest
from epson_printer.barcode import *

valid_tests = [
    # Barcode - UPC-A
    ("01234567890", BARCODE_UPCA),
    ("012345678901", BARCODE_UPCA),
    # Barcode - UPC-E
    ("123456", BARCODE_UPCE),
    ("0123456", BARCODE_UPCE),
    ("01234567", BARCODE_UPCE),
    ("01234567890", BARCODE_UPCE),
    ("012345678901", BARCODE_UPCE),
    # Barcode - JAN13
    ("012345678901", BARCODE_JAN13),
    ("0123456789012", BARCODE_JAN13),
    # Barcode - JAN8
    ("0123456", BARCODE_JAN8),
    ("01234567", BARCODE_JAN8),
    # Barcode - Code39
    ("1234", BARCODE_CODE39),
    ("ABC 012", BARCODE_CODE39),
    ("$%+-./", BARCODE_CODE39),
    ("*TEXT*", BARCODE_CODE39),

    # Barcode - ITF
    ("1234", BARCODE_ITF),
    # Barcode - Codabar
    ("A012345A", BARCODE_CODABAR),
    ("A012$+-./:A", BARCODE_CODABAR),
    # Barcode - Code93
    ("012abcd", BARCODE_CODE93),
    # Barcode - Code128
    ("{A" + "012ABCD", BARCODE_CODE128),
    ("{B" + "012ABCDabcd", BARCODE_CODE128),
    ("{C" + chr(21) + chr(32) + chr(43), BARCODE_CODE128)
]

invalid_tests = [
    # Barcode - UPC-A
    ("0123456789012", BARCODE_UPCA),
    ("A12345678901", BARCODE_UPCA),
    # Barcode - UPC-E
    ("012345678", BARCODE_UPCE),
    ("A12345678901", BARCODE_UPCE),
    # Barcode - JAN13
    ("01234567890", BARCODE_JAN13),
    ("A123456789012", BARCODE_JAN13),
    # Barcode - JAN8
    ("012345678", BARCODE_JAN8),
    ("A1234567", BARCODE_JAN8),
    # Barcode - Code39
    ("*TEXT", BARCODE_CODE39),
    ("12*34", BARCODE_CODE39),
    ("abcd", BARCODE_CODE39),
    ("**", BARCODE_CODE39),
    # Barcode - ITF
    ("123", BARCODE_ITF),
    ("A234", BARCODE_ITF),
    # Barcode - Codabar
    ("012345", BARCODE_CODABAR),
    ("012A45", BARCODE_CODABAR),
    # Barcode - Code93
    ("", BARCODE_CODE93),
    # Barcode - Code128
    ("ABCD", BARCODE_CODE128),
]


class TestBarcode(unittest.TestCase):
    def test_valid_barcode(self):
        for t in valid_tests:
            self.assertTrue(validate_barcode(t[0], t[1]))

    def test_invalid_barcode(self):
        for t in invalid_tests:
            self.assertFalse(validate_barcode(t[0], t[1]))

if __name__ == '__main__':
    unittest.main()
