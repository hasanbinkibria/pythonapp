from functions import function1
from clases import user
result = function1(34)

print(f"Hello {result}")
inputusername = input("Enter Your Name : ")
inputage = int(input("Enter Your Age : "))
person = user(f"{inputusername}",f"{inputage}")

print(f"Your name is",person.name)
print(f"Your age is",person.age)