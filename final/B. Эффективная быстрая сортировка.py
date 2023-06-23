def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = arr[start][1]  # Выбираем первый элемент в качестве опорного
    left = start + 1
    right = end
    while left <= right:
        # Поиск элементов, которые нужно поменять местами
        while left <= right and (
            arr[left][1] > pivot
            or (arr[left][1] == pivot and arr[left][2] < arr[start][2])
            or (
                arr[left][1] == pivot
                and arr[left][2] == arr[start][2]
                and arr[left][0] < arr[start][0]
            )
        ):
            left += 1
        while left <= right and (
            arr[right][1] < pivot
            or (arr[right][1] == pivot and arr[right][2] > arr[start][2])
            or (
                arr[right][1] == pivot
                and arr[right][2] == arr[start][2]
                and arr[right][0] > arr[start][0]
            )
        ):
            right -= 1
        if left <= right:
            arr[left], arr[right] = (
                arr[right],
                arr[left],
            )  # Меняем элементы местами
            left += 1
            right -= 1
    arr[start], arr[right] = (
        arr[right],
        arr[start],
    )  # Помещаем опорный элемент на правильное место
    quick_sort(arr, start, right - 1)  # Рекурсивно сортируем левую часть
    quick_sort(arr, right + 1, end)  # Рекурсивно сортируем правую часть


# Считываем количество участников
n = int(input())

participants = []
# Считываем информацию о каждом участнике
for _ in range(n):
    login, problems_solved, penalty = input().split()
    problems_solved = int(problems_solved)
    penalty = int(penalty)
    participants.append((login, problems_solved, penalty))

quick_sort(participants, 0, n - 1)

# Выводим логины отсортированных участников
for participant in participants:
    print(participant[0])
