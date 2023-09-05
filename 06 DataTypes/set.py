empty_set = set([])
set_1 = set(["Augustine", "Kerala", 1, 2, False])
set_2 = {"Augustine"}
frozenset = frozenset()
print("is frozenset : ", type(frozenset))

# Union
union = set_1 | set_2
print("union : ", union)


# Intersection
intersection = set_1 & set_2
print(" Intersection : ", intersection)


# Difference
difference = set_1 - set_2
print(f"difference: {difference}")


# Symmetric difference
symmetric = set_1 ^ set_2
print("Symmetric : ", symmetric)


# Subset
print("Subset : ", set_1 <= set_2)


# Superset
print("Superset : ", set_1 >= set_2)


# set comprehensions
nums = (1, 2, 3, 4, 5)
set = {x**2 for x in nums}


text = "hello world"
upper = {x.upper() for x in text}
print(upper)
