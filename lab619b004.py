import os
import time
id=os.fork()
if id<0:
    print("Failed")
if id>0:
    print("parent pid: {0}".format(os.getpid()))
    time.sleep(10)
else:
    #print("parent is about to sleep")
    print("child pid : {0}".format(os.getpid()))
    

#print("Hello Miss from the process {0}\n and parent is {1} ".format(os.getpid(),os.getppid()))


