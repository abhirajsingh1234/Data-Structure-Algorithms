'''
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
'''

'''
class Solution:
    def pattern10(self, n):
        for i in range(1, n + n):

            if i>n:
                print("*" * abs(n-abs(n-i)))
            else:
                print("*" * i)

obj = Solution()
obj.pattern10(5)
'''

'''
class Solution:
    def pattern11(self, n):
        val = '0'
        for i in range(1,n+1):
            for j in range(i):
                print(val, end = "")
                val = '0' if val=='1' else '1'
            print()



obj = Solution()
obj.pattern11(5)
'''


