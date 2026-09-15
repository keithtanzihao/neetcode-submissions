class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        pt = len(digits)-1
        
        while pt >= 0:
            val = digits[pt] + 1
            if val > 9 and pt == 0:
                digits[pt] = 0
                digits.insert(0, 1)
                break
            elif val > 9:
                digits[pt] = 0
            else:
                digits[pt] += 1
                break
            pt -=1
        return digits
            
            

