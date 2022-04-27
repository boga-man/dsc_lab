
print("-----------------------------------------------------")
print("Name: Venkata Sai Manoj Boganadham")
print("Roll no: 197121")
print("Section: A")
print("-----------------------------------------------------")

# Function to check if three numbers for a pythagorean triplet
def pythagTriplet(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    elif a**2 + c**2 == b**2:
        return True
    elif b**2 + c**2 == a**2:
        return True
    else:
        return False

# Take input of three numbers from user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Check if the three numbers are pythagorean triplet
if pythagTriplet(a,b,c) == True:
    print("The three numbers can form a pythagorean triplet")
else:
    print("The three numbers cannot form a pythagorean triplet")
