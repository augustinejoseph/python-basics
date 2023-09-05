dictionary = {"name": "Augustine", "place": "Kerala"}

# Printing dictionary
for key, value in dictionary.items():
    print(value)


# Adding element
dictionary["qualification"] = "Graduate"
dictionary["key_3"] = "value_3"
print(dictionary)

# Removing element
del dictionary["place"]
dictionary.pop("key_3")
print(dictionary)


# Exists in dictionary
if "name" in dictionary:
    print(f'Name exists. Name is  {dictionary["name"]}')
else:
    print("does not exist")
