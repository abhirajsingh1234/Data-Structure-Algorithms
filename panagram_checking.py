class Solution:
    def checkPangram(self,s):
        #code here
        total_chars = 'qwertyuioplkjhgfdsazxcvbnm'
        s= s.lower()
        if len(total_chars)>len(s):
            return False
        for c in total_chars:
            if c not in s:
                print(c,' not in  ',s)
                return False
            else:
                pass
        return True
                
obj = Solution()
print(obj.checkPangram('Bawds jog, flick quartz, vex nymph'))