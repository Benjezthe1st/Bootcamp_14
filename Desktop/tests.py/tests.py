import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""
    def test_is_not_int():
    	assert int(is_prime())
    def test_is_zero_prime():
        assert not is_prime(0)

    def test_is_one_prime():
        assert not is_prime(1)

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

    def test_negative_number(self):
    """Is a negative number correctly determined not to be prime?"""
    for index in range(:0):
        self.assertFalse(is_prime(index))


if __name__ == '__main__':
    unittest.main()