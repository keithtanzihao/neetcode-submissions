class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        r = {}
        for i in nums:
            if i not in r:
                r[i] = 1
            else:
                r[i] += 1
        print(r)
        fk = 0
        fv = 0
        for k, v in r.items():
            if v > fv:
                fv = v
                fk = k
        
        return fk