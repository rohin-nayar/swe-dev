from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            count = [0]*26

            for char in word:
                count[ord(char)-ord("a")] +=1
            
            key = tuple(count)
            # the key is to ensure the key is an immutable object
            # dictionary keys must be hasbable
            groups[key].append(word)
        
        return list(groups.values())
