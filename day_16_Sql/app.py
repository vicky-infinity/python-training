import time

def timecalculate():
    result = 0
    for i in range(1, 1000001):
        result = i
        print(i)
    return result

starttime = time.time()
timecalculate()
endt = time.time()

print(f"Final time is {endt-starttime} seconds")