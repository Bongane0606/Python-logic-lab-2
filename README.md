# Python Programming Basics

This repository contains simple Python functions that demonstrate fundamental programming concepts. These exercises cover conditionals, functions, loops, and basic algorithms.

The project is designed for beginners who are learning Python and want to understand how common programming patterns work.

---

## Concepts Covered

The code examples in this repository demonstrate:

* Conditional statements (`if`, `elif`, `else`)
* Functions
* Basic loops (`for`)
* Working with strings
* Working with lists
* Basic algorithms

---

# Functions Overview

## 1. Check Even or Odd

Determines whether a number is even or odd.

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
print_numbers(5)
```

Output:

```
1
2
3
4
5
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
count_vowels("Hello World")
```

Output:

```
3
```

---

## 8. Find Maximum Number

Finds the largest number in a list **without using `max()`**.

Example:import unittest
import practice_questions as pq
from io import StringIO
import sys


class TestPracticeQuestions(unittest.TestCase):

    # 1
    def test_check_even(self):
        self.assertEqual(pq.check_even(4), "Even")
        self.assertEqual(pq.check_even(7), "Odd")

    # 2
    def test_grade_score(self):
        self.assertEqual(pq.grade_score(85), "A")
        self.assertEqual(pq.grade_score(72), "B")
        self.assertEqual(pq.grade_score(65), "C")
        self.assertEqual(pq.grade_score(55), "D")
        self.assertEqual(pq.grade_score(30), "F")

    # 3
    def test_multiply_numbers(self):
        self.assertEqual(pq.multiply_numbers(3, 4), 12)
        self.assertEqual(pq.multiply_numbers(5, 2), 10)

    # 4
    def test_reverse_string(self):
        self.assertEqual(pq.reverse_string("hello"), "olleh")
        self.assertEqual(pq.reverse_string("python"), "nohtyp")

    # 5
    def test_print_numbers(self):
        captured = StringIO()
        sys.stdout = captured

        pq.print_numbers(3)

        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue().strip().split("\n"), ["1", "2", "3"])

    # 6
    def test_sum_numbers(self):
        self.assertEqual(pq.sum_numbers(5), 15)
        self.assertEqual(pq.sum_numbers(3), 6)

    # 7
    def test_count_vowels(self):
        self.assertEqual(pq.count_vowels("hello"), 2)
        self.assertEqual(pq.count_vowels("Python"), 1)

    # 8
    def test_find_max(self):
        self.assertEqual(pq.find_max([1, 5, 2, 9, 3]), 9)
        self.assertEqual(pq.find_max([10, 20, 5]), 20)

    # 9
    def test_is_palindrome(self):
        self.assertTrue(pq.is_palindrome("racecar"))
        self.assertFalse(pq.is_palindrome("hello"))

    # 10
    def test_count_even_numbers(self):
        self.assertEqual(pq.count_even_numbers([1, 2, 3, 4, 6]), 3)
        self.assertEqual(pq.count_even_numbers([1, 3, 5]), 0)


if __name__ == "__main__":
    unittest.main()

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

## 10. Count Even Numbers in a List

Counts how many even numbers exist in a list.

Example:

```python
count_even_numbers([1, 2, 3, 4, 5, 6])
```

Output:

```
3
```

---

# How to Run the Code

1. Install Python (version 3.x recommended)
2. Clone the repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

3. Navigate to the folder

```bash
cd your-repository-name
```

4. Run the Python file

```bash
python filename.py
```

---

# Purpose

This project was created to practice and demonstrate basic Python programming concepts. It can be useful for beginners who are learning:

* problem solving
* writing clean functions
* understanding loops and conditionals

---

# Author

Name : Letsoenyo Clen Bongane

---

# License

This project is open source and available under the MIT License.
