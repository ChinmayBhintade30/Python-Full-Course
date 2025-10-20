#print the given number is prime or not with the help of any loop

n = int(input("Enter the number: "))
#As we know that the number divisible by 1 and itself is a prime number , otherwise not 


# including 1 will create an error of division

#so assume 1 and start with 2 


for i in range(2,n):
    if(n%i == 0):
        print("The number is not prime number")
        break
else:
    print("The number is prime")
    

"""
Enter the number: 5
The number is prime


Enter the number: 6
The number is not prime number

"""


 

#we didnt used else: after the if block in for loop because , until the iteration 2, 3, 4 it is not divisible by 5 so it will
#execute the else block for 3 times , and when it comes to 5, it will not deu to last digit 

#we use else block after the for loop , outside - so that it prints the prime number statement only once



#why break statement is used - because if any number between 2 and n is divisible by the number it is not a prime number at all
#so why to waste the time to iterate the rest of the numbers
