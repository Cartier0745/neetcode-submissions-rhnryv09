class Solution:

    def encode(self, strs: List[str]) -> str:        
        encoded = ""
        for stre in strs:
            encoded += str(len(stre)) + "#" + stre

        return encoded

    def decode(self, s: str) -> List[str]:
        arr = []
        indexk = 0
        j = 0
        while indexk < len(s):
            j = indexk
            while s[j] != '#':
                j += 1
            length = int(s[indexk:j])
            arr.append(s[j+1 : j+1+length])
            indexk = j + 1 + length
        return arr
