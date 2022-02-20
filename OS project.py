#---------------------------task 1-------------------------
from multiprocessing import Process, Value, Array
import time
start1=time.time()
def f1(n,a1,a2,arr3):
    n=5500
    for j in range(n):
        a1[j]=j**2
        arr3[j]=j**2
    # print(a1[:])
    for i in range(n,len(a2)):
        a2[i]=i**2
        arr3[i]=i**2
    # print(a2[:])    
    print(arr3[:])
if __name__=='__main__':
    num=Value('i',5500)
    arr1=Array('i',range(1,11000))
    # print(arr1[:])
    arr2=Array('i',11000)
    # print(arr2[:])
    arr3=Array('i',11000)
    # print(arr3[:])
    p1=Process(target=f1,args=(num,arr1,arr2,arr3))
    p1.start()
print(time.time()-start1)


#single processing )))
import time
arr=[]
arr2=[]
start=time.time()
for i in range(1,11000):
    i=i**2
    arr.append(i)
print(arr)
for j in range(11000):
    j=j**2
    arr2.append(j)
print(arr2)
print(time.time()-start)


# -----------------------task 2------------------
import time
from multiprocessing import Pool
start=time.time()
def square(x):
    square = x * x
    print("start process")
    return square


if __name__ == "__main__":
    # In the Process class, we had to create processes explicitly. 
    # However, the Pool class is more convenient, 
    # and you do not have to manage it manually. 
    # The syntax to create a pool object is multiprocessing.Pool(processes, initializer, initargs, maxtasksperchild, context).
    # All the arguments are optional. 
    # processes represent the number of worker processes you want to create. 
    # The default value is obtained by os.cpu_count(). 
    # The second initializer argument is a function used for initialization, 
    # and the initargs are the arguments passed to it. 
    # maxtasksperchild represents the number of tasks assigned to each child process.
    # After that number of tasks, the process will get replaced by a new worker process. 
    # The advantage of specifying this is that any unused resources will be released. 
    # If not provided any, 
    # the processes will exist as long as the pool does.
    pool = Pool()
    # While the pool.map() method blocks the main program until the result is ready, 
    # the pool.map_async() method does not block, and it returns a result object. 
    # The syntax is pool.map_async(function, iterable, chunksize, callback, error_callback). 
    # The arguments, callback. and error_callback are optional.
                            #calling function
    result = pool.map_async(square, range(10000))
    print("main script")
    print(result.get())
    print("end main script")
print(time.time()-start)



#As you can see in the output above, 
# the map_async() method does not block the main script. 
# The result.get() method is used to obtain the return value of the square() method.
#  Note that result.get() holds up the main program until the result is ready. 
# It also takes a timeout argument, which means that it will wait for timeout seconds for the result.
#  If the result does not arrive by that time, a timeout error is thrown.

# -------------------------task 3--------------------------------
# this problem is from internet resource because this problem or algorithm is hard to implement 
# so we understand the functionality of code and run thsi task as it is providing us our results.
import numpy as np
# numpy is used for matrices multiplication
from timeit import timeit
from multiprocessing import Pool

def fib(dummy):
    n = [1,1]
    for ii in range(100000):
        n.append(n[-1]+n[-2])

def silly_mult(matrix):
    for row in matrix:
        for val in row:
            val * val

if __name__ == '__main__':
# lambda is an anonymous funtion
# A lambda function is a small anonymous function. A lambda function can take any number of arguments,
# but can only have one expression. Multiply argument a with argument b and return the result
    dt = timeit(lambda: map(fib, range(10)), number=10)
    # This module provides a simple way to time small bits of Python code. 
    # It has both a Command-Line Interface as well as a callable one. 
    # It avoids a number of common traps for measuring execution times. 
    print( "Fibonacci, non-parallel: %.5f" %dt)

    matrices = [np.random.randn(1000,1000) for ii in range(10)]
    dt = timeit(lambda: map(silly_mult, matrices), number=10)
    print( "Silly matrix multiplication, non-parallel: %.5f" %dt)
    # if we use 8 processes or more the time is much higher in this case 
    # or if we use 4 processes this will give ideal timw to execute in parallel
    pool = Pool(4)
    dt = timeit(lambda: pool.map(fib,range(10)), number=10)
    print( "Fibonacci, parallel: %.3f" %dt)

    dt = timeit(lambda: pool.map(silly_mult, matrices), number=10)
    print( "Silly matrix multiplication, parallel: %.3f" %dt)
    # the pool library assigns the task to the given processors
    # AS we know that the processes are running parallely so therefor the pool 
    # library has to save the task information which results in extra overhead 
    # this overhead can beome the reason for slowing down the task while in serail 
    # processing  there is no overhead because the task are not divided.it is very 
    # difficult to find optimal condition where the number of proesses and the 
    # overhead combine together result in a time lesses than serial computing as 
    # increasing the proecees results in a greater overhead while edecreasing the 
    # processes results in a greater completion time of the task however the 
    # overhead in this siatuation is less .

#-------------------------------------------task 4-------------------------------

#parallel code
import time
from multiprocessing import Process,freeze_support,Array
start=time.time()
def calc_square(numbers):
    for n in numbers:
        print('square ' + str(n*n))
 
def calc_cube(numbers):
    for n in numbers:
        print('cube '+ str(n*n*n))
if __name__ == '__main__':
    #this line is called because python interpreter throughs an error 
    #if this line is not added this is because the old version of python
    freeze_support()
    #freeze support : The "freeze_support()" line can be omitted if the program
        # is not going to be frozen to produce an executable.
    arr=Array('i',range(100000))
    p1=Process(target=calc_square,args=(arr,))
    p2=Process(target=calc_cube,args=(arr,))
    p1.start()
    p2.start()
    p2.join()
    p1.join()
print(time.time()-start)
print("Done")
    
#serial code works faster 
#serial squaring
import time
arr=[]
arr1=[]
start=time.time()
for i in range(100000):
    i=i**2
    arr.append(i)
for j in range(100000):
    j=j**3
    arr1.append(j)
print(arr)
print(arr1)
print(time.time()-start)