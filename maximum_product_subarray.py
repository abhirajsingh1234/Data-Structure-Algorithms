class Solution:
	def maxProduct(self, arr):
		# code here
		maximum = arr[0]
		suff_product = 1
		prefix_product = 1
		arr_length = len(arr)
		for i in range(arr_length):
			prefix_product = prefix_product * arr[i]
			suff_product = suff_product * arr[arr_length - 1 - i]
			maximum = max(maximum, prefix_product)
			maximum = max(maximum, suff_product)
			if prefix_product == 0:
				prefix_product = 1
			if suff_product == 0:
				suff_product = 1
		return maximum


			 
		
obj =Solution()

print(obj.maxProduct([-2, 6, -3, -10, 0, 2]))