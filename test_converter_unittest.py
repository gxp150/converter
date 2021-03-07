import pytest
import unittest
from converter import fahrenheit

class TestCelsius(unittest.TestCase):
    def test_temperature(self):
        self.assertAlmostEqual(fahrenheit(27),27*(9/5)+32)
        self.assertAlmostEqual(fahrenheit(0),32)
        self.assertAlmostEqual(fahrenheit(-4),(-4)*(9/5)+32)
        self.assertRaises(TypeError, fahrenheit, True)
        self.assertRaises(TypeError, fahrenheit, "34")
        
def testing_a_random_TypeError():
    """Testing a random TypeError."""
    with pytest.raises(TypeError):
        TypeError = "Must be fahrenheit"
        TypeError = "Must be 34"

unittest.main()
