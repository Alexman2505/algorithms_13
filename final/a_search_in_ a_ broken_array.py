# 88543131
def broken_search(nums, target) -> int:
    """Ищет целевой элемент в отсортированном, но сломанном массиве
    с использованием модифицированного алгоритма бинарного поиска.

    Аргументы:
        nums (List[int]): Отсортированный, но сломаный массив уникальных чисел.
        target (int): Целевой элемент для поиска.
    Возвращает:
        int: Индекс целевого элемента, если он найден, или -1, если не найден.
    """

    def update_search_range(
        left, right, middle, target, left_value, middle_value
    ):
        """Обновляет диапазон поиска на основе сравнения целевого элемента
        и элементов с указанными индексами.

        Аргументы:
            left (int): Левый индекс текущего диапазона поиска.
            right (int): Правый индекс текущего диапазона поиска.
            middle (int): Средний индекс текущего диапазона поиска.
            target (int): Целевой элемент для поиска.
            left_value (int): Значение элемента с левым индексом.
            middle_value (int): Значение элемента с средним индексом.
        Возвращает:
            Tuple[int, int]: Кортеж, представляющий обновленный диапазон поиска (left, right).
        """
        if left_value < target < middle_value or (
            middle_value <= nums[right] < left_value
            and (target < middle_value or target > left_value)
        ):
            return left, middle - 1
        return middle + 1, right

    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        middle_value = nums[middle]
        left_value = nums[left]

        if middle_value == target:
            return middle
        if left_value == target:
            return left

        left, right = update_search_range(
            left, right, middle, target, left_value, middle_value
        )
    return -1
