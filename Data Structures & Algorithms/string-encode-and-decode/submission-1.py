class Solution:

    def encode(self, strs: List[str]) -> str:
        res = [] 
        # for each s in strs
        for s in strs: 
        # get length of s
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)
    
    def decode(self, s: str) -> List[str]:
        res = [] 
        i = 0 
        
        while i < len(s): 
            j = i 
            while s[j] != '#': 
                j += 1 
            length = int(s[i:j])
            i = j + 1
            j = i + length 
            res.append(s[i:j])
            i = j 
            
        return res 
