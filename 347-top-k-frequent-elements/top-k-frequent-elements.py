class Solution(object):
    def topKFrequent(self, nums, k):
        count={}
        fre=[[] for i in range(len(nums)+1)]
        for num in nums:
            count[num]=1+count.get(num,0)
        for num,cnt in count.items():
            fre[cnt].append(num)
        res=[]
        for i in range(len(fre)-1,0,-1):
            for num in fre[i]:
                res.append(num)
                if len(res)==k:
                    return res        
       
       
       