class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxSeq = 0

        for i in range(len(nums)):
            if nums[i] - 1 in nums:
                continue
            j = 1
            conSeq = 1
            while nums[i] + j in nums:
                conSeq += 1
                j += 1
            
            maxSeq = max(maxSeq, conSeq)
        
        return maxSeq
            

        