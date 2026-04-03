class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in array:
                return [nums.index(difference) , i]
            if nums[i] not in array:
                array[nums[i]] = 0
            array[nums[i]] += 1
  
        

        

        