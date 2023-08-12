import time

n = 500000

start = time.process_time()
for i in range(n):
    print(".", end='')
end = time.process_time()
cpu_time_used = end - start
print("timing with i/o", cpu_time_used)

total = 0
n = 500000
start2 = time.process_time()
for i in range(n):
    total += i
end2 = time.process_time()
cpu_time_used2 = end2 - start2
print("timing without i/o", cpu_time_used2)