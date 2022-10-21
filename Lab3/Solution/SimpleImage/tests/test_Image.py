import unittest

from Image import *


class TestImage(unittest.TestCase):
    def test_ctor(self):
        image = Image(128, 128)
        self.assertEqual(image.width, 128)
        self.assertEqual(image.height, 128)
        self.assertEqual(len(image.pixels), 128 * 128)

    def test_clear(self):
        image = Image(128, 128)
        image.clear(255, 0, 0, 255)
        for pixel in image.pixels:
            r, g, b, a = pixel.get_rgba()
            self.assertEqual(r, 255)
            self.assertEqual(g, 0)
            self.assertEqual(b, 0)
            self.assertEqual(a, 255)

    def test_save(self):
        image = Image(128, 128)
        image.clear(255, 0, 0, 255)
        self.assertTrue(image.save("test.png"))
        image.clear(255, 0, 0, 255)
        image.save("red.png")
        image.clear(0, 255, 0, 255)
        image.save("green.png")
        image.clear(0, 0, 255, 255)
        image.save("blue.png")

    def test_load(self):
        image = Image(0, 0)
        self.assertTrue(image.load("test.png"))
        self.assertEqual(image.width, 128)
        self.assertEqual(image.height, 128)
        for pixel in image.pixels:
            self.assertEqual(pixel.red(), 255)
            self.assertEqual(pixel.green(), 0)
            self.assertEqual(pixel.blue(), 0)
            self.assertEqual(pixel.alpha(), 255)

    def test_set_get(self):
        image = Image(10, 10)
        for x in range(0, 10):
            for y in range(0, 10):
                image.set_pixel(x, y, 128, 255, 64, 255)
        image.save("setPixel.png")

        for x in range(0, 10):
            for y in range(0, 10):
                r, g, b, a = image.get_pixel(x, y)
                self.assertEqual(r, 128)
                self.assertEqual(g, 255)
                self.assertEqual(b, 64)
                self.assertEqual(a, 255)

    def test_get_average_rgba(self):
        image = Image(20, 20)
        image.clear(255, 0, 0)
        r, g, b, a = image.get_average_rgba()
        self.assertEqual(r, 255)
        self.assertEqual(g, 0)
        self.assertEqual(b, 0)
        self.assertEqual(a, 255)

    def test_get_average_hsv(self):
        image = Image(20, 20)
        image.clear(255, 0, 23)
        h, s, v = image.get_average_hsv()
        self.assertEqual(h, 355)
        self.assertEqual(s, 100)
        self.assertEqual(v, 100)
