# Intuition
Took help from here:
https://algomap.io/problems/longest-common-prefix

# Code
```python []
class Solution(object):
    def longestCommonPrefix(self, strs):
        min_length = 201 # according to constraints max can be 200
        for i in strs:
            if len(i) < min_length:
                min_length = len(i)
        i = 0
        while i < min_length:
            for j in strs:
                if j[i] != strs[0][i]:
                    return j[:i]
            i += 1
        return strs[0][:i]
        
```
