class Solution:    
    def findUnion(self, a, b):
        # code here
        data = {}
        for i in a:
            data[i] = 1

        for j in b:
            if j in data:
                data[j] = data[j]+1
            else:
                pass
        return {values for values in data.keys()if data[values]>1}

obj =  Solution()
print(obj.findUnion([1,1,8,2,2,3,3],[5,6,7,8,8]))