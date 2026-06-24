class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        curr_count = 0
        for i in nums:
            if i == 1:
                curr_count+=1
            else:
                max_count = max(curr_count,max_count)
                curr_count = 0

        return max(curr_count,max_count)