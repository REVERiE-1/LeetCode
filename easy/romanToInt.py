'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Given a roman numeral, convert it to an integer.

For this exercise all we have to really do is understand how roman numbers are constructed then reverse the process.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Now that we see how roman numerals work, we can try to use a mapping strategy in this instant. I will create a dictionary that maps 
each roman numeral to its integer value.

HOWEVER, we have to take into account the subtraction cases. If a smaller numeral appears before a larger numeral, 
we subtract the smaller numeral.

--->
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

'''

# constructed a dictionary that maps each roman numeral to its integer value.
roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

#can we assume that the input is always valid? if that's the case i can simply use a for loop and iterate thru the whole string
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0 

        for i in range(len(s)):
            # Check if this is a subtraction case
            if (i + 1 < len(s)) and (roman_map[s[i]] < roman_map[s[i + 1]]):
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]

        return total
    
if __name__ == "__main__":
    s = Solution()
    tests = ["III", "IV", "IX", "LVIII", "MCMXCIV", "XLII", "CDXLIV"]
    for t in tests:
        print(f"romanToInt({t}) -> {s.romanToInt(t)}")

