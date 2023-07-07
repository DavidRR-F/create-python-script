def sum_list_cython(list items):
    cdef int sum = 0
    cdef int i
    for i in range(len(items)):
        sum += items[i]
    return sum