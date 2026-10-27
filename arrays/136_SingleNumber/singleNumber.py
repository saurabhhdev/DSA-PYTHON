class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for num in nums:
            count = 0
            for x  in nums:
                if x == num:
                    count +=1
            if count == 1:
                return num