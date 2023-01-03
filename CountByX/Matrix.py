def summaryRanges(nums: list[int]) -> list[str]:
    if not nums:
        return []
    nums = sorted(nums)
    nums.append(nums[-1])
    res = []
    right = nums[0]
    left = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == right + 1:
            right += 1
            continue

        if left == right:
            res.append(str(left))
        else:
            res.append(f"{left}->{right}")
        left = nums[i]
        right = nums[i]
    return res


numbers = [1, 4, 3, 2]
print(summaryRanges(numbers))