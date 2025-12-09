"""
Problem: Minimum Time to Complete Tasks

You have a list of workers, where workers[i] is the time (in minutes) it takes worker i to complete one task.
Workers can work independently and simultaneously, and each worker can do multiple tasks.

You need to complete t tasks total.

Return the minimum number of minutes needed to finish at least t tasks.
"""

# Output should be: 42
workers = [2, 3, 7, 5, 11]
t = 50

def min_minutes(workers, tasks):
    low, high = 0, min(workers) * tasks

    while low < high:
        mid = (low + high) // 2

        total = sum(mid // worker for worker in workers)

        if total >= tasks:
            high = mid
        else:
            low = mid + 1
    
    return low

print(min_minutes(workers, t))
