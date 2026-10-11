class Solution:
    def multiplyStrings(self, s1, s2):
        # code here
        if len(s1)==0 or len(s2) == 0:
            return None
        
        s1_sign = 1
        s1_index = 0
        s1_int = 0
        if s1[0] =='+':
            pass
            s1_index+=1
        elif s1[0]=='-':
            s1_sign = -1
            s1_index+=1
        s2_sign = 1
        s2_index = 0
        s2_int = 0
        if s2[0] =='+':
            pass
            s2_index+=1
        elif s2[0]=='-':
            s2_sign = -1
            s2_index+=1

        for i in range(s1_index,len(s1)):
            result = ord(s1[i])-ord('0')
            if result>=0 and result<=9:
                s1_int = (s1_int*10) + result
            else:
                break
        for i in range(s2_index,len(s2)):
            result = ord(s2[i])-ord('0')
            if result>=0 and result<=9:
                s2_int = (s2_int*10) + result
            else:
                break
        return (s1_sign*s1_int)*(s2_sign*s2_int)
        
        
obj = Solution()
print(obj.multiplyStrings('-12','12'))