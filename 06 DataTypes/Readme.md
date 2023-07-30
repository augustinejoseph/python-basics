## List
* Store multiple data at once
* [] is used
* mutable
* can store data of different types
* can store duplicate elements
* accessed using list index


### Negative indexing
* -1 refers to the last index.
* -2 refers to the second last item.

### List slicing
* : is used
```
nums = [1,2,3,4,5]
print(nums(1:3))
```
### List Operations
* append() : add item to end

## List Comprehension
Concise way to create a list.
```
new_list = [expression for item in iterable if condition]
```

## Tuple
* () is  used.
* immutable
* can be nested  
* accessed using index
* negative indexing is also used.
* nested tuples are accessed using nested index.

```
nested_tuple = ((1, 2), ('a', 'b'), (True, False))
```
* var1 = ("Hello") # string
* var2 = ("Hello",) # tuple
Here trailing comma is used to indicate it is a tuple



## String
string is  a sequence of characters.




## Set
* Collection of unique data.
* empty set = set()
* empty dictionary = { }
* Implemented using hash tables.

#### 1. **Frozenset** = Immutable
#### 2. **Set** = Mutable 

### set operations
* **union  ( | )** = join two sets without duplicates.
* **Intersection ( & )** = elements common in both sets.
* **Difference ( - )** = Elements in first set, but not in second set.
* **Symmetric difference  (^ )** = Elements that are either of the sets, but not in both.
* **Subset (<= or issubset())** = if all elements of a set is present in another set.
* **Superset (>=)**  = A set is considered a superset of another set if it contains all the elements of the other set.


### Additional methods
* add() = Add element.
* remove() = Raises Key Error if element is not found
* discard() =  Doesn't raise error if element is not found.
* copy() = 
* clear() = Remove all elements in a set.


### Set comprehension
Concise way to write a set.
```
{expression for item in iterable if condition}
```


## Dictionary
