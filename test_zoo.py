# 65070503410 - Charunthon Limseelo | test_zoo.py
# Submitted to Aj. Chaiyong Ragkhitwetsagul
import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    # Add your additional test cases here.

    def test_child_ticket_price_c1b1(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Invalid age")

    def test_child_ticket_price_c1b2(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test_child_ticket_price_c1b3(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_child_ticket_price_c1b4(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
    
    def test_child_ticket_price_c1b5(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

if __name__ == '__main__':
    unittest.main()