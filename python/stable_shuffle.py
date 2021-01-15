import time
import random

def stable_shuffle(lst, window, shift):
    size = len(lst)
    if size <= 1:
        return lst
    start = 0
    end = min(start+window, size)
    while start < end and start < size:
        shuffle(lst, start, end)
        start += shift
        end = min(start + window, size)
    return lst

def shuffle(lst, start, end):
    while start < end:
        r = random.randint(start, end-1)
        if start != r:
            lst[start], lst[r] = lst[r], lst[start]
        start += 1

lst = []
for i in range(100):
    lst.append(i)
start_time = time.time()
lst = stable_shuffle(lst, 10, 5)
end_time = time.time()
print("%.3f" % (end_time-start_time))
print(lst)
