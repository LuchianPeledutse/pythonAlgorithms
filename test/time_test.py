import time



def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        time_result = round(end-start, 5)
        return time_result
    return wrapper