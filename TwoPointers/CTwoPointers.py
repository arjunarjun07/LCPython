

class CTwoPointers:
    
    def normalisestr(self, s:str) -> str:
        if s.isalnum():
            return True
        else:
            return False
    
    def isPalindrome(self, s: str) -> bool:        
        res = True
        
        s = s.upper()
        normalised_list = list(filter(self.normalisestr, s))
        normalised_str = "".join(normalised_list)
        
        i,j = 0, len(normalised_str) -1
        
        while i < j:
            if(normalised_str[i] == normalised_str[j]):
                i += 1
                j -= 1
            else:
                res = False
                break
        
        return res