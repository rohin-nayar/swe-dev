class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return []
        
        store = {}

        for i in range(len(nums)):
            val = target - nums[i]
            if val in store:
                return [store[val], i]

            store[nums[i]] = i
