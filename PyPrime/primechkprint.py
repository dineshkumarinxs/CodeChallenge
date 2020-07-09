# Prime Number - A prime number is a whole number greater than 1 whose only factors are 1 and itself
# Program to find a whether a given number is Prime or NOT
# Also print all the print numbers till N if it is a prime number

num = int(input("Enter the number to check: "))
numr = []


#Function to check if a number is prime
def isPrime(num):
    # Corner case
    if (num <= 1):
        return False

    # Check from 2 to n-1
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

#Function to Print all prime numbers till N
def printPrime(num):
    count = 0
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            if (i % j == 0):
                count += 1
        if (count == 2):
            numr.append(i)
        count = 0


# Driver Program to print result
if isPrime(num):
    print("The given number", num, "is a prime number")
    printPrime(num)
    print("The prime numbers till", num, "are :", numr)
else:
    print("The given number", num, "is not a prime number")



