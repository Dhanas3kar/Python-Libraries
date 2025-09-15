import numpy as np

arr=np.array([[[1, 2, 3], [4, 5,6], [7, 8, 9]]])
print("Given array:", arr)

print("Positive Indexing:")
for i in range(len(arr)):
    print(f"Element at index {i} is {arr[i]}")
    
print("Negative Indexing:")
for i in range(1, len(arr)+1):
    print(f"Element at index {-i} is {arr[-i]}")
    

arr2=np.array([1,2,3,4,5,6,7,8,9])
mask=arr2>3
print("Boolean Indexing:", arr2[mask])