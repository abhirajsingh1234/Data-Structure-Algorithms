class Solution:
    def isSubset(self, a, b):
        counter = {}
        for i in a:
            if i in counter.keys():
                counter[i] = counter[i]+1
            else:
                counter[i] = 1
        for i in b:
            print(f"Counter : {counter}")
            if i in counter:
                print(f"{i} in {counter}")
                if counter[i]<=0:
                    return False
                else:
                    counter[i]-=1
                    print(f"dictionary update to {counter}")
            else:
                return False
        return True
obj = Solution()
print(obj.isSubset([11, 7, 1, 13, 21, 3, 7, 3], [11, 3, 7, 1, 7]))