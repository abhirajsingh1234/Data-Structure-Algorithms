import datetime 
class Solution:
    def whileLoop(self, d : int) -> int:
        # Your code goes here
        start_time = datetime.datetime.now()
        end = 50
        start = 1
        sum = 0
        multiplyier=1
        while(multiplyier>0):
            if start<=end and  str(multiplyier).endswith(str(d)):
                sum=  sum+multiplyier
                multiplyier+=1
                start+=1
            else :
                multiplyier+=1
            if start>end:
                break
        end_time = datetime.datetime.now()
        print("Time taken to execute the while loop: ", end_time - start_time)
        return sum
rum =Solution()
print(rum.whileLoop(9))



class Solution:
    def whileLoop(self, d: int) -> int:
        start_time = datetime.datetime.now()
        
        # Determine the first number ending in d
        multiplyier = 10 if d == 0 else d
        
        total_sum = 0
        count = 0
        
        # Jump directly by 10 every iteration
        while count < 50:
            total_sum += multiplyier
            multiplyier += 10  # ✅ Correct step: 5, 15, 25, 35...
            count += 1
            
        end_time = datetime.datetime.now()
        print("Time taken to execute the while loop: ", end_time - start_time)
        return total_sum

rum = Solution()
print(rum.whileLoop(9))