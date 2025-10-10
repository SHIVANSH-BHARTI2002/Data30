import numpy as np
# task 1
arr = np.arange(9).reshape(3,3)
print(arr)

#task 2
randArr = np.random.normal(0,10,100)
print("Mean= ",np.mean(randArr))
print("Standard Deviation= ",np.std(randArr))
