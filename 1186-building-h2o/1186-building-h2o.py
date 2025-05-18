import threading

class H2O:
    def __init__(self):
        self.h_semaphore = threading.Semaphore(2)  # 2 hydrogen threads allowed
        self.o_semaphore = threading.Semaphore(1)  # 1 oxygen thread allowed
        self.barrier = threading.Barrier(3)        # Wait until 3 threads are ready


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_semaphore.acquire()
        self.barrier.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.h_semaphore.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_semaphore.acquire()
        self.barrier.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.o_semaphore.release()