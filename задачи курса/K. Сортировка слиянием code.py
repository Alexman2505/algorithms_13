from typing import List


def merge(arr: List[int], left: int, mid: int, right: int) -> List[int]:
    left_arr = arr[left:mid]
    right_arr = arr[mid:right]
    i = j = 0
    k = left
    merged = []

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            merged.append(left_arr[i])
            i += 1
        else:
            merged.append(right_arr[j])
            j += 1

    while i < len(left_arr):
        merged.append(left_arr[i])
        i += 1

    while j < len(right_arr):
        merged.append(right_arr[j])
        j += 1

    arr[left:right] = merged
    return arr


def merge_sort(arr: List[int], left: int, right: int) -> None:
    if left < right - 1:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right)


def test() -> None:
    a = [1, 4, 9, 2, 10, 11]
    merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert a == expected

    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, len(c))
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected
