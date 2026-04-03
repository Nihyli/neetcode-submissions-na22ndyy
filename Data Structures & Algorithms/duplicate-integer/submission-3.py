class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasher = {}

        for num in nums:
            if num not in hasher:
                hasher[num] = 1
            else:
                return True


        return False

        