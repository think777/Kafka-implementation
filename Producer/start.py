import threading
from producer import run

def print_cube(num):
	# function to print cube of given num
	run(num)










if __name__ =="__main__":
	
	# creating an empty list
	
	name = {}
# number of elements as input
	n = int(input("Enter number of producers : "))
# iterating till the range
	for i in range(0, n):
		s = (input("Enter name of producer : "))
		ele = int(input("Enter port number : "))
		name[s] = ele # adding the element

	

	# creating thread
	for key, value in name.items():
		key = threading.Thread(target=print_cube, args=(value,))
		# starting thread 1
		key.start()

	
	
