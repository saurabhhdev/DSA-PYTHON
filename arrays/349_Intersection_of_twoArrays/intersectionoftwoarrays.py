class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        answer = set()
        for num in nums2:
            if num in set1:
                answer.add(num)
        return list(answer)