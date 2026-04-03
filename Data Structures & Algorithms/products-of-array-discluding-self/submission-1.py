class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        total = 1
        zero_count = 0

        for i in range(len(nums)):
            if nums[i]:
                total *= nums[i]
            else:
                zero_count += 1
        
        holder = total

        for i in range(len(nums)):
            total = holder
            if zero_count > 1:
                output.append(0)
            elif nums[i] == 0:
                output.append(total)
            elif zero_count > 0:
                output.append(0)
            else:
                total = total // nums[i]
                output.append(total)
        
        return output


