class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        output = []

        for i in range(len(nums)):
            if nums[i] not in frequency:
                frequency[nums[i]] = 0
            frequency[nums[i]] += 1
        
        for i in range(k):
            maxVal = max(frequency.values())
            for i, n in frequency.items():
                if n == maxVal:
                    maxKey = i
            output.append(maxKey)
            del frequency[maxKey]
            
        return output
        
        