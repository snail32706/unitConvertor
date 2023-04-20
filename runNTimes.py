import time
import mathTool as mathTool

def time_func(func):
    
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("elapsed", end - start, "second")
    return wrapper

def _100000_times():
    for i in range(100000):
        mathTool.Unit_Convertor_Math(i, 'K', 'eV').unit_convertor()

_100000_times = time_func(_100000_times)

_100000_times()