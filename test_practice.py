# Python Programming Basics

This repository contains simple Python functions that demonstrate fundamental programming concepts in Python. The project includes practice exercises covering conditionals, functions, loops, and basic algorithms, along with automated unit tests.

The goal of this repository is to practice writing clean Python code and verifying correctness using **unit testing**.

---

# Project Structure

```
project-folder/
│
├── practice_questions.py   # Main Python functions
├── test_practice.py        # Unit tests
└── README.md               # Project documentation
```

---

# Concepts Covered

The exercises demonstrate the following programming concepts:

* Conditional statements (`if`, `elif`, `else`)
* Functions
* Basic loops (`for`)
* String manipulation
* List operations
* Basic algorithms
* Unit testing using `unittest`

---

# Functions Overview

## 1. Check Even or Odd

Determines whether a number is even or odd.

Example:

```python
check_even(7)
```

Output:

```
Odd
```

---

## 2. Grade Score

Returns a grade based on a numeric score.

| Score Range | Grade |
| ----------- | ----- |
| 80+         | A     |
| 70–79       | B     |
| 60–69       | C     |
| 50–59       | D     |
| Below 50    | F     |

Example:

```python
grade_score(75)
```

Output:

```
B
```

---

## 3. Multiply Numbers

Returns the product of two numbers.

```python
multiply_numbers(4, 5)
```

Output:

```
20
```

---

## 4. Reverse String

Reverses a given string.

Example:

```python
reverse_string("hello")
```

Output:

```
olleh
```

---

## 5. Print Numbers

Prints numbers from `1` to `n`.

Example:

```python
print_numbers(3)
```

Output:

```
1
2
3
```

---

## 6. Sum Numbers

Returns the sum of numbers from `1` to `n`.

Example:

```python
sum_numbers(5)
```

Output:

```
15
```

---

## 7. Count Vowels

Counts the number of vowels in a string.

Example:

```python
count_vowels("hello")
```

Output:

```
2
```

---

## 8. Find Maximum Number

Finds the largest number in a list **without using `max()`**.

Example:

```python
find_max([3, 8, 2, 10, 5])
```

Output:

```
10
```

---

## 9. Palindrome Checker

Checks if a word reads the same forward and backward.

Example:

```python
is_palindrome("racecar")
```

Output:

```
True
```

---

## 10. Count Even Numbers

Counts how many even numbers exist in a list.

Example:

```python
count_even_numbers([1, 2, 3, 4, 6])
```

Output:

```
3
```

---

# Unit Testing

This project includes automated tests using Python's built-in **unittest** framework.

The tests verify that each function behaves correctly for different inputs.

Example test:

```python
def test_check_even(self):
    self.assertEqual(pq.check_even(4), "Even")
    self.assertEqual(pq.check_even(7), "Odd")
```

---

# Running the Tests

To run the unit tests:

```bash
python -m unittest test_practice.py
```

If all tests pass, you will see something like:

```
..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK
```

---

# Requirements

* Python 3.x
* No external libraries required (uses Python standard library only)

---

# How to Run the Project

1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

2. Navigate into the project folder

```bash
cd your-repository-name
```

3. Run the Python file or run the tests.

---

# Purpose of the Project

This project was created to practice:

* writing clean Python functions
* solving simple algorithm problems
* understanding loops and conditionals
* learning how to test code using `unittest`

---

# Author

Your Name

---

# License

This project is open source and available under the MIT License.
