class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans1 = ""
        ans2 = ""
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
                print(count, w, curr)
            if match:
                ans1 += curr

            ptr += 1
            print(ans1)
            print("\n")
        return ans2