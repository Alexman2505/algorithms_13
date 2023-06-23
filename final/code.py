# 88488493
def broken_search(nums, target) -> int:
    """Ищет целевой элемент в отсортированном, но сломанном массиве
    с использованием модифицированного алгоритма бинарного поиска.

    Аргументы:
        nums (List[int]): Отсортированный, но сломаный массив уникальных чисел.
        target (int): Целевой элемент для поиска.
    Возвращает:
        int: Индекс целевого элемента, если он найден, или -1, если не найден.
    """

    def update_search_range(left, right, middle, target):
        """Обновляет диапазон поиска на основе сравнения целевого элемента
        и элементов с указанными индексами.

        Аргументы:
            left (int): Левый индекс текущего диапазона поиска.
            right (int): Правый индекс текущего диапазона поиска.
            middle (int): Средний индекс текущего диапазона поиска.
            target (int): Целевой элемент для поиска.
        Возвращает:
            Tuple[int, int]: Кортеж, представляющий обновленный диапазон поиска (left, right).
        """

        if nums[left] <= target < nums[middle] or (
            nums[middle] <= nums[right] < nums[left]
            and (target < nums[middle] or target >= nums[left])
        ):
            return left, middle - 1
        else:
            return middle + 1, right

    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        left, right = update_search_range(left, right, middle, target)
    return -1
