def broken_search(nums, target) -> int:
    def update_search_range(left, right, middle, target):
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

        left, right = update_search_range(left, right, middle, target)
    return -1


def test():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
    print(broken_search(arr, 1))


test()
