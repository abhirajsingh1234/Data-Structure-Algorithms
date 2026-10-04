class Solution:
    def findMajority(self, arr):
        dict = {}
        for i in arr:
            if i in dict.keys():
                dict[i] = dict[i]+1
            else:
                dict[i] = 1
        return sorted([k for k,v in dict.items() if v>len(arr)//3],reverse = True)
        

obj = Solution()
print(obj.findMajority([2, 2, 3, 1, 3, 2, 1, 1]))