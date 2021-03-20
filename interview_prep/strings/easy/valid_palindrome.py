import re


class Solution:
    """
    Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
    """
    def isPalindrome(self, s: str) -> bool:
        x = re.findall("[a-zA-Z0-9]", s)
        x = ''.join(x).lower()
        return x[:] == x[::-1]