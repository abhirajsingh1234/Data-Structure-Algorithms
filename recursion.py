class Solution:
    def recursion(self, n):
        if n == 0 :
            return
        print(n)
        self.recursion(n-1)
        print(n)

pobj = Solution()
pobj.recursion(5)
