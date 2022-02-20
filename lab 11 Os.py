"""import os  
os.fork()
r,w = os.pipe() 
pid = os.fork
if pid > 0:  
    os.close(r)     
    print("Parent process is writing")      
    text =b"Hello child process"     
    os.write(w,text)       
else:      
    os.close(w)      
    # Read the text written by parent process      
    print("\nChild Process is reading")     
    r = os.fdopen(r)      
    print("Read text:", r.read()) 

import os
r, w = os.pipe()
r1,w1 = os.pipe()
print(w1,r1)   
pid = os.fork()
if pid > 0:
    os.close(r)
    print("Parent process is writing")
    text =b"Hello child process"
    os.write(w, text)
    os.close(w)
    os.wait()
    os.close(w1)
    print("parent process is reading")
    r=os.fdopen(r1)
    print("Read text:", r.read())
else:
    os.close(w)
# Read the text written by parent process
    print("\nChild Process is reading")
    r = os.fdopen(r)
    print("Read text:", r.read())


    os.close(r1)
    print("Child process is writing")
    text =b"Hello child process"
    os.write(w1, text)
    os.close(w1)

from multiprocessing import Process, Pipe
def f(conn):
    conn.send([30, None, 'hello Students'])
    conn.close()
def f1(conn):
    conn.send([10, None, 'hello parent'])
    conn.close()
if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f1, args=(parent_conn,))
    p1=Process(target=f,args=(child_conn,))
    p.start()
    print(child_conn.recv())
    p.join()
    p1.start()
    print(parent_conn.recv())
    p1.join()

from multiprocessing import Process, Pipe
def f(conn):
    a = [1,2,3,4,5]
    for i in a:
        a = i**2
        print(a)
if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()

import os
r, w = os.pipe()
pid = os.fork()
if pid > 0:
    os.close(r)
    print("Parent process is writing")
    text =input("Enter yout name ")
    roll_sec=b" 19B-004-SE SEC A"
    arr = bytes(text, 'utf-8')
    os.write(w, arr)
    os.write(w, roll_sec)
    concate=arr+roll_sec
    
    os.close(w)

else:
    os.close(w)
    r = os.fdopen(r)
    print("Read text:", r.read())

"""