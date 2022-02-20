from threading import Thread
import time
message=(input("enter message "))
n=int(input("enter how much times you want to print message"))


def create_thread(n):
    for threads in range(n):
        # threads+=threads
        print(message,threads)
        

create_thread(n)
t1 = Thread(target=create_thread, args=(1,))
t1.start()
t1.join()

# from threading import Thread
# import time
# number=0
# msg_array=[]
# class myThread(Thread):
#     def __init__(self,ThreadID,message,printmessagecount):
#         Thread.__init__(self)
#         self.ThreadID=ThreadID
#         self.message=message
#         self.printmessagecount=printmessagecount
#     def run(self):
#         print_msg(self.message,10)


# def print_msg(msg,printmessagecount):
#     while printmessagecount:
#         time.sleep(3)
#         msg_array.append(msg)
#         printmessagecount-=printmessagecount
    
#     for i in msg_array:
#         global number
#         number+=number
#         print(str(i)+''+str(number))
# msg=input("enter message ")
# printmessagecount=int(input("enter how much times you want to print message"))