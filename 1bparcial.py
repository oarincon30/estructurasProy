def mergeSort(arr):
    if len(arr) >2:
        ter1 = len(arr)//3 #Finding the mid of the array
        ter2 = 2*ter1
        L = arr[:ter1] # Dividing the array elements
        M = arr[ter1:ter2]
        R = arr[ter2:] # into 2 halves

        mergeSort(L) # Sorting the first half
        mergeSort(M)
        mergeSort(R) # Sorting the second half

        i = n = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and < len(M) and j < len(R):
            if L[i] < M[n] and l[i]<R[j]:
                arr[k] = L[i]
                i+=1
            elif L[i] < M[n] and l[i]<R[j]:
                arr[k] = R[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

# driver code to test the above code
#if __name__ == '__main__':
arr = [12, 11, 13, 5, 6, 7]
print ("Given array is", end="\n")
printList(arr)
mergeSort(arr)
print("Sorted array is: ", end="\n")
printList(arr)
