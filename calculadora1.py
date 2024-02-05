# Select the operation
Operation = input("Please enter the operation you wish to complete: ")

# Collecting the data
number_one = int(input('Type it the first number: '))
number_two = int(input('Type it the second number: '))

# Condintion for the operation: 

if Operation == "+":
    print("The result is:")
    print(number_one + number_two)

elif Operation == "-":
    print("The result is:")
    print(number_one - number_two)
    
elif Operation == "*":
    print("The result is:")
    print(number_one * number_two)
    
elif Operation == "/":
    print("The result is:")
    print(number_one / number_two)