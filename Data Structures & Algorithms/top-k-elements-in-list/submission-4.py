class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        hash1 = {}

        for num in nums:
            if num not in hash1:
                hash1[num] = 0
            hash1[num] += 1
        
        #iterate over the hashmap k times and find the biggest value

        for i in range(k):
            maxVal = max(hash1.values())

            for i, n in hash1.items():
                if n == maxVal:
                    maxKey = i

            output.append(maxKey)
            del hash1[maxKey]
        
        return output