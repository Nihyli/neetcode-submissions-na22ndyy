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
                    return True
            return False
        
        array = matrix[0]
        for i in range (1,len(matrix)):
            array += matrix[i]

        return binarySearch(array, target)