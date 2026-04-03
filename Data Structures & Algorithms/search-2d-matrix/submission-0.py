class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(nums: List[List[int]], target: int):
            l,r = 0, len(nums) - 1

            while l <= r:
                m = (l+r)//2

                if nums[m] < target:
                    l = m+1
                elif nums[m] > target:
                    r = m-1
                else:
                    return m
            return -1
        
        for i in range(len(matrix)):
            if binarySearch(matrix[i], target) != -1:
                return True
        
        return False