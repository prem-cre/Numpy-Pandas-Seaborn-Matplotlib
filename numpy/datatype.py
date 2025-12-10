import  numpy as np
var1 = np.array([1,2,334,5,5,66,])
print(var1.dtype)

var1 = np.array([1,2,3,1.7])
print(var1.dtype)

var1 = np.array(['harr','typ','prem'])
print(var1.dtype)

var1 = np.array(['A','S'])
print(var1.dtype)

var1 = np.array(['A','D',1,2,3])
print(var1.dtype)

x = np.array([1,2,3,4],dtype='f')
print(x.dtype)
print(x)

x1 = np.array([1,2,3,4],dtype=np.int8)
print(x1.dtype)
print(x1)

x2 = np.array([1,2,3,4])
new = np.float32(x2)
print(new.dtype)
print(x2.dtype)
print(x2)
print(new)

x3 = np.array([1,2,3,4])
new1 = x3.astype(float)
print(x3)
print(new1)