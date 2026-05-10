import threading
import time

def task(name):
    print(f"Task {name} is starting.")
    time.sleep(2)
    print(f"Task {name} is done.")

    # threading.current_thread() returns the current thread object, and .name gives us the name of that thread.
    print(f"Task {name} is running in thread: {threading.current_thread().name}")


start = time.perf_counter()

if __name__ == "__main__":

    task("1")  # This will run in the main thread
    task("2")  # This will also run in the main thread
    task("3")  # This will also run in the main thread

    finish = time.perf_counter()

    print(f"Finished in {finish - start} second(s)")


    print("Executing task() using threads")

    start = time.perf_counter()
    t1 = threading.Thread(target=task, args=("1",))
    t2 = threading.Thread(target=task, args=("2",))
    t3 = threading.Thread(target=task, args=("3",))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    finish = time.perf_counter()
    print(f"Finished in {finish - start} second(s)")