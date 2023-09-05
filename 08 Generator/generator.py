def generator(nums):
    for n in nums:
        yield n

nums = [1,2,3,4,5]
result = generator(nums)
print(next(result))
print(next(result))
print(next(result))
