from heapq import heappush, heappop


def heap_sort(arr):
    heap = []
    sorted_list = []
    for i in arr:
        heappush(heap, i)

    while heap:
        sorted_list.append(heappop(heap))
    return sorted_list


print(heap_sort([9, 5, 7, 3, 2, 6, 0, 7, 1]))
