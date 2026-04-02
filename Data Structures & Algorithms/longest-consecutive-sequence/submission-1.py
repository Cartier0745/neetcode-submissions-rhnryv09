class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashs = {}
        startDict = {}
        nums.sort()
        for i in range(len(nums)):
            hashs[nums[i]] = i
        if len(nums) == 0:
            lastStartingIndex = 0
        else: lastStartingIndex = -1
        maxLen = 0
        i = 0
        print(hashs)
        for key in hashs:
            if key-1 in hashs:
                i += 1
                continue
            else:
                print(key)
                lenS =  i - lastStartingIndex
                if lenS > maxLen:
                    maxLen = lenS
                lastStartingIndex = i
                i += 1
        #for last set
       
        lenS = i - lastStartingIndex       
        if lenS > maxLen:
            maxLen = lenS
        return maxLen
