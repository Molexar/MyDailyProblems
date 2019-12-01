test = list(map(int, input().split(' ')))


def quick_sort(array):
    if len(array) <= 2:
        return sorted(array)
    else:
        pivot = len(array)-1
        index = 0
        while index < pivot:
            if array[pivot] < array[index]:
                pocket = array[pivot]
                array[pivot] = array[index]
                array[index] = array[pivot-1]
                array[pivot-1] = pocket
                pivot -= 1
            else:
                index += 1
        return quick_sort(array[:pivot])+[array[pivot]]+quick_sort(array[pivot+1:])


print(quick_sort(test))
