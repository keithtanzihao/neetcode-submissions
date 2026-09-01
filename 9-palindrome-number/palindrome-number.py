class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = list(str(x))
        c = len(l)-1
        
        m = len(l) % 2
        h = len(l) // 2

        for i in range(0, h):
            v1 = l[i]
            v2 = l[c-i]
            if v1 != v2:
                return False
        return True
            
            
            
