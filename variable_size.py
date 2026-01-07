# Sliding Window 
# Variable size but not fixed 
def longest_subarray(a,k):
    left=0
    current_sum=0
    max_length=0
    for right in range(len(a)):
        current_sum+=a[right]
        while(current_sum>k):
            current_sum-=a[left]
            left+=1
        max_length=max(max_length,right-left+1)    
    return max_length

# Longest substring without repeating characters
def longest_substring(s):
    left=0
    max_length=0
    current_length=0
    seen=set()
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])
        max_length=max(max_length,right-left+1)
    return max_length
    
# Maximum average subarray
def max_sub_array(nums,k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i]        # add right
        window_sum -= nums[i - k]    # remove left
        max_sum = max(max_sum, window_sum)

    return max_sum / float(k)  
b=[1,12,-5,-6,50,3]
k=4
print(max_sub_array(b,4))
a=[1,-1,3,4,6,5]
k=15
s="abcabcdab"
print(longest_substring(s))
print(longest_subarray(a,k))
