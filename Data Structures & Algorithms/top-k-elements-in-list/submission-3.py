class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxarr = []
        maxheap = []
        dicts = {}
        dictsFreq = {}
        kcount = k
        for num in nums:
            freq = 1+ dicts.get(num,0)
            dicts[num] = freq
        for key,value in dicts.items():
           
            arr = []
            arr = dictsFreq.get(value,[])
            if arr is None:
                arr = []
            else:  arr.append(key)
            dictsFreq[value] = arr
            # print(dicts)
        for key in dictsFreq:
            heapq.heappush(maxheap, key * -1)
            
        print('dictsFreq',dictsFreq)
            
        while len(maxheap):
            tempFreq = heapq.heappop(maxheap) * -1
            print('tempFreq', tempFreq)
            arr = dictsFreq.get(tempFreq,[])
          
            print('arr=',arr)
            if len(arr) >= kcount :
                maxarr.extend(arr[0:kcount])
                break;
            else:
                maxarr.extend(arr)
                kcount -= len(arr)
        return maxarr
        