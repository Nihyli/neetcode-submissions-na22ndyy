class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxNum = max(nums)
        minNum = min(nums)
        maxSeq = 0
        currSeq = 0
        hash1 = defaultdict(int)

        for num in nums:
            hash1[num] += 1

        for i in range(minNum ,maxNum+1):
            if i in hash1:
                currSeq += 1
            else:
                maxSeq = max(currSeq, maxSeq)
                currSeq = 0
        
        maxSeq = max(currSeq, maxSeq)
        
        return maxSeq


        