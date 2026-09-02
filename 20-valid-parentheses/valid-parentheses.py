class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        l = []

        if len(s)%2 != 0:
            return False

        for c in s:
            if c not in map:
                l.append(c)

            if not l:
                return False

            if c in map:
                if l[-1] == map[c]:
                    l.pop()
                else:
                    return False
        
        if not l:
            return True
        return False
            

                