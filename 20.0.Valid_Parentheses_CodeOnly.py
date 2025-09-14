class Solution(object):
    def isValid(self, s):
        stack=[]
        i = 0
        for i in range(0, len(s)):
            if s[i]=='('or s[i]=='['or s[i]=='{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                top=stack.pop()
                if s[i]==')'and top!='(':
                    return False
                if s[i]==']'and top!='[':
                    return False
                if s[i]=='}'and top!='{':
                    return False
        if len(stack) != 0 :
            return False
        return True

        
