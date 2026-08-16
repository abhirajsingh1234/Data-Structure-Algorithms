class Solution:
    def pattern8(self, n):

        for i in range(1,n+1):
            space = n -i
            stars = 2*i - 1
            print(" " * space + "*" * stars)
        
        for i in range(0,n):
            space = n - (n-i)
            stars = 2*(n-i) - 1
            print(" " * space + "*" * stars)

        

obj = Solution()
obj.pattern8(5)