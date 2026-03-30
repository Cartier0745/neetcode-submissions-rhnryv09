class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = 1
        output = [1] * len(nums)
        #suffx = [1] * len(nums)
        for i in range(len(nums)):
            
            if i == 0:
                output[i] = 1
            else: 
                res *= nums[i-1]
                output[i] = res

        print(output)
        res = 1
        for i in range(len(nums), 0, -1):
            index = i - 1
            
            output[index] *= res
            res *= nums[index]
    
        return output