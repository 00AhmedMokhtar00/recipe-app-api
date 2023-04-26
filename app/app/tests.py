from django.test import SimpleTestCase
from . import calc


class CalcTests(SimpleTestCase):
    def test_add_nimbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = calc.subtract(5, 10)
        self.assertEqual(res, 5)
