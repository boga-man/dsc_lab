# function to perform recursive binary search
def binary_search(arr, l, r, x):
    # check if the array is empty
    if r >= l:
        # performing integer division
        mid = l + (r - l) // 2
        # check if the mid element is equal to x
        if arr[mid] == x:
            return mid
        # if the mid element is greater than x, perform search in the left half
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        # if the mid element is less than x, perform search in the right half
        else:
            return binary_search(arr, mid + 1, r, x)
    # if the array is empty, return -1
    return -1

# function to perform binary search
def binary_search_itr(arr, x):
    # initialize left and right indices
    l = 0
    r = len(arr) - 1
    # loop till left index is less than right index
    while l <= r:
        # performing integer division
        mid = l + (r - l) // 2
        # check if the mid element is equal to x
        if arr[mid] == x:
            return mid
        # if the mid element is greater than x, perform search in the left half
        elif arr[mid] > x:
            r = mid - 1
        # if the mid element is less than x, perform search in the right half
        else:
            l = mid + 1
    # if the element is not found, return -1
    return -1

list = []
# length of the list from user
n = int(input("Enter the number of elements in the list: "))
# taking the list from the user
for i in range(n):
    list.append(int(input("Enter element " + str(i+1) + ": ")));
# sort the list
list.sort()
# print the list
print("The sorted list is: ", list);



# search for an element in the list
x = int(input("Enter the element to be searched: "))
# calling the recursive function
result = binary_search(list, 0, len(list) - 1, x)
# check if the element is found
if result != -1:
    print("Element found")
else:
    print("Element not found")


# calling the iterative function
result = binary_search_itr(list, x)
# check if the element is found
if result != -1:
    print("Element found")
else:
    print("Element not found")
