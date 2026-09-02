class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans1 = ""
        ptr = 0

        while True:
            curr = ""
            match = True
            for w in strs:
                if ptr < len(w):
                    if curr == "":
                        curr = w[ptr]
                    if curr != w[ptr]:
                        match = False
                        return ans1
                else:
                    return ans1
            if match:
                ans1 += curr
            ptr += 1

        return ans2