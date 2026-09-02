class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        l = ""

        if len(s)%2 != 0:
            return False

        for c in s:
            if c not in map:
                l += c

            if not l:
                return False

            if c in map:
                if l[-1] == map[c]:
                    l = l[:-1]
                else:
                    return False
        
        if not l:
            return True
        return False
            

                