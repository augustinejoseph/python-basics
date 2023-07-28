num = 0


def sum(num1, num2):
    return num1 + num2


print(sum(2, 4))


# Positional argument
def details(name, age):
    return name + str(age)


print(details(" Augustine : ", 24))


# Keyword argument
def details(name, age):
    return name + str(age)


print(details(age=24, name=" Augustine "))


# Args
def sum(*args):
    total = 0
    for num in args:
        total += num
    return total
print("Args")
print(sum(1,2,3,4,5))


# Kwargs
def details(**kwargs):
    for one, two in kwargs.items():
        print(f'{one} : {two}')
details(age =24, name = "Augustine")



# Lambda
result = (lambda x,y : x+y)(3,4)
print(result)

number = [1,2,3,4,5,6,7,8,9]
even_nums = list(filter(lambda x : x%2 ==0, number))
print(even_nums)