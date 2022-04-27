# function to implement bubble sort on a list
def bubbleSort(list):
    n = len(list);
    for i in range(n):
        # Traverse through all array elements
        for j in range(0,n-i-1):
            # Swap if the element found is greater
            if(list[j]>list[j+1]):
                list[j], list[j+1] = list[j+1], list[j];
        # printing the list at every pass
        print("Pass",i+1,":", list);


# taking input from the user
n = int(input("Enter the number of elements in the list: "));
list = [];
# taking the list from the user 
for i in range(n):
    list.append(int(input("Enter element " + str(i+1) + ": ")));
print("The list before sorting: ", list);
print("Initiating bubble sort...");
# calling the function
bubbleSort(list);
print("The list after sorting: ", list);