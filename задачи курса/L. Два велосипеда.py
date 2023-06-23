def find_bike_days(n, savings, bike_cost):
    first_bike_day = -1
    second_bike_day = -1
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if savings[mid] >= bike_cost:
            first_bike_day = mid
            right = mid - 1
        else:
            left = mid + 1

    if first_bike_day == -1:
        return -1, -1

    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if savings[mid] >= 2 * bike_cost:
            second_bike_day = mid
            right = mid - 1
        else:
            left = mid + 1

    if second_bike_day == -1:
        return first_bike_day + 1, -1

    return first_bike_day + 1, second_bike_day + 1


n = int(input())
savings = list(map(int, input().split()))
bike_cost = int(input())

result = find_bike_days(n, savings, bike_cost)
print(result[0], result[1])


################################
def binarySearch(money, price, left, right):
    if right <= left and left != 0:
        return -1
    middle = (left + right) // 2
    if money[middle] >= price and (money[middle - 1] < price or middle == 0):
        return middle + 1
    elif price <= money[middle]:
        return binarySearch(money, price, left, middle)
    else:
        return binarySearch(money, price, middle + 1, right)


days = int(input())
money = [int(num) for num in input().split(' ')]
price = int(input())
print(binarySearch(money, price, left=0, right=len(money)), end=' ')
print(binarySearch(money, price * 2, left=0, right=len(money)), end=' ')
