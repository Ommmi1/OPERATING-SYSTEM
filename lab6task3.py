#!bin/bash/

import os 
import time
pid=os.fork()
"""
parent=[3,2,5,3,1,35,7,8]
if pid>0:
    os.wait()
    print("child process")
    for i in range(len(parent)-1):
        for j in range(0,len(parent)-i-1):
            if parent[j]>parent[j+1]:
                parent[j],parent[j+1]=parent[j+1],parent[j]

time.sleep(10)
print("Sorted array is: ")
for i in range(len(parent)):
    print("% d" % parent[i])"""


#task2
parent=[]
if pid is 0:
    parent.append(os.getpid())
    
    c2=os.fork()
    if c2 is 0:
        parent.append(os.getpid())
        
        c3=os.fork()
        if c3 is 0:
            parent.append(os.getpid())
            print(parent)
        else:
            os.wait()
    else:
        os.wait()
else:
    os.wait()
