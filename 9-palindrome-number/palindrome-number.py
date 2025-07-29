class Solution(object):
    def isPalindrome(self, x):
  
        if (x<0):
            return False
        rev=x    
        num=0    
        while rev: 
            num =(num * 10) +(rev % 10)
            rev//=10
        return x == num       
        
         
        
        


        