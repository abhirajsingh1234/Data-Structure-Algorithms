class Solution:
    def rearrange(self,arr):
        # code here
        positive = []
        negative = []
        output_array = []
        
        for  i in arr:
            if i >=0:
                positive.append(i)
            else:
                negative.append(i)
                
        iterations = max(len(positive),len(negative))
        print('positive :',len(positive),'negative :',len(negative))
        for i in range(iterations):
            print('itering :' , i)
            if i<=len(positive)-1:
                output_array.append(positive[i])
            if i<=len(negative)-1:
                output_array.append(negative[i])
        return output_array

obj =Solution()
print(obj.rearrange([9, 4, -2, -1, 5, 0, -5, -3, 2]))