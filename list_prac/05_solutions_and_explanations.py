"""
=============================================================================
REFERENCE SOLUTIONS & STEP-BY-STEP EXPLANATIONS (ALL EXERCISES)
Target Audience: Marcus
Recommendation: Review only after attempting the problems yourself!
=============================================================================
"""

def print_separator(title):
    print(f"\n{'='*20} {title} {'='*20}")


# =============================================================================
# LEVEL 1: BASIC EXERCISE SOLUTIONS
# =============================================================================

def solve_level_1():
    print_separator("LEVEL 1: BASIC EXERCISES")

    # --- EXERCISE 1 ---
    print("\n[EXERCISE 1: CREATION, INDEXING & SLICING]")
    animals = ["dog", "cat", "rabbit", "tiger", "bear", "lion", "squirrel"]
    print("a. First:", animals[0], "| Last:", animals[-1])
    print("b. Middle 3 animals (index 2..4):", animals[2:5])
    animals[1] = "leopard"
    print("c. After updating 'cat' -> 'leopard':", animals)
    print("d. Reversed list:", animals[::-1])

    # --- EXERCISE 2 ---
    print("\n[EXERCISE 2: ADDING AND EXTENDING ELEMENTS]")
    numbers = [10, 20, 30]
    numbers.append(40)          # [10, 20, 30, 40]
    numbers.insert(1, 15)       # [10, 15, 20, 30, 40]
    numbers.extend([50, 60])    # [10, 15, 20, 30, 40, 50, 60]
    print("List after append, insert, and extend:", numbers)

    # --- EXERCISE 3 ---
    print("\n[EXERCISE 3: REMOVING AND POPPING ELEMENTS]")
    cart = ["book", "pencil", "eraser", "pen", "ruler", "pencil", "backpack"]
    cart.remove("eraser")
    last_item = cart.pop()      # "backpack"
    print("Popped last item:", last_item)
    first_item = cart.pop(0)    # "book"
    print("Popped first item:", first_item)
    del cart[1]                 # Deletes item at index 1
    print("Remaining cart:", cart)

    # --- EXERCISE 4 ---
    print("\n[EXERCISE 4: SEARCHING AND FREQUENCY COUNTING]")
    grades = [8, 9, 7, 10, 6, 8, 9, 8, 10, 5, 8]
    print("Did anyone score 4?", 4 in grades)
    print("Number of students scoring 8:", grades.count(8))
    print("First index of score 10:", grades.index(10))
    print("Total number of graded exams:", len(grades))

    # --- EXERCISE 5 ---
    print("\n[EXERCISE 5: SUMMARY STATS AND SORTING]")
    temperatures = [28.5, 30.0, 27.2, 32.5, 29.8, 31.0, 26.5]
    print("Max temp:", max(temperatures), "| Min temp:", min(temperatures))
    avg_temp = round(sum(temperatures) / len(temperatures), 2)
    print("Average temperature:", avg_temp)
    sorted_temps = sorted(temperatures)
    print("New sorted list (ascending):", sorted_temps)
    temperatures.sort(reverse=True)
    print("Original list sorted in-place (descending):", temperatures)


# =============================================================================
# LEVEL 2: INTERMEDIATE EXERCISE SOLUTIONS
# =============================================================================

def solve_level_2():
    print_separator("LEVEL 2: INTERMEDIATE EXERCISES")

    # --- EXERCISE 6 ---
    print("\n[EXERCISE 6: CATEGORIZING & FILTERING]")
    raw_numbers = [12, -7, 0, 15, -3, 28, 41, -10, 8, 0, 33]
    positives = [x for x in raw_numbers if x > 0]
    negatives = [x for x in raw_numbers if x < 0]
    positive_evens = [x for x in raw_numbers if x > 0 and x % 2 == 0]
    print("Positives:", positives)
    print("Negatives:", negatives)
    print("Positive evens:", positive_evens)

    # --- EXERCISE 7 ---
    print("\n[EXERCISE 7: REMOVE DUPLICATES PRESERVING ORDER]")
    views = ["SKU01", "SKU03", "SKU02", "SKU01", "SKU04", "SKU03", "SKU05", "SKU02"]
    # Method 1: Iterative check
    unique_views = []
    for item in views:
        if item not in unique_views:
            unique_views.append(item)
    print("Method 1 (Loop):", unique_views)
    # Method 2: dict.fromkeys() (Preserves insertion order in Python 3.7+)
    unique_views_dict = list(dict.fromkeys(views))
    print("Method 2 (dict.fromkeys):", unique_views_dict)

    # --- EXERCISE 8 ---
    print("\n[EXERCISE 8: ROTATE LIST]")
    items = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    # Slicing the last k elements and prepending them
    k = k % len(items)  # Handle edge cases where k > length
    rotated = items[-k:] + items[:-k]
    print(f"List after rotating right by {k} positions:", rotated)

    # --- EXERCISE 9 ---
    print("\n[EXERCISE 9: NESTED LISTS & 2D TABLE DATA]")
    class_scores = [
        [8.5, 7.0, 9.0],
        [6.0, 8.0, 7.5],
        [9.5, 9.0, 9.0]
    ]
    print("Student 0 English score:", class_scores[0][2])
    for i, student in enumerate(class_scores):
        gpa = sum(student) / len(student)
        print(f"Student {i}: GPA = {gpa:.2f}")
    math_scores = [student[0] for student in class_scores]
    avg_math = sum(math_scores) / len(math_scores)
    print(f"Class average for Math: {avg_math:.2f}")

    # --- EXERCISE 10 ---
    print("\n[EXERCISE 10: LIST COMPREHENSION]")
    cities = ["   new york  ", "san FRANCISCO", "tokyo", "PARIS   ", "london"]
    cleaned = [c.strip().title() for c in cities]
    print("Cleaned city names:", cleaned)
    longer_than_5 = [c for c in cleaned if len(c) > 5]
    print("Cities with length > 5:", longer_than_5)


# =============================================================================
# LEVEL 3: ADVANCED EXERCISE SOLUTIONS
# =============================================================================

def solve_level_3():
    print_separator("LEVEL 3: ADVANCED EXERCISES")

    # --- EXERCISE 11 ---
    print("\n[EXERCISE 11: DEEP FLATTEN ARBITRARILY NESTED LIST]")
    nested_list = [1, [2, 3], [4, [5, 6, [7, 8]]], 9, [10]]
    def flatten(lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))  # Recursive unpack
            else:
                result.append(item)
        return result
    print("Deeply flattened list:", flatten(nested_list))

    # --- EXERCISE 12 ---
    print("\n[EXERCISE 12: TWO-SUM PROBLEM]")
    nums = [2, 7, 11, 15, 3, 6]
    target = 9
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((i, j))
    print(f"Index pairs summing to {target}:", pairs)

    # --- EXERCISE 13 ---
    print("\n[EXERCISE 13: CHUNKING A LIST]")
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    chunk_size = 3
    def chunk_list(lst, k):
        return [lst[i:i + k] for i in range(0, len(lst), k)]
    print(f"Partitioned list into chunks of size {chunk_size}:")
    print(chunk_list(data, chunk_size))

    # --- EXERCISE 14 ---
    print("\n[EXERCISE 14: MULTI-CRITERIA CUSTOM SORTING]")
    candidates = [
        {"name": "Marcus", "score": 88, "age": 16},
        {"name": "Alice",  "score": 95, "age": 15},
        {"name": "Bob",    "score": 88, "age": 14},
        {"name": "David",  "score": 95, "age": 16},
        {"name": "Emma",   "score": 82, "age": 17}
    ]
    # Primary: -score (descending), Secondary: age (ascending)
    sorted_candidates = sorted(candidates, key=lambda x: (-x["score"], x["age"]))
    print("Tournament Ranking:")
    for rank, c in enumerate(sorted_candidates, 1):
        print(f"Rank {rank}: {c['name']} | Score: {c['score']} | Age: {c['age']}")

    # --- EXERCISE 15 ---
    print("\n[EXERCISE 15: 2D MATRIX - TRANSPOSE & 90-DEGREE ROTATION]")
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    # a. Transpose
    transposed = [[row[col] for row in matrix] for col in range(len(matrix[0]))]
    print("Transposed Matrix:")
    for r in transposed:
        print(r)

    # b. 90-degree clockwise rotation (reverse each row of transposed matrix)
    rotated_90 = [row[::-1] for row in transposed]
    print("Matrix after 90° clockwise rotation:")
    for r in rotated_90:
        print(r)


if __name__ == "__main__":
    solve_level_1()
    solve_level_2()
    solve_level_3()

