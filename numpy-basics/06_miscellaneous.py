## Load Data from File 
import numpy as np

filedata = np.genfromtxt('data.txt', delimiter=',')
print(filedata)
print(filedata.astype('int32'))



## Boolean Masking and Advanced Indexing
a = filedata > 50
print(a)

print(filedata[filedata > 50])

print(np.any(filedata > 50, axis=0))
print(np.all(filedata > 50, axis=0))
print((filedata > 5) & (filedata < 100))
print(~((filedata > 5) & (filedata < 100))) # ~ is not, output is reverse of above line