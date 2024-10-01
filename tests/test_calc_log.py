import math
import unittest
from parameterized import parameterized
from app.main import Calculator
from app.error import InvalidInputException


class TestLogarithm(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()

    def tearDown(self) -> None:
        ...

    @parameterized.expand([
        (100, 10, 2.0),
        (8, 2, 3.0),
        (27, 3, 3.0),
    ])
    def test_valid_input(self, a, base, expected):
        self.assertAlmostEqual(self.calc.log(a, base), expected)

    @parameterized.expand([
        (0, 2),
        (1, 2),
        (-10, 2),
        (10, 0),
        (10, 1),
        (10, -2),
    ])
    def test_invalid_input(self, a, base):
        with self.assertRaises(InvalidInputException):
            self.calc.log(a, base)

    @parameterized.expand([
        ("10", 2),
        (10, "2"),
    ])
    def test_invalid_input_non_numeric(self, a, base):
        with self.assertRaises(TypeError):
            self.calc.log(a, base)


if __name__ == "__main__":
    unittest.main()
