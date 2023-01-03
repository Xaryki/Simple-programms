def IntRangers(nums: list[int]):
    nums = sorted(nums)
    nums += [nums[-1]]
    lst = []
    left, right = nums[0], nums[0]
    for i in range(1, len(nums)):
        if nums[i] == right + 1:
            right += 1
            continue
        if left == right:
            lst += [f"{left}"]
        else:
            lst += [f"{left}-{right}"]
        left = nums[i]
        right = nums[i]
    return lst


numbers = [1, 4, 5, 2, 3, 9, 8, 11, 0]
print(IntRangers(numbers))
