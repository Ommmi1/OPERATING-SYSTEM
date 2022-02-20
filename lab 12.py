# from multiprocessing import Process, Value, Array
# def f(n, a):
#     n.value = 3.1415927
#     for i in range(len(a)):
#         a[i] = -a[i]

# if __name__ == '__main__':
#     num = Value('d', 0.0)
#     arr = Array('i', range(10))

#     p = Process(target=f, args=(num, arr))
#     p.start()
#     p.join()

#     print(num.value)
#     print(arr[:])
    
from ast import arg
from multiprocessing import Process, Value,Array
import os
array=[]
def fun(n,array1):
    for i in range(n):
        array1=i**4
        array.append(array1)
    # print(array1)
    # print("Now squaring process is being given to process 2")
    print(array)
def fun2(n,array2):  
    for i in range(n+1,11):
        array2=i**3
        array.append(array2)
    print(array)

if __name__ == '__main__':
    num = 5
    arr1=Array('i',range(0,11))
    arr2=Array('i',range(1,11))
    p1 = Process(target=fun, args=(num,arr1))
    p2 = Process(target=fun2, args=(num,arr2))
    # print(os.getpid())
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # p2.start()
    # p2.join()
    # print(num.value)
    # print(arr1[:])


from multiprocessing import Process, Value, Array
def f(n, a):
    n.value=n.value +10
def f1(n, a):
    n.value +=10
def f2(n, a):
    n.value +=10
def f3(n, a):
    n.value +=10
def f4(n, a):
    n.value +=10


num = Value('i', 0)
arr = Array('i', range(10))
print(num.value)
p = Process(target=f, args=(num, arr))
p.start()
p.join()
p1 = Process(target=f1, args=(num, arr))
p1.start()
p1.join()
p2 = Process(target=f2, args=(num, arr))
p2.start()
p2.join()
p3 = Process(target=f3, args=(num, arr))
p3.start()
p3.join()
p4 = Process(target=f4, args=(num, arr))
p4.start()
p4.join()
print(num.value)
#print(arr[:])

from multiprocessing import Process, Value, Array
def f1(n,a1,a2,arr3):
    n=5
    for j in range(n):
        a1[j]=j**2
        arr3[j]=j**2
    print(a1[:])
    for i in range(n,len(a2)):
        a2[i]=i**2
        arr3[i]=i**2
    print(a2[:])    
    print(arr3[:])
num=Value('i',5)
arr1=Array('i',range(1,11))
print(arr1[:])
arr2=Array('i',10)
print(arr2[:])
arr3=Array('i',10)
p1=Process(target=f1,args=(num,arr1,arr2,arr3))
p1.start()
# p1.join()
print(arr3[:])