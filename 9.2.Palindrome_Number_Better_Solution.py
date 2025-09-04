#Removed IF Condition making it more Better
class Solution(object):
    def isPalindrome(self, x):
            str_x = str(x)
            length = len(str_x)
            for i in range(0,length/2):
                if str_x[length-1-i]  != str_x[i] :
                    return False
            return True
                    
