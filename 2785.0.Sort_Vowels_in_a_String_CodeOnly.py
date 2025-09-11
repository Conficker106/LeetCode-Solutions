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
