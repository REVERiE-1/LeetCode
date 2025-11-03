
"""
For this exercise all we have to do is to check if the given input (an integer - assumption) is a palindrome or not.
Palindrome? 
A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, 
such as madam or racecar.

Approach: numeric reversal. For negative numbers return False. Reverse the
digits of x into rev and compare to the original value. This avoids
converting to string and works efficiently in Python.

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative numbers are not palindromes (because of the leading '-')
        if x < 0:
            return False

        original = str(x)
        rev = str(x)[::-1]  # Reverse the digits of x


        return rev == original


if __name__ == "__main__":
    s = Solution()
    tests = [121, -121, 10, 0, 12321, 1234321]
    for t in tests:
        print(f"isPalindrome({t}) -> {s.isPalindrome(t)}")
        