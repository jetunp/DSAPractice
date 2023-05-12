#basic syntax for recursion

# def recursion(parameters):
#     if exit from condition satisfied:
#         return some value
#     else:
#         recursion(modified paramaters)

#simple example
def recursion(n):
    if n<1:
        print("n is less than 1")
    else:
        recursion(n-1)
        #print(n)
recursion(32)

#how to write recursion function in 3 steps
#factorial
#step1: Recursive case - the flow
#step2: Base case - the stopping criterion
#step3: unintentional case - the constraint
def factorialRecursive(number):
    assert number>=0 and int(number) == number, "the number must be a positive integer only!"
    if number in [0,1]:
        
        return 1
    else:
        
        return number * factorialRecursive(number-1)
        
print(factorialRecursive(5))  

#factorial using iterative method
def factorialIterative(n):
    assert n>=0 and int(n) == n, "the number must be a positive integer only!"
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
#print(factorialIterative(-5))


#Fibonnacci series using recursion
#step1: Recursive case - the flow
#step2: Base case - the stopping criterion
#step3: unintentional case - the constraint
def fibonnacciRecursive(n):
    assert n>=0 and int(n) == n, "the number must be a positive integer only!"
    # if n==0:
    #     return 0
    # elif n==1:
    #     return 1
    if n in [0,1]:
        return n
    else:
        return fibonnacciRecursive(n-1)+fibonnacciRecursive(n-2)
print(fibonnacciRecursive(200))