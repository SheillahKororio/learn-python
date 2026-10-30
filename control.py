# a python program that chceks if someone is eligible to vote or no

age=int(input("Enter you age"))
if age >=18:
    print("you are eligible to vote")
else:
    Print("you can vote.. underage")

# create a program that 

# create program that checks between 3 numbers which on is biggest
# Get three numbers from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Compare them
if a >= b and a >= c:
    biggest = a
elif b >= a and b >= c:
    biggest = b
else:
    biggest = c

print(f"The biggest number is: {biggest}")