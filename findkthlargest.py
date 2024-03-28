class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=sorted(nums)
        c=len(nums)-k
        return h[c]
