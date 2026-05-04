import random
import timeit

from insertion_sort import insertion_sort
from merge_sort import merge_sort 

def test_case_random(size):
    return [random.randint(0, size) for _ in range(size)]    


def test_case_sorted(size):
    lst = list(range(size)) 
    lst[size // 2], lst[size // 2 + 1] = lst[size // 2 + 1], lst[size // 2]
    return lst   


def measure(func, data):
    return timeit.timeit(lambda: func(data.copy()), number=10)


sizes = {"small": 50, "large": 1000} 
results = {}

for size_name, size in sizes.items(): 
    datasets = {
        "random": test_case_random(size),  
        "sorted": test_case_sorted(size)
    } 
    results[size_name] = {}

    for name, data in datasets.items(): 
        results[size_name][name] = {
            "insertion": measure(insertion_sort, data),
            "merge": measure(merge_sort, data),
            "timsort": measure(sorted, data)
        } 
 

print(f"{'| Algorithm': <18} | {'Small random data': <18} | {'Small sorted data': <18} | {'Big random data': <18} | {'Big sorted data': <18}") 
print(f"| {'-'*16} | {'-'*18} | {'-'*18} | {'-'*18} | {'-'*18}")
print(f"{'| Insertion Sort': <18} | {results['small']['random']['insertion']: <18.6f} | {results['small']['sorted']['insertion']: <18.6f} | {results['large']['random']['insertion']: <18.6f} | {results['large']['sorted']['insertion']: <18.6f}") 
print(f"{'| Merge Sort': <18} | {results['small']['random']['merge']: <18.6f} | {results['small']['sorted']['merge']: <18.6f} | {results['large']['random']['merge']: <18.6f} | {results['large']['sorted']['merge']: <18.6f}") 
print(f"{'| Timsort': <18} | {results['small']['random']['timsort']: <18.6f} | {results['small']['sorted']['timsort']: <18.6f} | {results['large']['random']['timsort']: <18.6f} | {results['large']['sorted']['timsort']: <18.6f}") 
    




     