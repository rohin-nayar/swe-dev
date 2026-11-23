class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [1,1,2,3,4], val = 1
        # [_,1,2,3,4], do you re-insert the values at new addresses?

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        print(nums)
        return k

        