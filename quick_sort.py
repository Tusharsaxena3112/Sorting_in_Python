def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
        greater = []
        lower = []
        for i in range(length - 1):
            if sequence[i] > pivot:
                greater.append(sequence[i])
            else:
                lower.append(sequence[i])
        return quick_sort(lower) + [pivot] + quick_sort(greater)


print(quick_sort([2, 3, 1, 5, 6, 7, 1, 4, 8, 1]))
print(quick_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
