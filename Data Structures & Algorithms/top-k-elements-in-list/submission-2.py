class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Thoughts:
        - For each number count how many times it occurs in the sequence
        - Based on the count then reorder from highest to lowest 
        Ideas:
        - Dictionary which can be used to keep track of the occurences
        - nums = [1,2,2,3,3,3,3]; dict = {1:1, 2:2, 3:4}
        - And then iterate through the values from dict, need to figure out the sort
        - Reduce k as each value is stored in a list until k is 0
        Approach:
        """
        # Step 1: Count the frequency of each number
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Step 2: Create buckets indexed by frequency
        # Index i contains all elements that appear i times
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        
        # Step 3: Collect k most frequent elements by iterating buckets backwards
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res

