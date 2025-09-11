#### MultiThreading = It allows you to create processes that runs in parallel.
#### When to use 
''' 
* CPU Bound task = task which is computationally very very heavy heavy on the CPU(eg: Mathematical process)
* Parallel execution = Multiple cores of the CPU 
'''

import multiprocessing,time

def square_num():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")
        
def cube_num():
    for i in range(5):
        time.sleep(1)
        print(f"Cube: {i*i*i}")

if __name__ == "__main__":
    # Create two process
    p1= multiprocessing.Process(target=square_num)
    p2= multiprocessing.Process(target=cube_num)
    t = time.time()

    # start the process
    p1.start()
    p2.start()

    # wait for the process to complete
    p1.join()
    p2.join()
    
    finished_time = time.time() - t
    print(f"Finished Time: {finished_time}") ## open task manager and see the process opened