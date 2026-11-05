"""
=============================================================================
INTERMEDIATE LIST EXERCISES (LEVEL 2)
Target Audience: Marcus
Objective: Build algorithmic logic, filtering, list comprehension, and multi-dimensional lists.
=============================================================================
"""

# =============================================================================
# EXERCISE 6: CATEGORIZING & FILTERING NUMBERS
# =============================================================================
# Given a mixed list of integers:
raw_numbers = [12, -7, 0, 15, -3, 28, 41, -10, 8, 0, 33]

# Tasks:
# a) Create a list `positives` containing all positive numbers (> 0).
# b) Create a list `negatives` containing all negative numbers (< 0).
# c) Create a list `positive_evens` containing only positive even numbers.
# (Marcus, try solving this using both standard for-loops and List Comprehensions).

# --- Write your code below ---




# =============================================================================
# EXERCISE 7: REMOVE DUPLICATES WHILE PRESERVING ORDER
# =============================================================================
# Given a list of product codes browsed by a user:
views = ["SKU01", "SKU03", "SKU02", "SKU01", "SKU04", "SKU03", "SKU05", "SKU02"]

# Tasks:
# Create a new list `unique_views` with duplicates removed while maintaining
# the exact original order of first appearance.
# Note: list(set(views)) will scramble the order! Try using a loop or dict.fromkeys().
# Expected output: ['SKU01', 'SKU03', 'SKU02', 'SKU04', 'SKU05']

# --- Write your code below ---




# =============================================================================
# EXERCISE 8: ROTATE LIST TO THE RIGHT BY K POSITIONS
# =============================================================================
# Given a list of elements and an integer k:
numbers = [1, 2, 3, 4, 5, 6, 7]
k = 3

# Tasks:
# Rotate the list to the right by k positions.
# Rotating by 1: [7, 1, 2, 3, 4, 5, 6]
# Rotating by 3: [5, 6, 7, 1, 2, 3, 4]
# Hint: Solve this cleanly using list slicing (numbers[-k:] and numbers[:-k]).
# Make sure to handle edge cases where k > len(numbers) using k % len(numbers).

# --- Write your code below ---




# =============================================================================
# EXERCISE 9: NESTED LISTS & 2D TABLE DATA
# =============================================================================
# Given the grade table of 3 students across 3 subjects (Math, Literature, English):
class_scores = [
    [8.5, 7.0, 9.0],  # Student 0
    [6.0, 8.0, 7.5],  # Student 1
    [9.5, 9.0, 9.0]   # Student 2
]

# Tasks:
# a) Print Student 0's English score (row 0, column index 2).
# b) Compute and print each student's GPA in the format:
#    "Student 0: GPA = 8.17"
# c) Calculate the overall class average for Math (column index 0).

# --- Write your code below ---




# =============================================================================
# EXERCISE 10: PRACTICAL LIST COMPREHENSION
# =============================================================================
# Given a list of unformatted city names:
cities = ["   new york  ", "san FRANCISCO", "tokyo", "PARIS   ", "london"]

# Tasks (use List Comprehension):
# a) Clean up the data: strip leading/trailing whitespace (.strip()) and
#    convert to Title Case (.title()).
#    Expected: ['New York', 'San Francisco', 'Tokyo', 'Paris', 'London']
# b) From the cleaned list, extract only city names with more than 5 characters.

# --- Write your code below ---


