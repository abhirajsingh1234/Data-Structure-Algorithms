class Solution:
    def find3Numbers(self, arr):
        # code here
        n1 = None
        n2= None
        n1_counter = {'1':{}}
        n2_counter = 0
        for i in range(len(arr)):
            n3=arr[i]
            if n1 is None or n3<=n1:
                n1_counter['1'][i] = n3

                n1=n3
            elif n2 is None or n3<=n2:
                n2_counter =i
                n2=n3
            else:
                for k,v in n1_counter['1'].items():
                    print(f"{k}>{n2_counter}")
                    if k>n2_counter:
                        break
                    n1 = v
                print(n1_counter['1'].items())
                return [n1,n2,n3]
            
        return []

obj = Solution()
print(obj.find3Numbers([12, 11, 10, 5, 6, 2, 30]))