class Solution:
	def maxProduct(self, arr):
		# code here
		new_maximum = arr[0]
		new_minimum = arr[0]
		result = arr[0]
		for i in range(1,arr):
			x=arr[i]
			if x<0:
				new_maximum,new_minimum = new_minimum,new_maximum

			 
		
obj =Solution()

print(obj.maxProduct([-2, 6, -3, -10, 0, 2]))