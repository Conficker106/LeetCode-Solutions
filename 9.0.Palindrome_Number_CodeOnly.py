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
                    
            
        
