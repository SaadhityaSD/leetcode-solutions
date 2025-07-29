class Solution(object):
    def isAnagram(self, s, t):
        if len(str(s))!=len(str(t)):
            
            return False
        return sorted(s)==sorted(t)
           
              
       
       
        