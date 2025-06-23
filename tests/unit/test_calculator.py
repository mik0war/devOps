from unittest import TestCase

import calculator


class Test(TestCase):
    def test_invalid_data(self):
        expected = 'Неверные входные данные'
        actual = calculator.plus('3', 2)

        self.assertEqual(expected, actual)

    def test_plus(self):
        expected = 5
        actual = calculator.plus(3, 2)

        self.assertEqual(expected, actual)

    def test_minus(self):
        expected = 2.5
        actual = calculator.minus(3.3, 0.8)

        self.assertEqual(expected, actual)

    def test_mul(self):
        expected = 25
        actual = calculator.mul(5, 5)

        self.assertEqual(expected, actual)

    def test_div(self):
        expected = 3.0
        actual = calculator.div(18.0, 6)

        self.assertEqual(expected, actual)

    def test_div_zero(self):
        expected = 'Деление на 0'
        actual = calculator.div(3, 0)

        self.assertEqual(expected, actual)
