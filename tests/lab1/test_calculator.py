import unittest
from src.lab1.calculator import sm
from src.lab1.calculator import raz
from src.lab1.calculator import dl
from src.lab1.calculator import ml


class CalculatorTestCase(unittest.TestCase):

    def test_addition(self):
        self.assertEquals(sm(1,2), 3)

    def test_raz(self):
        self.assertEquals(raz(3,2),1)

    def test_dl(self):
        self.assertEquals(dl(4, 2), 2)

    def test_ml(self):
        self.assertEquals(ml(1, 2), 2)
