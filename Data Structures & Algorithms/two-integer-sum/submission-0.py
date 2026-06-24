class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value = {}
        for i in range(len(nums)):
            if target-nums[i] in value:
                return [value[target-nums[i]],i]
            value[nums[i]] = i
        