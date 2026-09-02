class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans1 = ""
        ptr = 0

        while True:
            curr = ""

            for w in strs:
                if ptr >= len(w):
                    return ans1
                if curr == "":
                    curr = w[ptr]
                if curr != w[ptr]:
                    return ans1

            ans1 += curr
            ptr += 1