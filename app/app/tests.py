from django.test import TestCase
from app.calc import add, sub


class CalcTexts(TestCase):

    def test_add_numbers(self):
        """testing that they are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """ vals are subtracted and returned"""
        self.assertEqual(sub(5, 11), 6)