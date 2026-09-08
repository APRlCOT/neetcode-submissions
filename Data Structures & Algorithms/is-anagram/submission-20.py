class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for chars in s:
            if chars in countS:
                countS[chars] += 1
            else:
                countS[chars] = 1
    
        for chars in t:
            if chars in countT:
                countT[chars] += 1
            else:
                countT[chars] = 1

        return countS == countT



    
    

    


                
            
        
        





