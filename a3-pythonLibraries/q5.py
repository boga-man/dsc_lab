from random import random
import numpy as np

# get number of elements from the user
n = int(input("Enter the number of elements in the list: "))

a = np.random.randint(1,10,size=(1,n))
b = np.random.randint(1,10,size=(1,n))

# print the lists a and b
print("Randomly generated lists")
print("List a: ", a)
print("List b: ", b)

indices = []

for i in range(n):
    if(a[0][i] > b[0][i]):
        indices.append(i);

# print indices
print("5a)")
print("Indices of elements in list a greater than list b: ", indices)
print("--------------------------------------------------------------------------------");

# create a numpy array of random numbers
arr = np.random.randint(1,10,size=(1,n))

print("5b)");
# replace all the even elements with zero
arr[arr%2==0] = 0
# print the array
print("\n(i) Array after replacing all even elements with zero: ", arr)
# extract all the prime numbers from the array
primes = []
for i in arr[0]:
    isPrime = 1
    entered = 0
    if(i>=2):
        entered = 1
        for j in range(2,i):
            if(i%j==0):
                isPrime = 0
                break
    if(isPrime==1 and entered==1):
        # insert i into the set primes
        primes.append(i);

#print the prime numbers
print("\n(ii) Prime numbers in the array: ", primes)

# Convert the 1D array to a 2D array in 2 rows Input
dim2 = n//2
newarr = arr.reshape(2,dim2);
# print the array
print("\n(iii) 2D array: ", newarr)

# Display the array element indices such that array elements are sorted in ascending order [ without the changing the position of elements]
sortedIndices = np.argsort(arr)
#print the sorted indices
print("\n(iv) Sorted indices: ", sortedIndices)

# Create a numpy array containing 0s and 1s
arr = np.random.randint(0,2,size=(1,n))
# convert the array to boolean
# type of the array before conversion
print("\n(v) Type of the array before conversion: ", type(arr))
boolarr = np.array(arr, dtype=bool)
# type of the array after conversion
print("Type of the array after conversion: ", type(boolarr))


# create a numpy array of 10 elements from user input
print("\n(vi) Splitting the array: ")
arr = np.random.randint(1,10,size=(1,10))
for i in range(len(arr[0])):
    print("Enter element", i+1, ": ")
    arr[0][i] = int(input())

a1 = arr[0][0:2]
a2 = arr[0][2:4]
a3 = arr[0][4:]

# print the arrays
print("Array 1: ", a1)
print("Array 2: ", a2)
print("Array 3: ", a3)
