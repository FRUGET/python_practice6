import unittest
from app.calculator import Calculator

class Test(unittest.TestCase):
   def setUp(self):
       self.calc = Calculator(25, 5)
       self.calc2 = Calculator(15, 3)

   def test_add(self):
       self.assertEqual(self.calc.add(), 30)
       self.assertEqual(self.calc2.add(), 18)

   def test_subtract(self):
       self.assertEqual(self.calc.subtract(), 20)
       self.assertEqual(self.calc2.subtract(), 12)

   def test_multiply(self):
       self.assertEqual(self.calc.multiply(), 125)
       self.assertEqual(self.calc2.multiply(), 45)

   def test_divide(self):
       self.assertEqual(self.calc.divide(), 5)
       self.assertEqual(self.calc2.divide(), 5)

   def test_power(self):
       self.assertEqual(self.calc.power(), 9765625)
       self.assertEqual(self.calc2.power(), 3375)

if __name__ == '__main__':
   unittest.main()
