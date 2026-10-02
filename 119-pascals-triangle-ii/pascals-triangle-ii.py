class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        fr = [[1]]
        i = 0

        while i <= rowIndex:
            pr = [0] + fr[i] + [0]
            cr = []
            x = 0
            y = 1
            while y < len(pr):
                val = pr[x] + pr[y]
                cr.append(val)
                x+=1
                y+=1
            print(f"i:{i:<5} pr:{str(pr):<20} cr:{str(cr)}")
            fr.append(cr)
            i+=1
        
        return fr[rowIndex]