class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        
        dupCheck = {}

        for num in nums:
            if num not in dupCheck:
                dupCheck[num] = 1
            else:
                return True
        else:
            return False