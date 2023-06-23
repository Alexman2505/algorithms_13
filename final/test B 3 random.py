from typing import List, Tuple


class Stack:
    def __init__(self):
        """Инициализация пустого стека."""
        self._stack = []

    def _push(self, item) -> None:
        """Добавляет элемент в стек."""
        self._stack.append(item)

    def _pop(self):
        """Удаляет и возвращает последний элемент из стека."""
        return self._stack.pop()

    def is_empty(self) -> bool:
        """Проверяет, является ли стек пустым."""
        return not self._stack


def compare_items(
    item1: Tuple[str, int, int], item2: Tuple[str, int, int]
) -> bool:
    """Сравнивает два элемента по заданным критериям.

    Элементы сравниваются сначала по второму значению (tasks), затем по третьему значению (penalty),
    и в случае равенства - по первому значению (login).

    Args:
        item1: Первый элемент для сравнения.
        item2: Второй элемент для сравнения.

    Returns:
        True, если item1 должен идти перед item2 в отсортированном порядке. False в противном случае.
    """
    if (
        item1[1] > item2[1]
        or (item1[1] == item2[1] and item1[2] < item2[2])
        or (
            item1[1] == item2[1]
            and item1[2] == item2[2]
            and item1[0] < item2[0]
        )
    ):
        return True
    return False


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
        while left <= right and compare_items(array[left], pivot):
            left += 1
        while left <= right and compare_items(pivot, array[right]):
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    array[start], array[right] = array[right], array[start]
    return right


def quick_sort(array: List[Tuple[str, int, int]]) -> None:
    """Выполняет сортировку списка по заданным критериям.

    Используется алгоритм быстрой сортировки.

    Args:
        array: Список для сортировки.
    """
    stack = Stack()
    stack._push((0, len(array) - 1))
    while not stack.is_empty():
        start, end = stack._pop()
        if start >= end:
            continue
        pivot_idx = partition(array, start, end)
        if start < pivot_idx - 1:
            stack._push((start, pivot_idx - 1))
        if pivot_idx + 1 < end:
            stack._push((pivot_idx + 1, end))


# Чтение входных данных
n = int(input())
participants = []
for _ in range(n):
    login, tasks, penalty = input().split()
    participants.append((login, int(tasks), int(penalty)))

# Сортировка и вывод результатов
quick_sort(participants)
for participant in participants:
    login, _, _ = participant
    print(login)
