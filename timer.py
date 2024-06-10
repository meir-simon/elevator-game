import time

class Timer:
    def __init__(self,time_to_run_down_from):
        """
        Initialize the Timer object.

        Parameters:
        time_to_run_down_from (float): The duration of the timer in seconds.
        """
        self.time = time.time() # The time when the timer was started
        self.time_to_run_down_from = time_to_run_down_from # The duration of the timer

    def time_left(self):
        """
        Calculate the remaining time on the timer.

        Returns:
        float: The remaining time in seconds if the timer has not yet expired.
        None: If the timer has expired.
        """
        time_left = self.time_to_run_down_from - (time.time() - self.time)# Calculate the time left
        if time_left >= 0:
            return time_left  # Return the remaining time if it is non-negative
        return None # Return None if the timer has expired
        