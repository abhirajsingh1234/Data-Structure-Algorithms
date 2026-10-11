class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        sign = 1
        output = 0
        upper_limit = 2147483647
        lower_limit = -2147483648

        for i in s:
            if i == ' ':
                index+=1
        if s[index]=='-':
            sign = -1
            index+=1
        elif s[index]=='+':
            sign = 1
            index+=1
            

        for i in range(index, len(s)):
            result = ord(s[i]) - ord('0')
            if result>=0 and result<=9:
                output = (output*10)+result
            else:
                break
        output = sign*output
        if output ==0:
            return output
        elif output>=upper_limit:
            return upper_limit
        elif output<=lower_limit:
            return lower_limit
        return output
        
obj = Solution()
print(obj.myAtoi(' 123345563456789f65'))