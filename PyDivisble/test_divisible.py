import unittest
import divisible


class TestDivisible(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(divisible.divisib(1),[1])#TC_001
        self.assertEqual(divisible.divisib(2),[1, 2])#TC_002
        self.assertEqual(divisible.divisib(3),[1, 3])#TC_003
        self.assertEqual(divisible.divisib(4),[1, 2, 4])#TC_004
        self.assertEqual(divisible.divisib(5),[1, 5])#TC_005
        self.assertEqual(divisible.divisib(6),[1, 2, 3, 6])#TC_006
        self.assertEqual(divisible.divisib(7),[1, 7])#TC_007
        self.assertEqual(divisible.divisib(8),[1, 2, 4, 8])#TC_008
        self.assertEqual(divisible.divisib(9),[1, 3, 9])#TC_009
        self.assertEqual(divisible.divisib(10),[1, 2, 5, 10])#TC_010
        self.assertEqual(divisible.divisib(33),[1, 3])#TC_011
        self.assertEqual(divisible.divisib(44),[1, 2, 4])#TC_012
        self.assertEqual(divisible.divisib(25),[1, 5])#TC_013
        self.assertEqual(divisible.divisib(42),[1, 2, 3, 6, 7])#TC_014
        self.assertEqual(divisible.divisib(49),[1, 7])#TC_015
        self.assertEqual(divisible.divisib(64),[1, 2, 4, 8])#TC_016
        self.assertEqual(divisible.divisib(81),[1, 3, 9])#TC_017
        self.assertEqual(divisible.divisib(100),[1, 2, 4, 5, 10])#TC_018
        self.assertEqual(divisible.divisib(71),[1])#TC_019
        self.assertEqual(divisible.divisib(99999),[1, 3, 9])#TC_020
        
     
    def test_negative(self):
        self.assertEqual(divisible.divisib(-10),[1, 2, 5, 10])#TC_021
        self.assertEqual(divisible.divisib(0),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])#TC_020
        

if __name__ == '__main__':
    unittest.main()