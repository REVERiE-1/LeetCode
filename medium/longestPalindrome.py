'''
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome when it reads the same backward as forward.

I've encountered a similar problem before with isPalindrome where we checked if a string is a palindrome 
by comparing characters from both ends towards the center.

In this problem, I believe we can mimic the approach of the previous problem. 

Using the similar approach of sliding window technique, we can expand around potential centers of palindromes.

The idea is to consider each character (and the gap between characters) as a potential center of a palindrome,
and expand outwards while the characters on both sides are equal.

'''



class Solution:
    '''
    Helper function to expand around the center and find the longest palindrome.
    given two indices L and R (initially equal for odd centers, or adjacent for even centers), 
    expand L-- and R++ while L >= 0, R < n, and s[L] == s[R].

    When expansion stops, return the start index and length (or end index).

    '''

    def expandAroundCenter(self, s: str, left: int, right: int) -> (int, int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        best_start = 0
        best_len = 0 

        if not s: 
            return ""

        for i in range(len(s)-1):
            # odd length palindromes
            left1, right1 = self.expandAroundCenter(s, i, i)
            len1 = right1 - left1 + 1
            if len1 > best_len:
                best_len = len1
                best_start = left1

            # even length palindromes
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            len2 = right2 - left2 + 1
            if len2 > best_len:
                best_len = len2
                best_start = left2



        return s[best_start:best_start + best_len+1]
    

    
