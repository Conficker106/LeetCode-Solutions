# Intuition
The problem asks us to sort only the vowels in a string while keeping the positions of the consonants and other characters unchanged.
The first thought is:

Extract all vowels.

Sort them.

Replace them back into their original positions.

This way, consonants remain untouched, and vowels appear in sorted order.

# Approach
Identify vowels: Create a set or string containing all vowels (both uppercase and lowercase).

Traverse the string:

Store the vowels and their positions separately.

Sort vowels: Sort the collected vowels in ascending order.

Reinsert vowels: Using the stored positions, replace vowels in the original string with the sorted ones.

Return final string: Join the list back into a single string.
# Complexity
- Time complexity:
Time Complexity:

Traversing the string: O(n)

Sorting vowels: O(k log k), where k = number of vowels

Reinserting vowels: O(k)
Overall: O(n + k log k) (k ≤ n)

- Space complexity:
Extra space for vowels and positions → O(k)

# Code
```python []
class Solution(object):
    def sortVowels(self, s):
        vowels = "aeiouAEIOU"
        slist = list(s)
        position = []
        vlist = []
        for i in range(0, len(s)):
            if slist[i] in vowels:
                position.append(i)
                vlist.append(slist[i])
        vlist.sort()
        var = int(0);
        for pos in position:
            slist[pos] = vlist[var]
            var = var + 1
        return "".join(slist)






        
