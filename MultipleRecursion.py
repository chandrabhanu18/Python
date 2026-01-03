# Multiple recursions
def fibonacci(n):
    if n<=1:
        return n
    previous,current=0,1
    for i in range(n):
        print(previous)
        previous,current=current,previous+current
    
n=int(input("Enter the value of n : "))
print(fibonacci(n))
