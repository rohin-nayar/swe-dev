class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return []
        
        store = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in store:
                return [store[complement], i]

            store[nums[i]] = i
