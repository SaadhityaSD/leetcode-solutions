class Solution(object):
    def groupAnagrams(self, strs):
        res=defaultdict(list)
        for s in strs:
            sort=''.join(sorted(s))
            res[sort].append(s)
        return list(res.values())    
        
        
                  
                  