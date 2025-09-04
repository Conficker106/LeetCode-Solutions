#Previous Solutions Runtime Was 13ms
#This One is 5ms

class Solution(object):
    def isPalindrome(self, x):
        if x < 0 :
            return False
        else:
            str_x = str(x)
            length = len(str_x)
            for i in range(0,length/2):
                if str_x[length-1-i]  != str_x[i] :
                    return False
            return True
                    
            

#reduce loop to half time by dividing max length by 2
