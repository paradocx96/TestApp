
A = []
for x in range (5):
    A.append(int(input("Enter a Number : ")))
print("\nNormal Array")
print(A)

def InsertionSort(A):
    for j in range(len(A)):
        key = A[j]
        print("Key : ", key)
        i = j-1
        print("i 1 : ", i)
        while (i >= 0 and A[i] > key):
            A[i+1] = A[i]
            i = i - 1
            print("i 2 : ", i)
        A[i+1] = key

InsertionSort(A)
print("\nSorted Array")
print(A)
