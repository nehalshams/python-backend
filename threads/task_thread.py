# Create a class to print 1 to 100 using threads for each number
import threading


class NumberPrinter(threading.Thread):
    def __init__(self, number):
        self.number = number
        threading.Thread.__init__(self)

    def run(self):
        print(f"Number: {self.number} is printed in thread: {threading.current_thread().name}")

if __name__ == "__main__":
    threads = []
    for i in range(1, 101):
        t = NumberPrinter(i)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

