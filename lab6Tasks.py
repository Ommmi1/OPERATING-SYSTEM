#!bin/bash/
import os
import time
terminated_child=[]
created_processes=[]
pid=os.fork()

if pid is 0:
    os.fork()
    os.fork()
    created_processes.append(os.getpid())
       # print("child has been terminated",os.wait())
        #terminated_child.append(os.getpid())
else:
    print("not running")
    print("Child processes are :",created_processes)
