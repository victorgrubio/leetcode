import unittest
from valid_palindrome import Solution


class TestValidPalindrome(unittest.TestCase):

    def test_valid_palindrom_true(self):
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(Solution().isPalindrome(s))
    
    
    def test_valid_palindrom_false(self):
        s = "race a car"
        self.assertFalse(Solution().isPalindrome(s))
    
    def test_valid_palindrome_error(self):
        s = "0P"
        self.assertFalse(Solution().isPalindrome(s))