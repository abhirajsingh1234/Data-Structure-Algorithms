class Solution:    
    def findUnion(self, a, b):
        # code here
        data = {}
        for i in a:
            if i in data.keys():
                data[i] = data[i]+1
            else:
                data[i] = 1
        for j in b:
            if j in data:
                data[j] = data[j]+1
            else:
                data[j] = 1
        return {values for values in data.keys()}

obj =  Solution()
print(obj.findUnion([1,1,2,2,3,3],[5,6,7,8,8]))

