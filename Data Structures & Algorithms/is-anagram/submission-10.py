class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for chars in s:
            if chars in count:
                count[chars] += 1
            else:
                count[chars] = 1
        for chars in t:
            if chars not in count or count[chars] == 0:
                return False
            count[chars] -= 1

        return True

                
            
        
        





