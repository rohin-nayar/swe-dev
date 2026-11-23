class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # nums = [3,4,5,6]
        # target = 7
        # store = {3:0, 4:1, 5:3, 6:3}
        store = {}
        for ind,num in enumerate(nums):
            complement = target - num
            if complement in store:
                return [store[complement], ind]
            
            store[num] = ind