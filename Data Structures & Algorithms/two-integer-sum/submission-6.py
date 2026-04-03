class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = {}

        for i, v in enumerate(nums):
            difference = target - v
            if difference in hash1:
                return [hash1[difference], i]
            
            hash1[v] = i
            
        
        