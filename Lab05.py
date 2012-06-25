#1.a. It won't output anything
def do(thing):
    return str(thing)+str(1)
do(5)

#b.it won't output anything
def do(one, two=5):
    return one+two
do(5)

#c.
def do(a,b):
    a=5
    b=5
    return a*b
inp=8
do(inp,5)
print inp

#d.
def try_to_change_list_contents(the_list):
    the_list.append('four')
outer_list=['one','two','three']
try_to_change_list_contents(outer_list)
print outer_list

#e.
def do(a,f):
    return a*f(a)
def inp(a):
    return a*2
print do(6,inp)

#2.
def factorial(a):
    import math
    return math.factorial(a)
a=int(raw_input('Enter the number\n'))
print "Factorial is", factorial(a)

#3.
import sys
def main():
    print "How many numbers of the sequence would you like?"
    n=int(sys.stdin.readline())
    fib(n)
def fib(n):
    a,b=0,1
    for i in range(0,n):
        print a
        a,b,=b,a+b
main()

#4.
def prime(possible_prime):
    divisor_count=0
    for i in range(1,possible_prime+1):
        if possible_prime%i==0:
            divisor_count+=1
    if divisor_count==2:
        print possible_prime,"is prime"
    else:
        print possible_prime,"is not prime"
possible_prime=int(raw_input('Enter number\n'))
prime(possible_prime)

#challenge.4
string=raw_input('Enter string\n')
def isPalindrome(string):
    index=0
    check=True
    while index<len(string):
        if string[index]==string[-1-index]:
            index+=1
            return True
        return False
if isPalindrome(string)==True:
        print "It is a Palindrome"
else:
        print "it is not a palindrome"                            

#5
a=raw_input('Enter first string\n')
b=raw_input('Enter second string\n')
if b in a:
    print b,"is a subset of", a
