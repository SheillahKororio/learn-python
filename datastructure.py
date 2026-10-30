# list datastructure
# changeable/mutable
# ordered, indexes

myproducts=["Bread,","Milk","Sugar","Blueband"]

print(myproducts)
myproducts.pop()
myproducts[1]="honey"
print("I like drinking tea that has {myproducts[1]}")
print(myproducts)

# Tuple datastructures
countries=("Kenya","Tanzania","Burundi","Somalia")
# countries[0]="USA"
print(countries)

# set datastructures
# avoid duplicates
# non orders
computers={"hp","del","lenovo"}
print(computers)

# dictinary datastructure

customer={
    "name":"Erick",
    "Age":30,
    "City":"Nairobi",
    "Salary":3000,
    "proffesion":"Software Engineer",
}
print(f"customer name : {customer["name"]}")

myfruits=["mangoes","oranges","pineapple","watermelon","ovacado"]

for m in myfruits:
    print(f"I have {m}")
# imagine you are building as
#  school system that calculates the average marks

marks=[65,89,64,89,90]
totAL=0
for x in marks:
    total=total+x
average=total / len(marks)
print(f"Total marks: {total}")
print(f"average marks: {average}")
