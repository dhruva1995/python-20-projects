def binary_search(nums: list[int], key: int) -> int:
    if nums:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] == key:
                return mid
            elif nums[mid] < key:
                start = mid + 1
            else:
                end = mid - 1
    return -1


print(binary_search([1, 34, 45, 67, 234, 546, 6007, 7004], 1))
