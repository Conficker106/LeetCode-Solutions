# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first thought was to check each pair of numbers until I find the pair that sums to the target value.
# Approach
<!-- Describe your approach to solving the problem. -->
I used a brute-force approach:
1.Loop through the list using two nested loops.
2.For each element at index i, check all other elements at index j.
3.If the sum of nums[i] + nums[j] equals the target, return the indices [i, j].
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
O(n^2)
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
O(1)
# Code
```python []
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if j != i :
                    if nums[i] + nums[j] == target :
                        sol = [i,j]
                        return sol


        
```
