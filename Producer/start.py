import threading
from producer import run

def print_cube(num):
	# function to print cube of given num
	run(num)










if __name__ =="__main__":
	# creating thread
	t1 = threading.Thread(target=print_cube, args=(4000,))
	t2 = threading.Thread(target=print_cube, args=(4001,))

	# starting thread 1
	t1.start()
	# starting thread 2
	t2.start()
