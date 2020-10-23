A = []
for v in range(10):
    A.append(int(input("Enter a number between 10 to 20 : ")))
    
print("Original Array : ", A)
print("Length of Array : ", len(A))

#insertion Sort
def insertionSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while (i >= 0 and A[i] > key):
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

#Call the funtion
insertionSort(A)
print("Sorted Array : ", A)
