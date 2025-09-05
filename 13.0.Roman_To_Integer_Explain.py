# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first thought was to map each Roman numeral symbol to its integer value and process the string from left to right.
The only tricky part is handling cases like IV = 4 or IX = 9, where a smaller value comes before a larger one.
# Approach
<!-- Describe your approach to solving the problem. -->
Create a dictionary mapping Roman symbols (I, V, X, L, C, D, M) to their integer values.
1.Loop through the string:
2.If the current value is less than the next one, subtract it. (e.g., I before V → subtract 1)
3.Otherwise, add it.
4.Return the final sum after processing all characters.
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
O(n)
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
O(1)
# Code
```python []
class Solution(object):
    def romanToInt(self, s):
        roman_to_int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
                ans -= roman_to_int[s[i]]
            else:
                ans += roman_to_int[s[i]]

        return ans
        
```
