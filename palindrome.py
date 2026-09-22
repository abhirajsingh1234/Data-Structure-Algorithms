class Solution:
    def isPalindrome(self, s):
        # code here
        length = len(s)
        iterations = int(length/2 if length%2==0 else (length/2)-0.5)
        print(iterations)
        for i in range(iterations):
            if s[i]!=s[length-1-i]:
                print(f"{s[i]}!={s[length-i-1]}")
                return False
        return True
            
        
obj = Solution()
print(obj.isPalindrome('ABBA'))