import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])

slice=arr[2:5]
print("1D Sliced array:", slice)

arr2=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
slice2=arr2[0:2, 1:3]
print("2D Sliced array:", slice2)

arr3=np.array([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]])
slice3=arr3[1:3, 0:2, 1]    
print("3D Sliced array:", slice3)

arr4=np.array([1,2,3,4,5,6,7,8,9])
step_slice=arr4[1:8:2]
print("1D Step Sliced array:", step_slice)

arr5=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
step_slice2=arr5[0:3:1, 0:5:2]
print("2D Step Sliced array:", step_slice2) 

arr6=np.array([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]])
step_slice3=arr6[0:3:1, 0:2:1, 0:2:1]
print("3D Step Sliced array:", step_slice3)