import unittest
from epson_printer.epsonprinter import PrintableImage
from PIL import Image
from time import time
from os.path import join, realpath, dirname

class TestPrintableImage(unittest.TestCase):

    def test_from_image(self):
        im = Image.open(join(dirname(realpath(__file__)), '../../logo.png'))
        start = time()
        printable = PrintableImage.from_image(im)
        elapsed = time() - start
        print(elapsed)
        height = printable.height
        data = printable.data
        self.assertEqual(height, 432)
        expected = [27, 42, 33, 200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, \
                    2, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 2, 0, 0, 1, 0, 0, 2, 0, \
                    0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 2, 0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 2, \
                    0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, \
                    2, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 85, 85, 85, 34, 34, 34, \
                    27, 74, 48, 27, 42, 33, 200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 85, 0, 0, 42, 0, 159, 170, 0, \
                    96, 213, 0, 191, 126, 7, 74, 131, 1, 245, 253, 22, 42, 170, 11, 223, 85, 22, 160, 174, \
                    25, 127, 83, 22, 144, 157, 91, 224, 2, 44, 144, 1, 151, 64, 2, 105, 128, 0, 94, 192, 0, \
                    165, 0, 0, 123, 192, 0, 148, 128, 0, 111, 64, 2, 178, 160, 1, 109, 208, 2, 182, 80, 3, \
                    203, 175, 221, 118, 212, 42, 169, 59, 213, 95, 213, 110, 228, 174, 179, 59, 115, 93, \
                    205, 156, 170, 118, 103, 215, 171, 186, 121, 85, 85, 142, 186, 238, 243, 207, 51, 93, \
                    113, 204, 170, 158, 119, 87, 235, 154, 234, 84, 231, 93, 183, 56, 235, 217, 207, 20, \
                    46, 117, 239, 219, 170, 181, 101, 93, 90, 186, 227, 183, 215, 61, 73, 42, 214, 254, 221, \
                    169, 37, 106, 95, 218, 183, 228, 175, 89, 59, 113, 166, 206, 158, 253, 177, 235, 38, 222, \
                    85, 217, 107, 186, 110, 149, 79, 179, 250, 240, 92, 71, 95, 167, 186, 165, 121, 109, \
                    122, 150, 155, 149, 109, 228, 238, 182, 191, 83, 9, 82, 189, 94, 173, 202, 19, 218, 118, \
                    28, 103, 155, 7, 186, 229, 9, 77, 58, 6, 243, 205, 1, 93, 119, 0, 170, 168, 2, 173, 95, \
                    0, 51, 229, 0, 14, 90, 0, 1, 37, 0, 0, 154, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 85, 85, 85, 34, 34, 34, 27, 74, 48, 27, 42, \
                    33, 200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, \
                    0, 0, 0, 7, 0, 0, 4, 0, 0, 19, 0, 0, 29, 0, 0, 22, 0, 0, 75, 0, 0, 117, 0, 0, 26, 0, 0, \
                    237, 0, 0, 87, 0, 1, 104, 0, 0, 159, 0, 3, 106, 0, 0, 181, 0, 2, 90, 0, 1, 231, 0, 2, 57, \
                    0, 1, 206, 0, 2, 117, 0, 1, 171, 0, 2, 92, 0, 1, 231, 0, 2, 57, 0, 1, 206, 0, 2, 115, 0, \
                    1, 172, 0, 2, 119, 0, 1, 141, 0, 2, 242, 0, 1, 95, 0, 2, 169, 82, 1, 214, 173, 130, 107, \
                    162, 67, 157, 93, 128, 234, 234, 131, 55, 55, 66, 217, 217, 129, 102, 174, 66, 187, 83, \
                    129, 205, 252, 130, 114, 75, 67, 157, 182, 128, 231, 91, 67, 56, 228, 130, 207, 95, 129, \
                    117, 178, 66, 202, 205, 131, 119, 187, 0, 153, 173, 147, 238, 210, 128, 83, 125, 67, 189, \
                    139, 129, 74, 245, 2, 245, 46, 193, 91, 211, 2, 172, 189, 131, 87, 74, 64, 233, 247, 131, \
                    62, 41, 65, 197, 222, 130, 123, 101, 131, 173, 186, 64, 82, 87, 131, 191, 169, 66, 201, \
                    94, 129, 118, 229, 66, 173, 59, 131, 86, 204, 128, 185, 119, 119, 206, 169, 128, 115, 94, \
                    255, 157, 229, 18, 234, 59, 237, 85, 204, 86, 175, 119, 185, 116, 170, 215, 171, 85, 44, \
                    214, 187, 243, 59, 204, 157, 212, 119, 106, 111, 170, 215, 177, 91, 57, 94, 237, 206, 213, \
                    18, 115, 106, 255, 172, 175, 73, 87, 113, 182, 217, 158, 235, 110, 229, 28, 147, 58, 231, \
                    253, 215, 186, 74, 170, 85, 181, 93, 237, 94, 230, 54, 227, 57, 203, 61, 207, 181, 202, \
                    116, 218, 119, 171, 47, 169, 93, 241, 94, 227, 158, 229, 60, 101, 59, 215, 187, 212, 169, \
                    212, 175, 110, 47, 117, 179, 213, 138, 93, 186, 247, 170, 69, 40, 165, 181, 174, 186, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 68, 0, 1, 17, 0, 0, 68, 0, 0, 0, 0, 1, 17, \
                    0, 0, 68, 0, 1, 16, 0, 0, 5, 0, 0, 64, 0, 1, 18, 0, 0, 64, 0, 0, 10, 0, 1, 32, 0, 0, 4, \
                    0, 0, 144, 0, 0, 34, 0, 1, 0, 0, 0, 72, 0, 0, 2, 0, 0, 80, 0, 0, 5, 0, 0, 0, 0, 0, 82, \
                    0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 4, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 85, 85, 85, 34, 34, 34, 27, 74, 48, 27, 42, 33, 200, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 87, 0, 0, 8, \
                    0, 190, 247, 2, 67, 154, 9, 188, 231, 54, 103, 56, 11, 185, 207, 252, 206, 117, 167, 115, \
                    170, 89, 157, 87, 238, 106, 186, 83, 213, 213, 189, 46, 174, 74, 245, 115, 245, 171, 156, \
                    46, 92, 231, 211, 231, 57, 125, 57, 206, 138, 206, 115, 247, 115, 172, 88, 173, 87, 175, \
                    218, 234, 210, 103, 61, 189, 154, 198, 86, 237, 121, 171, 51, 174, 212, 221, 83, 63, 102, \
                    189, 210, 185, 202, 109, 206, 119, 182, 115, 152, 89, 156, 239, 174, 231, 85, 213, 58, 170, \
                    107, 213, 125, 188, 171, 167, 71, 108, 216, 249, 183, 47, 46, 89, 242, 211, 174, 157, 108, \
                    213, 102, 183, 107, 185, 76, 188, 206, 247, 71, 51, 41, 249, 221, 222, 46, 166, 99, 213, \
                    121, 189, 107, 174, 74, 156, 83, 245, 231, 189, 78, 186, 202, 179, 85, 119, 220, 219, 88, \
                    55, 109, 175, 201, 146, 213, 126, 253, 106, 165, 70, 189, 90, 187, 70, 247, 109, 249, 9, \
                    146, 47, 254, 255, 212, 165, 73, 107, 90, 182, 182, 175, 107, 75, 241, 157, 252, 30, 234, \
                    39, 229, 55, 217, 187, 217, 110, 76, 166, 153, 119, 123, 238, 169, 140, 83, 94, 247, 188, \
                    229, 74, 199, 59, 117, 121, 205, 154, 174, 178, 239, 83, 221, 81, 189, 102, 190, 211, 187, \
                    197, 108, 84, 122, 183, 175, 175, 73, 241, 81, 254, 30, 190, 73, 229, 211, 182, 186, 172, \
                    219, 87, 119, 53, 217, 141, 202, 102, 242, 125, 189, 95, 167, 82, 169, 88, 175, 86, 239, \
                    217, 237, 53, 110, 51, 202, 179, 221, 119, 92, 166, 153, 171, 123, 110, 213, 149, 181, 110, \
                    237, 75, 181, 54, 252, 107, 201, 39, 156, 191, 217, 231, 100, 174, 185, 155, 115, 86, 238, \
                    156, 173, 81, 231, 214, 190, 184, 57, 203, 79, 206, 181, 114, 117, 107, 156, 171, 156, 234, \
                    92, 231, 84, 171, 58, 168, 245, 213, 208, 26, 174, 72, 237, 113, 0, 151, 159, 64, 104, 64, \
                    0, 150, 164, 2, 0, 0, 0, 0, 0, 8, 0, 0, 34, 0, 66, 0, 0, 8, 169, 85, 32, 0, 0, 2, 37, 72, \
                    136, 128, 2, 34, 17, 80, 0, 132, 0, 168, 32, 74, 2, 133, 0, 32, 16, 34, 137, 2, 8, 2, 72, \
                    128, 160, 0, 42, 10, 42, 0, 64, 128, 137, 2, 9, 32, 40, 32, 138, 0, 138, 0, 138, 0, 160, \
                    32, 162, 10, 136, 8, 64, 2, 34, 17, 32, 128, 4, 8, 9, 65, 66, 160, 16, 8, 5, 133, 33, 16, \
                    32, 4, 4, 10, 65, 64, 64, 16, 21, 2, 132, 128, 40, 32, 34, 1, 10, 8, 0, 0, 160, 0, 164, 2, \
                    0, 0, 8, 0, 0, 162, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 85, 85, 85, 34, 34, 34, 27, 74, 48, 27, 42, 33, 200, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 111, 245, 32, \
                    180, 10, 128, 75, 245, 126, 246, 171, 165, 89, 93, 90, 175, 234, 237, 84, 23, 54, 239, \
                    234, 203, 82, 189, 181, 189, 70, 218, 214, 249, 47, 43, 47, 217, 213, 212, 166, 122, \
                    107, 123, 207, 181, 172, 50, 94, 87, 221, 163, 170, 102, 252, 247, 185, 151, 40, 206, \
                    105, 223, 115, 190, 101, 156, 197, 186, 231, 123, 77, 89, 173, 179, 174, 82, 221, 243, \
                    237, 102, 29, 54, 187, 234, 219, 84, 85, 165, 175, 174, 125, 114, 243, 166, 157, 28, 217, \
                    230, 231, 110, 187, 186, 181, 84, 85, 86, 175, 171, 185, 210, 221, 78, 122, 106, 243, 137, \
                    151, 44, 64, 233, 219, 0, 190, 160, 0, 69, 104, 0, 250, 144, 1, 79, 128, 20, 176, 160, 0, \
                    222, 0, 162, 101, 0, 8, 184, 2, 1, 70, 0, 164, 248, 8, 1, 34, 2, 80, 216, 8, 4, 160, 33, \
                    33, 112, 4, 8, 144, 64, 161, 224, 20, 4, 80, 1, 32, 160, 68, 8, 80, 16, 130, 160, 68, 40, \
                    192, 1, 1, 32, 148, 8, 208, 0, 161, 64, 68, 4, 144, 17, 16, 64, 128, 69, 144, 20, 0, 192, \
                    65, 80, 16, 8, 5, 192, 128, 144, 144, 42, 1, 64, 0, 68, 160, 145, 16, 64, 4, 5, 208, 64, \
                    64, 0, 21, 20, 208, 128, 64, 0, 16, 5, 208, 69, 16, 64, 0, 64, 160, 82, 21, 144, 0, 128, \
                    192, 72, 34, 80, 2, 136, 160, 80, 2, 64, 2, 32, 208, 72, 137, 32, 0, 4, 192, 82, 160, \
                    144, 0, 8, 96, 72, 130, 144, 2, 32, 64, 80, 10, 160, 2, 128, 64, 136, 41, 208, 32, 128, \
                    0, 2, 10, 208, 136, 32, 128, 34, 132, 65, 0, 16, 128, 74, 66, 64, 0, 16, 129, 81, 4, \
                    192, 4, 80, 0, 128, 2, 130, 21, 32, 64, 64, 9, 1, 4, 160, 128, 80, 4, 4, 2, 33, 1, 32, \
                    136, 8, 9, 2, 0, 160, 32, 10, 5, 10, 32, 64, 64, 4, 18, 17, 65, 64, 68, 144, 9, 0, 5, \
                    32, 21, 144, 5, 64, 1, 64, 8, 68, 20, 130, 16, 128, 32, 2, 5, 10, 72, 80, 64, 17, 0, \
                    20, 4, 37, 0, 64, 8, 69, 18, 129, 16, 8, 40, 0, 65, 2, 85, 16, 32, 0, 132, 137, 72, \
                    16, 32, 2, 66, 4, 80, 16, 161, 1, 4, 4, 20, 81, 16, 64, 0, 69, 17, 36, 0, 4, 129, \
                    81, 64, 16, 4, 21, 69, 0, 0, 0, 85, 68, 20, 0, 16, 65, 18, 66, 8, 64, 8, 34, 10, \
                    130, 128, 128, 32, 20, 36, 8, 1, 9, 66, 68, 64, 8, 16, 17, 33, 130, 132, 8, 40, \
                    32, 130, 0, 8, 40, 146, 130, 0, 0, 32, 128, 73, 8, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 85, 85, 85, 34, 34, 34, \
                    27, 74, 48, 27, 42, 33, 200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 0, 0, 100, 0, 0, 144, \
                    0, 0, 237, 128, 0, 86, 0, 0, 185, 240, 0, 78, 136, 0, 245, 244, 0, 42, 43, 0, 219, 220, \
                    0, 109, 99, 64, 150, 190, 0, 233, 81, 192, 63, 190, 128, 201, 75, 64, 118, 245, 128, 219, \
                    90, 208, 36, 165, 64, 255, 126, 144, 145, 163, 224, 110, 220, 128, 187, 55, 112, 69, 217, \
                    128, 250, 174, 112, 45, 83, 128, 214, 252, 240, 171, 75, 64, 118, 182, 176, 153, 105, 192, \
                    239, 158, 112, 84, 235, 128, 171, 53, 112, 125, 218, 208, 130, 34, 0, 80, 0, 64, 0, 129, 0, \
                    0, 0, 0, 0, 0, 0, 4, 2, 0, 0, 144, 36, 80, 4, 1, 2, 64, 144, 136, 18, 4, 33, 64, 80, 4, 10, \
                    2, 64, 128, 136, 20, 34, 33, 1, 8, 4, 68, 65, 64, 16, 20, 21, 1, 0, 0, 84, 73, 80, 1, 0, 5, \
                    32, 42, 32, 133, 0, 130, 16, 68, 40, 66, 16, 1, 16, 130, 136, 4, 32, 34, 80, 8, 136, 2, 162, \
                    1, 16, 0, 40, 68, 74, 130, 1, 0, 16, 80, 34, 64, 4, 136, 10, 16, 33, 32, 66, 4, 0, 16, 160, \
                    170, 2, 8, 0, 72, 34, 68, 0, 128, 145, 42, 20, 0, 128, 65, 4, 17, 8, 81, 4, 34, 4, 80, 128, \
                    128, 2, 8, 40, 32, 34, 0, 72, 136, 128, 2, 2, 32, 32, 160, 0, 136, 8, 144, 2, 130, 0, 40, \
                    40, 64, 0, 1, 16, 138, 144, 0, 32, 4, 160, 132, 80, 0, 17, 2, 128, 64, 32, 16, 5, 8, 128, \
                    16, 66, 0, 65, 16, 80, 20, 4, 0, 128, 161, 0, 34, 8, 64, 8, 66, 16, 129, 16, 128, 36, 4, \
                    0, 128, 64, 144, 21, 18, 0, 64, 64, 64, 8, 9, 0, 33, 34, 16, 132, 0, 128, 16, 168, 32, 4, \
                    2, 0, 65, 16, 128, 20, 66, 32, 128, 8, 0, 34, 128, 144, 8, 42, 0, 64, 0, 64, 18, 137, 16, \
                    4, 32, 0, 64, 138, 64, 20, 0, 16, 129, 34, 128, 36, 8, 32, 0, 128, 0, 148, 42, 128, 1, 0, \
                    32, 68, 9, 0, 16, 160, 64, 68, 4, 0, 1, 17, 64, 80, 64, 16, 4, 20, 128, 33, 0, 0, 136, 82, \
                    144, 2, 0, 0, 80, 72, 160, 1, 2, 0, 20, 32, 0, 65, 10, 160, 0, 64, 0, 85, 9, 0, 0, 32, 64, \
                    34, 10, 0, 8, 128, 0, 160, 34, 128, 5, 8, 0, 32, 64, 0, 136, 18, 128, 33, 64, 0, 4, 9, 0, \
                    160, 64, 0, 9, 0, 0, 64, 32, 0, 10, 0, 0, 32, 0, 0, 0, 0, 0, 128, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    85, 85, 85, 34, 34, 34, 27, 74, 48, 27, 42, 33, 200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 130, 0, 0, 0, 32, 0, 40, 5, 72, \
                    2, 144, 0, 144, 2, 34, 2, 80, 136, 72, 4, 0, 33, 17, 42, 4, 64, 0, 64, 20, 137, 21, 0, \
                    32, 0, 69, 4, 73, 16, 80, 32, 0, 2, 4, 85, 16, 65, 0, 68, 16, 18, 17, 69, 64, 128, 0, \
                    8, 36, 20, 130, 129, 64, 40, 16, 18, 1, 4, 0, 144, 80, 84, 36, 2, 1, 1, 32, 136, 68, \
                    10, 34, 16, 128, 128, 130, 36, 8, 32, 129, 162, 8, 20, 0, 162, 64, 74, 1, 9, 0, 8, \
                    32, 82, 162, 10, 0, 8, 128, 72, 128, 34, 2, 34, 136, 80, 8, 2, 2, 128, 160, 72, 42, \
                    9, 1, 0, 4, 80, 18, 160, 5, 64, 9, 64, 8, 128, 17, 34, 42, 4, 0, 0, 80, 138, 146, 2, \
                    32, 0, 16, 2, 84, 68, 168, 1, 16, 1, 16, 2, 36, 68, 80, 128, 1, 4, 41, 40, 16, 0, 2, \
                    66, 128, 0, 16, 32, 0, 4, 128, 0, 80, 0, 0, 2, 32, 0, 16, 128, 0, 68, 0, 0, 16, 32, \
                    0, 2, 128, 0, 80, 0, 1, 4, 72, 0, 17, 0, 2, 64, 32, 64, 4, 138, 8, 80, 0, 130, 2, \
                    162, 32, 72, 8, 10, 0, 130, 128, 82, 32, 36, 0, 8, 128, 20, 162, 18, 64, 0, 0, 2, 68, \
                    64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 85, 85, 85, 34, 34, 34, 27, 74, 48, 27, 42, 33, 200, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 0, 0, 0, 0, 0, 72, 0, 0, \
                    0, 0, 0, 64, 0, 0, 16, 0, 0, 132, 0, 0, 32, 0, 0, 8, 0, 0, 162, 0, 0, 0, 0, 0, 20, 0, 0, \
                    65, 64, 0, 0, 0, 0, 84, 64, 0, 1, 0, 0, 136, 64, 0, 34, 0, 0, 128, 128, 0, 10, 0, 0, 32, \
                    64, 0, 132, 8, 0, 17, 64, 0, 0, 16, 0, 84, 128, 0, 0, 0, 0, 18, 160, 0, 64, 0, 0, 9, 16, \
                    0, 32, 64, 0, 132, 0, 0, 17, 80, 0, 64, 0, 0, 5, 2, 0, 16, 80, 0, 68, 0, 0, 1, 16, 0, 80, \
                    64, 0, 5, 16, 0, 64, 0, 0, 17, 64, 0, 132, 16, 0, 32, 64, 0, 9, 0, 0, 64, 16, 0, 5, 64, \
                    0, 80, 0, 0, 1, 16, 0, 36, 0, 0, 1, 64, 0, 168, 0, 0, 1, 0, 0, 36, 0, 0, 129, 64, 0, 16, \
                    0, 0, 69, 0, 0, 0, 0, 0, 81, 0, 0, 4, 0, 0, 0, 0, 0, 82, 0, 0, 0, 0, 0, 136, 0, 0, 32, 0, \
                    0, 0, 0, 0, 136, 0, 0, 32, 0, 0, 0, 0, 0, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    85, 85, 85, 34, 34, 34, 27, 74, 48, 27, 42, 33, 200, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, \
                    128, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, \
                    0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, \
                    0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, \
                    0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, \
                    0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, \
                    0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, \
                    1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, \
                    0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, \
                    1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, \
                    0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, \
                    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 128, 0, 0, 0, 0, 1, 0, \
                    0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 128, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, \
                    0, 0, 1, 128, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 128, 0, 0, 0, 0, \
                    1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 128, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, \
                    0, 0, 0, 0, 1, 128, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 128, 0, 0, \
                    0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 128, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, \
                    1, 0, 0, 0, 0, 0, 1, 128, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 128, \
                    0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 128, 0, 0, 0, 0, 1, 0, 0, 0, \
                    128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, \
                    1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, \
                    0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, \
                    1, 0, 0, 0, 128, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 128, 85, 84, 0, 34, 34, 0, 27, 74, 48]
        self.assertEqual(len(data), len(expected))
        self.assertEqual(data, expected)



if __name__ == '__main__':
    unittest.main()


