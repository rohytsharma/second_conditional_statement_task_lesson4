#Check whether the user input number is even or odd and display it to user.

x=int(input("Enter any number: "))

if x % 2 ==0:
    print(f"the number {x} is even")
else:
    print(f"the number {x} is odd")