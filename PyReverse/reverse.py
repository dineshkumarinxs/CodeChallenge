# Get the number from user manually 
num = int(input("Enter your number to reverse: "))
 
def reverse_num(num):
    if num >= 0:
    
    # Initiate value to null
        test_num = 0

    # Check using while loop
        while(num>0):
    #Logic
            remainder = num % 10
            test_num = (test_num * 10) + remainder
            num = num//10
        return test_num
    else:
        return "Invalid number"
    
print ("The reverse number is :", reverse_num(num))