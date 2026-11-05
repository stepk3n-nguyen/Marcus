"""
=============================================================================
ADVANCED LIST EXERCISES (LEVEL 3)
Target Audience: Marcus
Objective: Master data structures, recursion, chunking, custom sorting, and 2D matrix transformations.
=============================================================================
"""

# =============================================================================
# EXERCISE 11: DEEP FLATTEN ARBITRARILY NESTED LIST
# =============================================================================
# Given a deeply nested list with irregular structures:
nested_list = [1, [2, 3], [4, [5, 6, [7, 8]]], 9, [10]]

# Tasks:
# Implement a function `flatten(lst)` that recursively unpacks all inner lists
# and returns a flat 1D list:
# Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Hint: Use recursion combined with isinstance(item, list).

# --- Write your code below ---




# =============================================================================
# EXERCISE 12: TWO-SUM PROBLEM
# =============================================================================
# Given an integer list and a target sum:
nums = [2, 7, 11, 15, 3, 6]
target = 9

# Tasks:
# Find all pairs of indices (index1, index2) where index1 < index2 such that
# nums[index1] + nums[index2] == target.
# Expected pairs for target = 9:
# (0, 1) because nums[0] + nums[1] = 2 + 7 = 9
# (4, 5) because nums[4] + nums[5] = 3 + 6 = 9

# --- Write your code below ---




# =============================================================================
# EXERCISE 13: CHUNKING A LIST INTO GROUPS OF SIZE K
# =============================================================================
# Given a list and a desired chunk size:
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
chunk_size = 3

# Tasks:
# Implement a function `chunk_list(lst, k)` that partitions the list into sublists
# of at most k elements each.
# Expected output:
# [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100]]
# Hint: Use range(0, len(lst), k) with list slicing lst[i:i+k].

# --- Write your code below ---




# =============================================================================
# EXERCISE 14: MULTI-CRITERIA CUSTOM SORTING
# =============================================================================
# Given a list of tournament participants:
candidates = [
    {"name": "Marcus", "score": 88, "age": 16},
    {"name": "Alice",  "score": 95, "age": 15},
    {"name": "Bob",    "score": 88, "age": 14},
    {"name": "David",  "score": 95, "age": 16},
    {"name": "Emma",   "score": 82, "age": 17}
]

# Tasks:
# Sort the candidates using two priority levels:
# 1. Primary: Score in DESCENDING order (highest scores first).
# 2. Secondary: If scores are tied, Age in ASCENDING order (younger candidate first).
# Hint: Use sorted() or sort() with key=lambda x: (-x["score"], x["age"]).

# --- Write your code below ---




# =============================================================================
# EXERCISE 15: 2D MATRIX - TRANSPOSE & 90-DEGREE ROTATION
# =============================================================================
# Given a 3x3 square matrix:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Tasks:
# a) Transpose the matrix (swap rows and columns):
#    Expected output:
#    [ [1, 4, 7],
#      [2, 5, 8],
#      [3, 6, 9] ]
#    Hint: Use nested list comprehension or zip(*matrix).
#
# b) Rotate the matrix 90 degrees CLOCKWISE:
#    Expected output:
#    [ [7, 4, 1],
#      [8, 5, 2],
#      [9, 6, 3] ]
#    Hint: Rotating 90° clockwise = Transpose matrix, then reverse each row!

# --- Write your code below ---


