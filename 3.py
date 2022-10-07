from random import random, randrange
import time

def insertion_sort(container):
   for i in range(1, len(container)):
        key = container[i]
        j = i - 1
        while j >= 0 and key < container[j]:
            container[j + 1] = container[j]
            j -= 1
        container[j + 1] = key

def quick_sort(container):
    if len(container) > 1:
        pivot = container[len(container) // 2]

        less = []
        greater = []
        equal = []

        for i in container:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                equal.append(i)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return container

if __name__ == '__main__':

    arr = [randrange(13, 26) for _ in range(10**6)]

    time_list = []

    for _ in range(11):
        start = time.perf_counter()
        insertion_sort(arr)
        time_list.append(time.perf_counter() - start)

    print(f"сортировка вставками занимает {sum(time_list) / 10}")

    for _ in range(11):
        start = time.perf_counter()
        quick_sort(arr)
        time_list.append(time.perf_counter() - start)

    print(f"быстрая сортировка занимает {sum(time_list) / 10}")









