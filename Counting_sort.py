# It sort the elements in the particular range. And cannot sort negative elements.


def counting_sort(n, m, arr):
    range_numbers = m - n + 1
    counts = [0 for i in range(range_numbers + 1)]
    print(counts)
    for number in arr:
        counts[number] += 1
    for count in range(len(counts)):
        print((str(count) + " ") * counts[count], end="")


# # Analysis :
# Here We have to traverse the number of keys : ie n number of keys so time for this
# traversal is O(n). After that we need to traverse the counts array for this time taken
# is k .  So time Complexity for Counting Sort is O(n+k)


counting_sort(1, 5, [1, 2, 1, 3, 2, 1, 5, 3, 4])
