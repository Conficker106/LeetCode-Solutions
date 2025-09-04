# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The problem asks whether a given integer reads the same forward and backward.
My first thought was to convert the number into a string and compare characters from both ends.

# Approach
<!-- Describe your approach to solving the problem. -->
1.Check negatives:
If the number is negative, it can never be a palindrome because of the - sign.

2.Convert to string:
Convert the number into a string for easy character comparisons.

3.Compare both ends:
Use a loop to compare the first and last characters moving towards the center:
A) If any pair doesn't match, return False.
B) If all pairs match, return True.
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
O(n)
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
O(n)
# Code
```python []
class Solution(object):
    def isPalindrome(self, x):
        if x < 0 :
            return False
        else:
            str_x = str(x)
            length = len(str_x)
            for i in range(0,length):
                if str_x[length-1-i]  != str_x[i] :
                    return False
            return True
                    
            
        
```
