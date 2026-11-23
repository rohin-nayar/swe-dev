from typing import List

# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def mergeSort(self, pairs: List['Pair']) -> List['Pair']:
        n = len(pairs)
        if n <= 1:
            return pairs

        mid = n // 2
        left = self.mergeSort(pairs[:mid])
        right = self.mergeSort(pairs[mid:])

        return self._merge(left, right)

    def _merge(self, left: List['Pair'], right: List['Pair']) -> List['Pair']:
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            # <= keeps it stable: equal keys come from the left first
            if left[i].key <= right[j].key:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Append leftovers
        if i < len(left):
            merged.extend(left[i:])
        if j < len(right):
            merged.extend(right[j:])

        return merged

