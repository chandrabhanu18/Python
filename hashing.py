# Hashing
# Contains duplicates
def contains_duplicates(nums):
    seen=set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False
#Finding first unique character 
def first_Unique_character(s):
    freq={}
    for i in s:
        freq[i]=freq.get(i,0)+1
    for i,num in enumerate(s):
        if freq[num]==1:
            return i
    return -1    
    
