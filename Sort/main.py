def merge_arrays(array1, array2):
    i, j = 0, 0
    a1 = len(array1)
    a2 = len(array2)
    array3 = []
    while i < a1 and j < a2:
        if array1[i] <= array2[j]:
            array3.append(array1[i])
            i += 1
        else:
            array3.append(array2[j])
            j += 1
    array3 += array1[i:] + array2[j:]
    return array3


def mergesort(array):
    if len(array) < 2:
        return array
    else:
        left = mergesort(array[:len(array) // 2])
        right = mergesort(array[len(array) // 2:])
        return merge_arrays(left, right)
