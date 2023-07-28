## Python Identifiers
Identifiers are the name given to variables, classes, methods, etc. For example,

`language = 'Python'`

Here, language is a variable (an identifier) which holds the value 'Python'.


## Variables
Variable is a container to store data

`num = 10`

Here `num` is a variable storing the data 10.

### Naming conventions
* Descriptive names
* Lowercase letters
* separate words with underscore
* Constants with capital letters  `PI=3.14`

### Assigning multiple values to Multiple variables
`a, b, c = 5, True, "Augustine Joseph"`


## Literals
A fixed value that appears directly in the code.

`company_name = "A company name" `

`result = True`

`value = None`

### Literal Collections
#### List literals
```
people = ["Augustine", "Nithin", "Arun", "Abhinav"]
```

#### Tuple literals
```
numbers = (1,2,3,4,5)
```

#### Dictionary literals
```
car_brands = {'ford': 'endevour', 'tata': 'safari'}
```

#### Set literals
```
vowels = {a,e,i,o,u}
```


## Data Types
1. Numeric - int, float,complex
2. String - str
3. Sequence - list, range, tuple
4. Mapping -dict
5. Boolean - bool
6. Set - set, frozenset


## Type conversions
Changing one data type to another (eg: int to str)
* implicit conversion - python converts automatically
* explicit conversion (typecasting) - manually converted. 

## Namespace
Collection of names
* Built-in (All over python)
* Global (Module)
* Local (Function)


## Global
when you create a variable outside of any function or block of code, it is called a global variable. Global variables are accessible from anywhere in the code, including inside functions.

However, if you want to modify the value of a global variable from within a function, you need to use the global keyword. This is because, by default, Python assumes that any variable created or modified inside a function is a local variable, not a global one.