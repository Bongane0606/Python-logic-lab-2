# 1. CONDITIONAL STATEMENTS
def check_even(number: int) -> str:
    """
    Return "Even" if the number is even,
    otherwise return "Odd".
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even(7))


# 2. CONDITIONAL STATEMENTS
def grade_score(score: int) -> str:
    """
    Return grades based on score:

    80+ -> "A"
    70-79 -> "B"
    60-69 -> "C"
    50-59 -> "D"
    below 50 -> "F"
    """
    if score < 50:
        return "F"
    elif 50 < score < 59:
        return "D"
    elif 60 < score < 69:
        return "C"
    elif 70 < score < 79:
        return "B"
    elif score > 80:
        return "A"



# 3. FUNCTIONS
def multiply_numbers(a: int, b: int) -> int:
    """
    Return the product of a and b.
    """
    return a * b


# 4. FUNCTIONS
def reverse_string(text: str) -> str:
    """
    Return the reversed version of the string.
    Example:
    "hello" -> "olleh"
    """
    return text[::-1]


# 5. BASIC LOOPS
def print_numbers(n: int):
    """
    Print numbers from 1 to n (inclusive)
    each on a new line.
    """
    total = 0
    for i in range(1, n + 1):
        total = total + 1
        print(i)


# 6. BASIC LOOPS
def sum_numbers(n: int) -> int:
    """
    Return the sum of numbers from 1 to n.
    Example:
    n=5 -> 15
    """
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total


# 7. ADVANCED LOOPS
def count_vowels(text: str) -> int:
    """
    Return the number of vowels in the string.
    Vowels: a, e, i, o, u (case insensitive)
    """
    vowels = "aeiouAEIOU"
    count = 0
    for i in text:
        if i in vowels:
            count = count + 1
    return count


# 8. ADVANCED LOOPS
def find_max(numbers: list) -> int:
    """
    Return the largest number in the list
    WITHOUT using max().
    """
    largest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
    return largest


# 9. SIMPLE ALGORITHMS
def is_palindrome(word: str) -> bool:
    """
    Return True if the word is a palindrome.

    Example:
    "racecar" -> True
    "hello" -> False
    """
    if word == word[::-1]:
        return True
    else:
        return False


# 10. SIMPLE ALGORITHMS
def count_even_numbers(numbers: list) -> int:
    """
    Return how many even numbers exist in the list.
    """
    total = 0
    for i in numbers:
        if i % 2 == 0:
            total = total + 1
    return total

