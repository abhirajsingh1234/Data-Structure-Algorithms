# def h(key, m):
#     return key % m


# print(h(33,10))
# print(h(333,10))
# print(h(3336,10))
# print(h(33334,10))

#---------------------------------------------------------------------

# import math
# def h(key, m):
#     A = (math.sqrt(5) - 1) / 2      # ~0.618, golden ratio constant
#     return int(m * ((key * A) % 1))

# for i in range(100):
#     print(f'{h(i,10)} : {i}')

#----------------------------------------------------------------------

def two_sum(nums, target):
    seen = {}  
                       # value → index
    for i, x in enumerate(nums):
        print(f"Dictionary 'seen': {seen}")
        need = target - x
        print(f"Current number: {x}, Needed number to reach target {target}: {need}")
        print(f"Checking if needed number {need} is in 'seen' dictionary...")
        
        if need in seen:
            print(f"Found! {need} is in 'seen' at index {seen[need]}. Returning indices [{seen[need]}, {i}]")
            return [seen[need], i]
        print(f"{need} not found in 'seen'. Adding {x} to 'seen' with index {i}.")
        seen[x] = i
        print('-'*50)
print(two_sum([2,4,6,-9,3,-1,-4],-1))