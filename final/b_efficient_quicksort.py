# 88566146
from typing import List


class Participant:
    def __init__(self, login: str, tasks: int, penalty: int):
        """Конструктор класса Participant.

        Принимает на вход логин участника, количество выполненных
        задач участника, и значение штрафа участника.
        """
        self.login = str(login)
        self.tasks = int(tasks)
        self.penalty = int(penalty)

    def __str__(self) -> str:
        """Возвращает строковое представление участника."""
        return self.login

    def __lt__(self, other: 'Participant') -> bool:
        """Определяет отношение "меньше" для участников.

        Это перезагруженный магический метод представляет собой
        оператор сравнения "<" меньше.
        Участники сортируются сначала по количеству выполненных задач
        (в убывающем порядке), затем по значению штрафа
        (в возрастающем порядке),и в случае равенства - по логину
        (в алфавитном порядке). Возвращается булево значение
        в зависимости от сравнения.
        """
        if self.tasks != other.tasks:
            return self.tasks > other.tasks
        if self.penalty != other.penalty:
            return self.penalty < other.penalty
        return self.login < other.login


def quick_sort(array: List[Participant]) -> None:
    """Выполняет сортировку списка участников по заданным критериям (in-place).

    Принимает на вход список (массив) участников для сортировки
    Внутри функция _quick_sort рекурсивно вызывает себя и partition
    для сортировки массива, используя модификацию алгоритма быстрой сортировки.
    """

    def partition(start: int, end: int) -> int:
        """Выполняет разделение списка на подсписки вокруг опорного элемента.

        Принимает на вход индекс начала и конца подсписка. Возвращает индекс
        опорного элемента. Используется алгоритм Хоара для разделения списка
        на две части вокруг опорного элемента.
        """
        pivot = array[start]
        left = start + 1
        right = end
        while left <= right:
            while left <= right and array[right] > pivot:
                right -= 1
            while left <= right and array[left] < pivot:
                left += 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        array[start], array[right] = array[right], array[start]
        return right

    def _quick_sort(left: int, right: int) -> None:
        """Выполняет рекурсивную сортировку списка.

        Принимает на вход индекс начала и конца списка.
        """
        if left < right:
            pivot_index = partition(left, right)
            _quick_sort(left, pivot_index - 1)
            _quick_sort(pivot_index + 1, right)

    _quick_sort(0, len(array) - 1)


if __name__ == '__main__':
    number_of_participants = int(input())
    participants = [
        Participant(*input().split()) for _ in range(number_of_participants)
    ]

    quick_sort(participants)
    print(*participants, sep='\n')
