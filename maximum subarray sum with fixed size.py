# Sliding windows
# Maximum subarray of window size k 
def maximum_sum(a,k):
    window_sum=sum(a[:k])
    maxi_sum=window_sum
    for i in range(k,len(a)):
        window_sum+=a[i]
        window_sum-=a[i-k]
        maxi_sum=max(window_sum,maxi_sum)
    return maxi_sum
 
a=[2,3,5,6,7,4,1]
n=3
print("maximum subarray sum is : ",maximum_sum(a,n))
