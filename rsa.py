#!/usr/bin/python

def isPrime(n):
    lst = []
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
            #this checks if i >= the sqrt of n
            if i >= (n ** 0.5):
                break
    if len(lst) > 2 or len(lst) == 1 or lst[1] != n:
        return(0)
    return(1)

def prime_factors(n):
    lst = []
    for i in range(1, n+1):
        if n % i == 0 and isPrime(i):
            lst.append(i)
            #this checks if i >= the sqrt of n
            if i >= (n ** 0.5):
                break
    
    print(f"{n}={lst[1]}*{lst[0]}")


if __name__ == "__main__":
    import sys

    with open(sys.argv[1], "r+") as file1:
        nums = (file1.read().splitlines())
    for i in range(len(nums)):
        num = int(nums[i])

    prime_factors(num)
