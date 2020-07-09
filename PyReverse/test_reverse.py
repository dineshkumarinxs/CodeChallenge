import unittest
import reverse


class TestPrime(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(reverse.reverse_num(0),0) #TC_01
        self.assertEqual(reverse.reverse_num(1),1) #TC_02
        self.assertEqual(reverse.reverse_num(12),21) #TC_03
        self.assertEqual(reverse.reverse_num(99),99) #TC_04
        self.assertEqual(reverse.reverse_num(12345),54321) #TC_05
        self.assertEqual(reverse.reverse_num(1221),1221) #TC_06
        self.assertEqual(reverse.reverse_num(29535),53592) #TC_07
        
    def test_negative(self):
        self.assertEqual(reverse.reverse_num(-1234),"Invalid number") #TC_08
        self.assertEqual(reverse.reverse_num(123456789),987654321) #TC_09
        

    if __name__ == '__main__':
        unittest.main()