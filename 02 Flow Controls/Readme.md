## if ... elif ...else
```
if condition1:
    # code block 1

elif condition2:
    # code block 2

else: 
    # code block 3
```

1. If condition1 evaluates to true, code block 1 is executed.
2. If condition1 evaluates to false, then condition2 is evaluated.
* If condition2 is true, code block 2 is executed.
* If condition2 is false, code block 3 is executed.

## For loop
Used to iterate over a sequence (list, tuple, string or range) and execute a block of code for each item in the sequence.

```
sequence = ['Swift', 'Python', 'Go']

for item in sequence
for _ in sequence:
    print('HEllO')

```

##  While loop
Run a code until a certain condition is met.
```
while condition:
    #body
```

``` 
 While loop is used if the number of iterations is unknown

 For loop is used if the number of iterations is known 
```

## Break
Used to terminate a loop

## Continue
The continue statement skips the rest of the current iteration and moves to the next iteration.

```
numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)

<!-- output : 1,3,5 -->
```


## Pass
null statement used as a placeholder for future  code.