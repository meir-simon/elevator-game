import time
from settings import *
class timer:
    def __init__(self,time_to_run_down_from):
        self.time = time.time()
        self.time_to_run_down_from = time_to_run_down_from
    def time_left(self):
        time_left = self.time_to_run_down_from - (time.time() - self.time)
        if time_left >= 0:
            return time_left
        return None
        