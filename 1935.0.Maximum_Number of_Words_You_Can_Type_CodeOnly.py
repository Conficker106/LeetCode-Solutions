class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        words = text.split()
        count = len(words)
        letters = list(brokenLetters)
        for word in words :
            for letter in letters:
                if letter in word:
                    count = count - 1
                    break
        return count 
