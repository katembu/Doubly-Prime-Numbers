import unittest
from DoublyPrimes import Doubly


class TestDoubly(unittest.TestCase):
    # Check Prime Number [2 , 3, 5]
    def test_isprime(self):
        doubly = Doubly()
        self.assertTrue(doubly.is_prime(2))

    # Check Numbers Not Prime Example [9 , 4, 8]
    def test_not_prime(self):
        doubly = Doubly()
        self.assertFalse(doubly.is_prime(9))

    # Check Doubly
    # Number should be prime
    # Its elements/characters should be prime too.
    # Example  Prime Example [19 , 23]
    def test_isdoubly(self):
        doubly = Doubly()
        self.assertTrue(doubly.is_prime(19))
        self.assertFalse(doubly.is_doubly(str(19)))

    def test_doublylist(self):
        correct_list = [1, 2, 3, 5, 7, 11, 13, 17, 23, 31, 37, 53, 71, 73]
        doubly = Doubly(100)
        p = list(doubly.prime_number_generator())
        doubly_list = doubly.doubly_list(p)
        self.assertFalse(cmp(correct_list, doubly_list))


if __name__ == '__main__':
    unittest.main()
