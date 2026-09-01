class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = list(str(x))
        c = len(l)-1

        m = len(l) % 2
        h = len(l) // 2

        for i in range(0, len(l)):
            v1 = l[i]
            v2 = l[c-i]

            if m == 1 and i == h and c-i == h:
                return l[i] == l[c-i]
            if m == 0 and i == h-1 and c-i == h:
                return l[i] == l[c-i]
            if v1 != v2:
                return False
            
            
            
            
