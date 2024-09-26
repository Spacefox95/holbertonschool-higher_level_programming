# Python - Almost a Circle

## Description

The "Almost a Circle" project focuses on implementing object-oriented programming principles in Python, specifically through the creation and manipulation of geometric shapes. This project is designed to deepen my understanding of class design, inheritance, and serialization in Python. I explored the concepts of unit testing, JSON file handling, and the use of variable-length argument lists (`*args` and `**kwargs`). By the end of the project, I have developed a hierarchy of classes, including `Base`, `Rectangle`, and `Square`, each with their own attributes and methods. This structured approach not only enhances my programming skills but also prepares my for working with larger, more complex projects in Python.

## General Topics Covered

- Understanding Unit Testing and its implementation in large projects
- Serialization and deserialization of classes
- Writing and reading JSON files
- Utilizing `*args` for variable-length arguments in functions
- Utilizing `**kwargs` for named arguments in functions
- Handling named arguments effectively in function definitions

## Step-by-Step Implementation

1. **Create the Base Class**: Write the initial class `Base` to serve as the foundation for the other shapes.
2. **Implement the Rectangle Class**: Create the `Rectangle` class that inherits from `Base`.
3. **Add Validation**: Update the `Rectangle` class to validate all setter methods and instantiation (excluding `id`).
4. **Area Method**: Implement the public method `def area(self):` to return the area of the `Rectangle` instance.
5. **Display Method**: Create the `def display(self):` method to print the `Rectangle` using the character `#` without handling `x` and `y`.
6. **String Representation**: Override the `str` method in `Rectangle` to return a string representation of the instance.
7. **Enhanced Display Method**: Improve the `display` method to incorporate the `x` and `y` offsets in the output.
8. **Update Method with *args**: Add the `def update(self, *args):` method to assign values to the attributes.
9. **Update Method with *args and **kwargs**: Modify the `update` method to `update(self, *args, **kwargs)` for key/value assignment to attributes.
10. **Create the Square Class**: Implement the `Square` class that inherits from `Rectangle`.
11. **Size Getter and Setter**: Add public getter and setter methods for the `size` attribute in `Square`.
12. **Square Update Method**: Implement the `def update(self, *args, **kwargs)` method in `Square` to assign attributes.
13. **Dictionary Representation for Rectangle**: Add the `def to_dictionary(self):` method in `Rectangle` to return its dictionary representation.
14. **Dictionary Representation for Square**: Implement the `def to_dictionary(self):` method in `Square` to return its dictionary representation.
15. **File Saving Method**: In `Base`, add the class method `def savetofile(cls, listobjs):` to write the JSON string representation of `listobjs` to a file.
16. **JSON String Conversion**: Implement the static method `def fromjsonstring(jsonstring):` in `Base` to return a list of instances from a JSON string.
17. **Create Instance from Dictionary**: Add the class method `def create(cls, dictionary):` in `Base` to create an instance with all attributes set.
18. **Load from File**: Implement the class method `def loadfromfile(cls):` in `Base` to return a list of instances from a file.

This project serves as an excellent opportunity to practice and apply object-oriented programming concepts while working with JSON serialization in Python.

---

## Author

- **Nathan Raynal**