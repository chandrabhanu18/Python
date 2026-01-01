# /Recursion
# Array Sum
def SumOfArray(i,array):
    if i==len(array):
        return 0;
    return array[i]+SumOfArray(i+1,array)
# String Reversing
def reversing(s):
    if not s:
        return s
    return reversing(s[1:])+s[0]
# Print 1 to n   
def printsFromN(n):
    if n==0:
        return 0;
    print(n)
    printsFromN(n-1)
# Factorial
def fact(n):
    if n==1 or n==0:
        return 1;
    return n*fact(n-1)
# Palindrome
def is_Palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome(s, left + 1, right - 1)
# Reverse
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)
array=[1,2,4]
print(SumOfArray(0,array))
print(reversing("Chandra"))
printsFromN(5)
print(fact(5))
print(is_Palindrome("Chandra",0,len("Chandra")-1))
print(reverse_number(1234))