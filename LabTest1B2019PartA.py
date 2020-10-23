A = []
for x in range(10):
    A.append(int(input("Enter a number : ")))
print("Inputed array : ", A)


n = len(A)
def INSERTION_SORT(A):
    for j in range(1,n):
        key = A[j]
        i = j - 1

        while(i >= 0 and A[i] < key):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

INSERTION_SORT(A)
print("Sorted Array : ", A)
