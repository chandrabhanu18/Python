# Move seroes to end
def move(a):
    ind=0
    for i in range(len(a)):
        if(a[i]!=0):
            a[i],a[ind]=a[ind],a[i]
            ind+=1
    return a   
#Find largest & second largest element
def finding(a):
    first=second=float('-inf')
    for i in a:
        if i>first:
            second=first
            first=i
        elif i>second and i!=first:
            second=i
    return first,second   
# Checking array is sorted or not
def isSorted(a):
    for i in range(1,len(a)-1):
        if a[i]<a[i-1]:
            return False
    return True        
def rotateByOne(a):
    last=a[-1]
    for i in range(len(a)-1,0,-1):
        a[i]=a[i-1]
    a[0]=last
    return a
a=list(map(int,input().split()))
print(move(a))
f,s=finding(a)
print("Largest element is : ",f)
print("Second largest element is: ",s)
if(isSorted(a)):
    print("Yes Sorted!")
else:
    print("Not Sorted")
print(rotateByOne(a))    
