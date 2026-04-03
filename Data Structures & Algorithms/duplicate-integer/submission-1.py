class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array = set()

        for num in nums:
            if num in array:
                return True
            array.add(num)
        return False
         