import random

print("-----------------------------------------------------")
print("Name: Venkata Sai Manoj Boganadham")
print("Roll no: 197121")
print("Section: A")
print("-----------------------------------------------------")


# Function to tell if the number is multiple of 12 or not
def multOf12(num):
    if num % 12 == 0:
        return True
    else:
        return False


# Counter to keep track of the number of multiples of 12
cnt = 0

# List to store the generated numbers
numsList = []

# List to store the multiples of 12
multsOf12 = []

# Create 100 random numbers between 1 and 100 and check if they are multiple of 12
for i in range(0,100):
    num = random.randint(0,100)
    numsList.append(num)
    if multOf12(num) == True and num != 0:
        multsOf12.append(num)
        cnt += 1

# Print the numbers generated
print("The numbers generated are: ")
print(numsList)
print("-----------------------------------------------------")

# Print the numbers that are multiple of 12 among the generated numbers
print("The numbers that are multiple of 12 are: ")
print(multsOf12)
print("-----------------------------------------------------")


# Print the count of multiples of 12
print("The number of multiples of 12 is: ", cnt)
print("-----------------------------------------------------")
