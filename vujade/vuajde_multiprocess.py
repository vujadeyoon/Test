import os
import time
from multiprocessing import Process
from multiprocessing import Queue


class BaseMultiProcess:
    def __init__(self, _target_method, _num_processes=os.cpu_count()):
        self.target_method = _target_method
        self.n_processes = _num_processes

    def proc_setup(self):
        self.queue = Queue()
        self.process = [Process(target=self.target_method, args=(self.queue,)) for _ in range(self.n_processes)]

        for p in self.process: p.start()

    def proc_release(self):
        for _ in range(self.n_processes): self.queue.put((None, None)) # Todo: The number of parameters for queue.put() should be checked.
        while not self.queue.empty(): time.sleep(1)
        for p in self.process: p.join()
