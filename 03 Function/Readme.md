## Function
A block of code that performs a specific task.

1. **Standard library functions** : Built in python functions
2. **User-defined functions** : Custom functions.


```
def function_name(arguments):
    #function body

    return
```

1. **Argument** : A value passed to a function.
2. **return** : Return some value to function call.


## Arguments
Value accepted by a function
1. **Positional Arguments**
2. **Keyword Arguments**

### Positional arguments:
Arguments passed to the function in the order they are defined in function.
```
def details(name, age):
    return name+ str(age)
print(details(" Augustine : " , 24))
```

### Keyword argument
Here arguments are passed as parameter_name = value.
Order of the argument doesn't matter.

```
def details(name, age):
    return name+ str(age)
print(details(age : 24, name: " Augustine"))

```


### Arbitrary Argument (Variadic functions)
To pass unknown nunber of arguments to a function
1. **args** (Arbitrary number of positional arguments.)
```
def sum(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum(1,2,3,4,5))
```


2. **kwargs** (Arbitrary number of keyword arguments.)
```
def details(**kwargs):
    for one, two in kwargs.items():
        print(f'{one} : {two}')
details(age =24, name = "Augustine")
```


## Anonymous function (Lambda)
No function name

 ```
lambda (arguments) : single expression
```
