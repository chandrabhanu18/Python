# kadane's algorithm
def kadane(nums):
    curr_sum=0
    max_sum=0
    for i in range(len(nums)):
        curr_sum=max(nums[i],curr_sum+nums[i])
        max_sum=max(curr_sum,max_sum)
    return max_sum   
a=[-2,-1,-3,-4,-1,-2,-1,-5,-4]
print(kadane(a))
