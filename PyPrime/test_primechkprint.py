import unittest
import primechkprint


class TestPrime(unittest.TestCase):

    def test_CheckPrime(self):
        self.assertEqual(primechkprint.isPrime(-1),False)#TC_001
        self.assertEqual(primechkprint.isPrime(0),False)#TC_002
        self.assertEqual(primechkprint.isPrime(1),False)#TC_003
        self.assertEqual(primechkprint.isPrime(2),True)#TC_004
        self.assertEqual(primechkprint.isPrime(3),True)#TC_005
        self.assertEqual(primechkprint.isPrime(4),False)#TC_006
        self.assertEqual(primechkprint.isPrime(9),False)#TC_007
        self.assertEqual(primechkprint.isPrime(10),False)#TC_008
        self.assertEqual(primechkprint.isPrime(11),True)#TC_009
        self.assertEqual(primechkprint.isPrime(99),False)#TC_010
        self.assertEqual(primechkprint.isPrime(100),False)#TC_011
        self.assertEqual(primechkprint.isPrime(99999),False)#TC_012
    
    def test_PrimePrint(self):
        self.assertEqual(primechkprint.isPrime(17),True)
        self.assertEqual(primechkprint.isPrime(19),True)
    


if __name__ == '__main__':
    unittest.main()