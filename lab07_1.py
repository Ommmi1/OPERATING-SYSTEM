from threading import Thread
import time

def thread1(val):
	print("Hello ! Omer This is Thread :", val)
	time.sleep(5)
	print("Thread 1 Terminated.")

def thread2(val):
	print("19B-004-SE This is Thread :", val)
	time.sleep(8)
	print("Thread 2 Terminated.")

if __name__ == "__main__":
	t1 = Thread(target=thread1, args=(1,))
	t2 = Thread(target=thread2, args=(2,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()


