def greet():
    print("This is my first function")
greet()

# function with parameters
def student(name,age,course):
    print(f"Student name is {name}")
    print(f"Studet age is {age}")
    print(f"Student course is {course}")
student("Erick",30,"Reactjs")
student("Mercy",10,"Reactjs")
student("Sheila",30,"ICT")
student("Jane",15,"Computer Science")

# function with return keyword
def add_number(a,b):
    return a+b
result=add_number(6,26)
print(f"sum :{result}")

# function to return product
def product_number(a,b,c):
    return a*b*c
result=product_number(6,26,10)
print(f"product :{result}")