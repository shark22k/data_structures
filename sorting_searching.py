# sorting


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_value = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < min_value:
                i_min = j
                min_value = arr[j]
        arr[i], arr[i_min] = arr[i_min], arr[i]
    return arr


def bubble_sort_1(arr):
    for i in range(1, len(arr)):
        swapping_happen = False
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                swapping_happen = True
        if not swapping_happen:
            break
    return arr


def bubble_sort_2(arr):
    for i in range(len(arr) - 1):
        swapping_happen = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                swapping_happen = True
        if not swapping_happen:
            break
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        hole = i
        value = arr[hole]
        while hole > 0 and arr[hole - 1] > value:
            arr[hole] = arr[hole - 1]
            hole -= 1
        arr[hole] = value
    return arr


def binary_search(arr):
    def binary_search_h(arr, start, end, value):
        if start <= end:
            mid = (start + end) // 2
            if arr[mid] == value:
                return mid
            elif arr[mid] < value:
                binary_search_h(arr, mid + 1, end, value)
            else:
                return binary_search_h(arr, start, mid - 1, value)

    return binary_search_h(arr, 0, len(arr) - 1, 5)


# print(binary_search([x for x in [10,2,2,3,4,5,5,5,8,9,10]]))

def merge_sort(arr):

    def merge(arr, left, right):
        left_ptr = 0
        right_ptr = 0
        arr_ptr = 0
        while left_ptr < len(left) and right_ptr < len(right):
            if left[left_ptr] < right[right_ptr]:
                arr[arr_ptr] = left[left_ptr]
                left_ptr += 1
            else:
                arr[arr_ptr] = right[right_ptr]
                right_ptr += 1
            arr_ptr += 1
        while left_ptr < len(left):
            arr[arr_ptr] = left[left_ptr]
            left_ptr += 1
            arr_ptr += 1
        while right_ptr < len(right):
            arr[arr_ptr] = right[right_ptr]
            right += 1
            arr_ptr += 1

    def merge_sort_h(arr, start, end):
        if start < end:
            start = 0
            end = len(arr) - 1
            mid = (start + end) // 2
            left = [x for x in arr[:(mid + 1)]]
            right = [x for x in arr[(mid + 1):]]
            print(f"left {left}")
            print(f"right {right}")
            merge_sort_h(left, 0, len(left) - 1)
            merge_sort_h(right, 0, len(right) - 1)
            merge(arr, left, right)
            print(f"merged {arr}")

    merge_sort_h(arr, 0, len(arr) - 1)
    return arr


print(merge_sort([x for x in range(10, 0, -1)]))
