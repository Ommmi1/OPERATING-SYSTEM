#!bin/bash/
import os
import time

pid=os.fork()
array_parent=[4,32,5,4,6,8,6,9,1,2,5,2,3,5]
temp=0

if pid>0:
    time.sleep(10)
    for i in range(len(array_parent)-1,0,-1):
        for j in range(len(array_parent)-1):
            j=i+1
            if(array_parent[i]>array_parent[j]):
                temp=array_parent[i]
                array_parent[i]=array_parent[j]
                array_parent[j]=temp
    print("\n")
print("Parent process  : \n")
for i in range(len(array_parent)-1,0,-1):
    print(array_parent[i])

elif (pid==0):
    print("\n")
    for i in range(len(array_parent)-1,0,-1):
        for j in range(len(array_parent)-1):
            j=i+1
            if(array_parent[i]>array_parent[j]):
                temp=array_parent[i]
                array_parent[i]=array_parent[j]
                array_parent[j]=temp
print("Child process: \n")
for i in range(len(array_parent)-1,0,-1):
    print(arrray_parent[i])
print("\n")

elif:
    print("Process failed")


