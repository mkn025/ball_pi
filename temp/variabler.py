from cProfile import run
import time


# function that prints runtimes of program
start_time = time.time()
def runtime():
    print("Runtime: " + str(time.time() - start_time) + " seconds")



for n  in range(1,1000):
    print(n)



round(runtime(),)