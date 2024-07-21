import os
import time
import tracemalloc

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def read_numbers(filename):
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f]

def write_numbers(filename, arr):
    with open(filename, 'w') as f:
        for num in arr:
            f.write(f"{num}\n")

def main():
    numbers = read_numbers("arq.txt")

    tracemalloc.start()
    start_time = time.time()
    
    sorted_numbers = quick_sort(numbers)
    
    end_time = time.time()
    memory_usage = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    
    write_numbers("arq-saida.txt", sorted_numbers)
    
    print(f"Tempo de execução: {(end_time - start_time) * 1000} ms")
    print(f"Memória utilizada: {memory_usage / 1024} KB")

if __name__ == "__main__":
    main()
