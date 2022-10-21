import unittest

from RGBA import *


class TestRGBA(unittest.TestCase):
    def test_ctor(self):
        pixel = RGBA()
        r, g, b, a = pixel.get_rgba()
        self.assertEqual(r, 0)
        self.assertEqual(g, 0)
        self.assertEqual(b, 0)
        self.assertEqual(a, 255)

    def test_ctor_user(self):
        pixel = RGBA(123, 255, 0, 255)
        r, g, b, a = pixel.get_rgba()

        self.assertEqual(r, 123)
        self.assertEqual(g, 255)
        self.assertEqual(b, 0)
        self.assertEqual(a, 255)

    def test_colour_access(self):
        pixel = RGBA(128, 255, 56, 25)
        self.assertEqual(pixel.red(), 128)
        self.assertEqual(pixel.green(), 255)
        self.assertEqual(pixel.blue(), 56)
        self.assertEqual(pixel.alpha(), 25)

    def test_from_hex(self):
        pixel = RGBA.from_hex("FF2F3F00")
        self.assertEqual(pixel.red(), 255)
        self.assertEqual(pixel.green(), 47)
        self.assertEqual(pixel.blue(), 63)
        self.assertEqual(pixel.alpha(), 0)

        with self.assertRaises(ValueError):
            pixel = RGBA.from_hex("nonsense")

    def test_set(self):
        pixel = RGBA()
        pixel.set(255, 0, 0, 255)
        self.assertEqual(pixel.red(), 255)
        self.assertEqual(pixel.green(), 0)
        self.assertEqual(pixel.blue(), 0)
        self.assertEqual(pixel.alpha(), 255)

    def test_to_hsv(self):
        test_values = [
            [(255, 0, 23), (355, 100, 100)],
            [(156, 146, 147), (354, 6, 61)],
            [(81, 118, 158), (211, 49, 62)],
        ]
        pixel = RGBA()
        for value in test_values:
            print(value)
            pixel.set(value[0][0], value[0][1], value[0][2])
            h, s, v = pixel.as_hsv()
            self.assertEqual(h, value[1][0])
            self.assertEqual(s, value[1][1])
            self.assertEqual(v, value[1][2])
