from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:        
        counter = Counter(nums)
        max_count, output = 0, 0
        
        for k, v in counter.items():
            if v > max_count:
                max_count = v
                output = k
        
        return output