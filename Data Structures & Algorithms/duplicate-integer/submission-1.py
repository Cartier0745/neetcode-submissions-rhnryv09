class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arrOrg = []
        for i in range(len(nums)):
            if nums[i] in arrOrg:
                return True
            else:
                arrOrg.append(nums[i])
        return False;