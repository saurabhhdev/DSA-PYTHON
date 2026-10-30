# KADANE 'S  ALGORITHM

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur = best = nums[0]
        for i in nums[1:]:
            if cur > 0 :
                cur+=i
            else:
                cur = i
            best = max(best,cur)
        return best
