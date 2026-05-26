class Solution:
    def isPalindrome(self, s: str) -> bool:
        onlyalphas =''
        
        for i in range(len(s)):
            if ord(s[i]) > 47 and ord(s[i]) <58:
                onlyalphas += s[i]
            elif ord(s[i]) > 64 and ord(s[i]) <91:
                onlyalphas += s[i]
            elif ord(s[i]) > 96 and ord(s[i]) <123:
                onlyalphas += s[i]
        s = onlyalphas
       
        if (len(s) < 1):
            return True
        s = s.lower()
        isEven = len(s) %2 == 0 
        news = ''
        if isEven:  
            half = int(len(s)/2)
            if (s[half] != s[half-1]):
                return False
            else:
                s1 = s[0:half]
                s2 = s[half+1:len(s)]
                news = s1 + s2
                half -= 1
        else:
            half = math.floor(len(s)/2)
            news = s

        i = 1
        while i + half < len(news):
            
            if news[half - i] != news[half + i] :
                
                return False
            else : 
                i += 1
        return True