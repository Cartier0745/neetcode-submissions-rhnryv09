class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = 1
        output = [1] * len(nums)
        #suffx = [1] * len(nums)
        for i in range(len(nums)):
                
                output[i] = res
                res *= nums[i]

        print(output)
        res = 1
        for i in range(len(nums), 0, -1):
            index = i - 1
            
            output[index] *= res
            res *= nums[index]
    
        return output