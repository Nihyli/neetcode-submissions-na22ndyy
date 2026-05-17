class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        We can do this with a two array solution where one keeps track of suffix value and the other prefix value
        then multiply everything together
        """

        pre = []
        suf = []
        sol = []

        val = 1
        for num in nums:
            pre.append(val)
            val = num * val
            
        
        val = 1

        for i in range(len(nums) - 1,-1, -1):
            suf.append(val)
            val = nums[i] * val

        
        suf.reverse()
        
        for i in range(len(nums)):
            sol.append(pre[i] * suf[i])

        return sol

        