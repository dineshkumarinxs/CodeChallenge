Prime Numbers - Week 1 Challenge

A prime number is a number that is only divisible by 1 and by itself. This means that for each of the numbers from 2 to that number, the number cannot be divided without a remainder.

For example, 9 is not a prime number because it can be divided by 3 without a remainder. But 7 is a prime number because it cannot be divided by 2, 3, 4, 5, or 6 without a remainder. For further explanation, click here (Links to an external site.).
Write an application that will show the number and indicate whether or not it is prime. There are two ways that you can achieve this.

This solution can be addressed in many programming languages, we have used Python here with two methods.

Method 1: The user will have to input a number, and you will display that number. You will check if that number is prime and indicate that to the user.
For example, if the user typed 10, it would display the following output: 10 is not a prime number

Method 2: Generate all the prime numbers till N given by the user.

How to run the program?

1. Open command prompt and navigate to the 

C:\workspace\Primepy>python primechkprint.py

2. The Program will execute and prompt user to enter a number, once the number is entered the results will be published as shown below

Enter the number to check: 11
The given number 11 is a prime number
The prime numbers till 11 are : [2, 3, 5, 7, 11]

3. To run the unit test case program run the below command

C:\workspace\Primepy>python -m unittest test_primechkprint.py

The output will be displayed as shown below

Enter the number to check: 5
The given number 5 is a prime number
The prime numbers till 5 are : [2, 3, 5]
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK

The two dots (..) indicated the number of scenarios executed. Since all cases passed the result will printed as OK. 
If any errors the corresponding failed cases will be mentioned with line number