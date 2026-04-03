class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = {}

        for i,v in enumerate(nums):
            hash1[v] = i
        
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hash1 and hash1[difference] != i:
                return[i, hash1[difference]]


        