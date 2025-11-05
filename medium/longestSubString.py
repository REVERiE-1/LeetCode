'''
In this particular exercise, we are given a string and we are to find the length of the longest substring without repeating characters.
A substring is a contiguous sequence of characters within a string.
and we are to return the length of the longest substring that contains no repeating characters basically.


In this problem, I used a sliding window technique with a dictionary data structure to 
keep track of the last seen index of each character.

Having a left and right pointer to represent the current window of non-repeating characters, when 
we encounter a repeating character, we move the left pointer just after the 
previous occurrence of that character to ensure all characters in the window are unique.

Once we update the window, we calculate its length and update the maximum length found so far if necessary.
eg.
Input: s = "abcabcbb"
Start: left=0, last_seen={}
r=0, ch='a': not seen → last_seen['a']=0; current window length 1, max_len=1 (substr="a")
r=1, ch='b': not seen → last_seen['b']=1; length 2, max_len=2 (substr="ab")
r=2, ch='c': last_seen['c']=2; length 3, max_len=3 (substr="abc")
r=3, ch='a': last_seen['a']=0 which is >= left(0) → left = 0+1 = 1; update last_seen['a']=3; window now s[1:4] = "bca"; max_len stays 3
r=4, ch='b': last_seen['b']=1 >= left(1) → left = 2; update last_seen['b']=4; window s[2:5] = "cab"
r=5, ch='c': last_seen['c']=2 >= left(2) → left = 3; update last_seen['c']=5; window s[3:6] = "abc"
r=6, ch='b': last_seen['b']=4 >= left(3) → left = 5; update last_seen['b']=6; window s[5:7] = "cb"
r=7, ch='b': last_seen['b']=6 >= left(5) → left = 7; update last_seen['b']=7; window s[7:8] = "b"
Final max_len = 3


'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        test = "abcabcbb"
        # implement a window sliding technique using dict mapping 
        last_seen = {}
        left = 0 
        max_len = 0
        substr = ""
        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                # ch repeats inside current window: move left just after previous ch
                left = last_seen[ch] + 1
            last_seen[ch] = right
            if right - left + 1 > max_len:
                max_len = right - left + 1
                substr = s[left:right+1]
        return max_len
