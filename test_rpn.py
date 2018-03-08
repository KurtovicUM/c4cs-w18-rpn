#!/usr/bin/env python3
import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
        print("addition passed")

    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
        print("subtraction passed")


    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
        print("multiplication passed")

    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
        print("division passed")

    def test_expo(self):
        result = rpn.calculate("2 2 ^")
        self.assertEqual(4, result)
        print("exponential passed")