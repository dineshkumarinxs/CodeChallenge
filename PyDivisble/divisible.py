# Program to check if a given number is divisible from 1 to 10

#Get input from user
num = int(input("Enter the number you like to check: "))

#Function to check if the given number is divisible from 1 to 10
def divisib(num):
    numr = []
    for i in range(1, 11):
        if (num % i == 0):
            numr.append(i)            
    return numr   #Return the output

#Print the output
print("The number",num, "is divisible by following numbers from 1 till 10")
print(divisib(num))