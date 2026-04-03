class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numSet = set(nums)
        maxSeq = 0

        for num in numSet:
            if num - 1 not in numSet:
                conSeq = 1
                while num + conSeq in numSet:
                    conSeq += 1
                maxSeq = max(maxSeq, conSeq)
            
        return maxSeq
            

        