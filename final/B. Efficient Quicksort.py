# 88495145
from typing import List, Tuple


def compare_items(
    item1: Tuple[str, int, int], item2: Tuple[str, int, int]
) -> bool:
    """Сравнивает два элемента по заданным критериям.

    Элементы сравниваются сначала по второму значению (tasks),
    затем по третьему значению (penalty),
    и в случае равенства - по первому значению (login).
    """
    return (
        item1[1] > item2[1]
        or (item1[1] == item2[1] and item1[2] < item2[2])
        or (
            item1[1] == item2[1]
            and item1[2] == item2[2]
            and item1[0] < item2[0]
        )
    )


def partition(array: List[Tuple[str, int, int]], start: int, end: int) -> int:
    """Выполняет разделение массива на подмассивы в соответствии с опорным элементом.

    Используется алгоритм Хоара для разделения массива на две части вокруг опорного элемента.

    Args:
        array: Массив для разделения.
        start: Индекс начала подмассива.
        end: Индекс конца подмассива.

    Returns:
        Индекс опорного элемента.
    """
    pivot = array[start]
    left = start + 1
    right = end
    while left <= right:
        while left <= right and compare_items(pivot, array[right]):
            right -= 1
        while left <= right and compare_items(array[left], pivot):
            left += 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    array[start], array[right] = array[right], array[start]
    return right


def quick_sort(
    array: List[Tuple[str, int, int]], left: int, right: int
) -> None:
    """Выполняет сортировку списка по заданным критериям (in-place).

    Используется модификация алгоритма быстрой сортировки "in-place".

    Args:
        array: Список для сортировки.
        left: Индекс начала списка.
        right: Индекс конца списка.
    """
    if left < right:
        pivot_index = partition(array, left, right)
        quick_sort(array, left, pivot_index - 1)
        quick_sort(array, pivot_index + 1, right)


# Чтение входных данных
n = int(input())
participants = []
for _ in range(n):
    login, tasks, penalty = input().split()
    participants.append((login, int(tasks), int(penalty)))

# Сортировка и вывод результатов
quick_sort(participants, 0, n - 1)
for participant in participants:
    login, _, _ = participant
    print(login)
