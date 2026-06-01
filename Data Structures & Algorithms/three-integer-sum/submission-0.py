class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answer = set()
        for in1 in range(len(nums)-2):
            for in2 in range(in1+1,len(nums)):
                num  = (nums[in1] + nums[in2])*-1
                if num in nums[in2+1:len(nums)]:
                    if  nums[in1] <num < nums[in2]:
                        ans = (nums[in1],num,nums[in2])
                    elif nums[in2] <num < nums[in1]:
                        ans = (nums[in2],num,nums[in1])
                    elif nums[in2] > num:
                        if nums[in2] > nums[in1]:
                            ans =(num,nums[in1],nums[in2])
                        else:
                            ans =(num,nums[in2],nums[in1])
                    else:
                        if nums[in2] > nums[in1]:
                            ans =(nums[in1],nums[in2],num)
                        else:
                            ans =(nums[in2],nums[in1],num)

        
                    print(ans)
                    answer.add(ans)
        answer = list(answer)            
        print(answer)
        return answer