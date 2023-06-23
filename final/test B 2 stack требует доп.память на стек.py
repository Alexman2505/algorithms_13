class Stack:
    def __init__(self):
        self.__stack = []

    def __push(self, item):
        self.__stack.append(item)

    def __pop(self):
        if self.__stack:
            return self.__stack.pop()


def quick_sort(arr, start, end):
    stack = Stack()
    stack._Stack__push(
        (start, end)
    )  # Используем приватный метод push для добавления пары индексов в стек
    while stack._Stack__stack:
        start, end = stack._Stack__pop()  # Извлекаем пару индексов из стека
        if start >= end:
            continue
        pivot = arr[start][1]
        left = start + 1
        right = end
        while left <= right:
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
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        arr[start], arr[right] = arr[right], arr[start]

        if start < right - 1:
            stack._Stack__push((start, right - 1))
        if right + 1 < end:
            stack._Stack__push((right + 1, end))


n = int(input())
participants = []
for _ in range(n):
    login, problems_solved, penalty = input().split()
    problems_solved = int(problems_solved)
    penalty = int(penalty)
    participants.append((login, problems_solved, penalty))

quick_sort(participants, 0, n - 1)

for participant in participants:
    print(participant[0])
