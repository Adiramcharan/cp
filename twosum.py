class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        c=0
        l=[]
        a=len(nums)
        for i in range(a):
            for j in range(i+1,a):
                c=nums[i]+nums[j]
                if c==target:
                    l.append(i)
                    l.append(j)
                    break
                else:
                    continue
        return l