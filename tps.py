#  TWO POINTERS PRACTICE 


# Two numbers add upto target
def Sum_Target(target,nums):
    i,j=0,len(nums)-1
    nums.sort()
    while i<j:
        if nums[i]+nums[j]==target:
            return [nums[i],nums[j]]
        elif nums[i]+nums[j]<target:
            i+=1
        elif nums[i]+nums[j]>target:
            j-=1
# remove duplicates in place like [1,1,2,3,3,4]=[1,2,3,4]
def remove_duplicates(a):
    if not a:
        return 0
    write=0
    for read in range(1,len(a)):
        if a[write]!=a[read]:
            write+=1
            a[write]=a[read]
    return write+1,a
# Checking an array is a palindrome or not
def is_palindrome(a):
    l,r=0,len(a)-1
    while l<r:
        if a[l]!=a[r]:
            return False
        l+=1
        r-=1
    return True    
n=[1,2,3,4,5,6]
t=9
print(Sum_Target(t,n))
n=[1,1,2,3,3,4,5,5]
value,array=remove_duplicates(n)
print(value)
print(array[:value])
arr=[1,2,3,7,2,1]
print(is_palindrome(arr))
