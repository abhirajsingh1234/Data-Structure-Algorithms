def sum_2_pair(nums,target):
    corpo = {}
    for i,v in enumerate(nums):
        print(corpo)
        x = target-v
        if x in corpo:
            return True
        corpo[v] = i
    return False

print(sum_2_pair([1, -2, 1, 0, 5],0))