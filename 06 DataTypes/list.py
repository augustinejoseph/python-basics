nums = [1, 2, 3, 4, 5]
print(nums[1:3])


# List comprehension
list_comprehension = [n**2 for n in nums if n > 4]
print(list_comprehension)
odd_even = ["even" if n % 2 == 0 else "odd" for n in nums]
print(odd_even)
