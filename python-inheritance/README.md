# Python - Inheritance

## Description

This project explores the concept of inheritance in Python, a key feature of object-oriented programming. Inheritance allows one class (the subclass) to inherit the attributes and methods of another class (the superclass), facilitating code reuse and the creation of hierarchical class structures. The project covers fundamental topics such as superclasses, subclasses, method overriding, and built-in functions like `isinstance`, `issubclass`, `type`, and `super`. It includes several tasks that implement and demonstrate these concepts through practical examples.

## General Concepts

- **Superclass, Base Class, or Parent Class:** A class that is inherited from.
- **Subclass:** A class that inherits from another class.
- **Listing Attributes and Methods:** How to list all attributes and methods of a class or instance.
- **Instance Attributes:** Understanding when an instance can have new attributes.
- **Inheriting Classes:** How to inherit a class from another.
- **Multiple Base Classes:** Defining a class with multiple base classes.
- **Default Class:** Every class inherits from the default `object` class.
- **Overriding Methods:** How to override a method or attribute inherited from the base class.
- **Inheritance Purpose:** Understanding the purpose of inheritance in programming.
- **Built-in Functions:** Utilizing `isinstance`, `issubclass`, `type`, and `super` to manage class relationships.

## Tasks

1. **Lookup**: Write a function that returns a list of available attributes and methods of an object. (File: `0-lookup.py`)
   
2. **My List**: Create a class `MyList` that inherits from `list` and includes a method to print the list sorted. (File: `1-my_list.py`)

3. **Exact Same Object**: Write a function that checks if an object is exactly an instance of a specified class. (File: `2-is_same_class.py`)

4. **Same Class or Inherit From**: Write a function that checks if an object is an instance of, or if it inherits from, a specified class. (File: `3-is_kind_of_class.py`)

5. **Only Sub Class Of**: Write a function that checks if an object is an instance of a class that inherits from a specified class. (File: `4-inherits_from.py`)

6. **Geometry Module**: Write an empty class `BaseGeometry`. (File: `5-base_geometry.py`)

7. **Improve Geometry**: Extend the `BaseGeometry` class to include an `area` method that raises an exception. (File: `6-base_geometry.py`)

8. **Integer Validator**: Add an `integer_validator` method to `BaseGeometry` that validates integer values. (File: `7-base_geometry.py`)

9. **Rectangle**: Create a `Rectangle` class that inherits from `BaseGeometry` and includes validation for width and height. (File: `8-rectangle.py`)

10. **Full Rectangle**: Enhance the `Rectangle` class to implement the `area` method and customize the `__str__` method for printing. (File: `9-rectangle.py`)

11. **Square #1**: Create a `Square` class that inherits from `Rectangle` and implements the necessary features. (File: `10-square.py`)

12. **Square #2**: Further extend the `Square` class to include proper string representation. (File: `11-square.py`)

---

## Author

- **Nathan Raynal**

