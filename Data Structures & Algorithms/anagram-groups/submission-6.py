class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = defaultdict(list)
        rest = []
        for st in strs:
            temp = "".join(sorted(st))
            arr = []
            arr = dicts.get(temp,[])
            print('arr=', arr)
            if arr is None:
                arr = []
            else: arr.append(st)
            dicts[temp] = arr
            print(dicts)
        print(dicts)
        for val in dicts.values():
            rest.append(val)
        return rest      