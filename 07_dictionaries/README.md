# Python Dictionaries

This section contains exercises focused on **Python dictionaries**, one of the most useful data structures for organizing and accessing data using key-value pairs.

## 🎯 Learning Objectives

The exercises in this section are designed to practice:

* Creating and modifying dictionaries
* Working with key-value pairs
* Adding and updating dictionary elements
* Accessing dictionary values
* Iterating through dictionaries
* Using `.keys()`, `.values()`, and `.items()`
* Combining dictionaries with loops and conditional statements
* Using built-in functions such as `min()` and `max()`
* Organizing structured data

## 📚 Concepts Covered

### Creating a Dictionary

```python
students = {
    1: 175,
    2: 182,
    3: 168
}
```

In this example, each student number is used as a **key**, while the student's height is stored as the **value**.

### Adding Data

New key-value pairs can be added directly:

```python
students[4] = 171
```

### Accessing Values

```python
print(students[1])
```

### Iterating Through a Dictionary

The `.items()` method allows both keys and values to be accessed:

```python
for student, height in students.items():
    print(student, height)
```

### Working with Dictionary Values

The `.values()` method can be used to access only the stored values:

```python
heights = students.values()
```

This can be combined with functions such as `min()` and `max()`:

```python
shortest = min(students.values())
tallest = max(students.values())
```

## 🧩 Exercises

### 01. Student Height Analysis

Read the student number and height of ten students, then identify the tallest and shortest students.

**Concepts practiced:**

* Dictionaries
* `for` loops
* `.items()`
* `.values()`
* `min()`
* `max()`
* Conditional statements

**File:**

```text
student_height.py
```

## 🚀 Progression

The exercises in this section are part of my progression in Python fundamentals.

The goal is to gradually move from basic data structures to more practical applications involving **data manipulation and analysis**.

Later, these concepts will serve as a foundation for working with tools such as **Pandas**, where structured data is frequently represented and manipulated.

---

**Next step:** Continue practicing dictionaries with more complex data structures and combine them with functions, lists, and input validation.
