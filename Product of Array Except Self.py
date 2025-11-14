from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        resLeft=[1] * n
        resRight=[1] * n
        for i in range(0,len(nums)):
            if i==0:
                resLeft[0]=1
            else:
                resLeft[i]=resLeft[i-1]*nums[i-1]
                # i=1 res[1]=1*1=1 
                #i=2 res[2]=1*nums[1]=2
                #i=3 res[3]=nums[2]*2=6
        for i in range(n-1,-1,-1):
            if i==n-1:
                resRight[n-1]=1
            else:
                resRight[i]=resRight[i+1]*nums[i+1]
        res=[1]*n
        for i in range(0,len(nums)):
            res[i]=resLeft[i]*resRight[i]
        return res