## Polymorphism(many forms)

1. Duck Typing : 
2. Operator Overloading: 
3. *Method Overloading: Not possible in python.* No two methods with same name can be created. Make the python interpreter slow.
4. Method Overriding: Method with same name and parameters in both classes which are inherited.



## Inheritance

**Single Inheritance**: A class only inherits from a single base class.

**Multiple Inheritance**:Class inherits from more than one base class.

**Multi-level Inheritance**: A class inherits from another class, which in turn inherits from another class.

## **Super**

1. **Calling the Superclass Constructor (Initializer)**:
You can use **`super().__init__()`** in the constructor of a subclass to call the constructor of the superclass.
2. **Calling Superclass Methods**:
You can use **`super().method_name()`** to call a method from the superclass.
3. **Multiple Inheritance**:
In cases of multiple inheritance, **`super()`** helps you call methods and constructors from different base classes in a specific order defined by the Method Resolution Order (MRO).


## **MRO or Method Resolution Order** 
First, it is searched in the current class. If not found, the search moves to parent classes. This is left-to-right, depth-first.
Python 3 uses the **[C3 linearization](https://en.wikipedia.org/wiki/C3_linearization)** algorithm for MRO.