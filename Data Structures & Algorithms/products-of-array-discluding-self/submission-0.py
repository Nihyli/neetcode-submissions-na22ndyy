class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            total = 1
            behind = -1
            forward = len(nums)

            if i > 0:
                behind = i - 1

            if i < len(nums) - 1:
                forward = i + 1
            
            while behind > -1:
                total *= nums[behind]
                behind -= 1
            
            while forward < len(nums):
                total *= nums[forward]
                forward += 1

            output.append(total)
        
        return output


