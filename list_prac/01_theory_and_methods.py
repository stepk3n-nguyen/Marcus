"""
=============================================================================
THEORY & COMPREHENSIVE GUIDE: PYTHON LISTS IN DEPTH
Target Audience: Marcus
Objective: Master Python list fundamentals, CRUD operations, and built-in methods.
=============================================================================
"""

def main():
    print("--- 1. INITIALIZATION & LIST CHARACTERISTICS ---")
    # A Python list is: ordered, mutable, permits duplicates, and can hold mixed data types.
    empty_list = []
    fruits = ["apple", "banana", "orange", "mango", "watermelon"]
    mixed_list = [10, "Python", 3.14, True, [1, 2]]
    print("Fruit list:", fruits)
    print("Length (number of items):", len(fruits))


    print("\n--- 2. INDEXING & SLICING ---")
    # Positive index: 0, 1, 2, ... (left-to-right)
    # Negative index: -1, -2, -3, ... (right-to-left)
    print("First element (fruits[0]):", fruits[0])
    print("Last element (fruits[-1]):", fruits[-1])

    # Slicing syntax: list[start:stop:step] (from start up to stop - 1)
    print("Items from index 1 to 3 (fruits[1:4]):", fruits[1:4])
    print("First 3 items (fruits[:3]):", fruits[:3])
    print("From index 2 to end (fruits[2:]):", fruits[2:])
    print("Every 2nd item (step=2, fruits[::2]):", fruits[::2])
    print("Reversed list (fruits[::-1]):", fruits[::-1])


    print("\n--- 3. MUTABILITY & UPDATING ELEMENTS ---")
    colors = ["red", "green", "blue"]
    print("Initial list:", colors)
    colors[1] = "yellow"  # Modifying item at index 1
    print("After changing index 1 to 'yellow':", colors)


    print("\n--- 4. ADDING ELEMENTS (CREATE) ---")
    numbers = [1, 2, 3]

    # append(x): Adds a single item to the end
    numbers.append(4)
    print("After append(4):", numbers)

    # insert(index, x): Inserts an item at a specific position
    numbers.insert(1, 99)
    print("After insert(1, 99):", numbers)

    # extend(iterable): Appends elements from another iterable to the end
    numbers.extend([100, 200])
    print("After extend([100, 200]):", numbers)

    # Concatenation (+) and Repetition (*) operators
    merged = [1, 2] + [3, 4]
    zeros = [0] * 5
    print("Concatenation (+):", merged)
    print("Repetition (*) [0] * 5:", zeros)


    print("\n--- 5. REMOVING ELEMENTS (DELETE) ---")
    items = ["A", "B", "C", "B", "D", "E"]
    print("Initial list:", items)

    # remove(x): Removes the FIRST occurrence of value x
    items.remove("B")
    print("After remove('B'):", items)

    # pop(index): Removes and RETURNS item at index (defaults to last element)
    last_item = items.pop()
    print(f"After pop() returned '{last_item}':", items)
    first_item = items.pop(0)
    print(f"After pop(0) returned '{first_item}':", items)

    # del: Deletes an item or slice by index
    del items[1]
    print("After del items[1]:", items)

    # clear(): Removes all elements
    temp = [1, 2, 3]
    temp.clear()
    print("After clear():", temp)


    print("\n--- 6. SEARCHING, COUNTING & MEMBERSHIP ---")
    scores = [10, 8, 9, 8, 7, 8, 6]
    print("Scores list:", scores)

    # in / not in: Membership test operators
    print("Is 10 in scores?", 10 in scores)
    print("Is 5 in scores?", 5 in scores)

    # count(x): Counts occurrences of value x
    print("Occurrences of 8 (scores.count(8)):", scores.count(8))

    # index(x): Returns first index of value x (raises ValueError if not found)
    print("First index of 9 (scores.index(9)):", scores.index(9))


    print("\n--- 7. SORTING & REVERSING ---")
    nums = [45, 12, 89, 3, 27]
    print("Original numbers:", nums)

    # sort(): Modifies list in-place
    nums.sort()
    print("After sort() (ascending):", nums)
    nums.sort(reverse=True)
    print("After sort(reverse=True) (descending):", nums)

    # sorted(): Returns a NEW sorted list without modifying the original
    raw = [5, 2, 9, 1]
    sorted_copy = sorted(raw)
    print("Original raw list:", raw)
    print("Result of sorted(raw):", sorted_copy)

    # reverse(): Reverses list elements in-place
    nums.reverse()
    print("After reverse():", nums)


    print("\n--- 8. AGGREGATION & SUMMARY FUNCTIONS ---")
    vals = [15, 30, 5, 50]
    print("Values list:", vals)
    print("Length len():", len(vals))
    print("Minimum min():", min(vals))
    print("Maximum max():", max(vals))
    print("Total sum():", sum(vals))
    print("Average:", sum(vals) / len(vals))


    print("\n--- 9. SHALLOW VS DEEP COPYING ---")
    # WARNING: Simple assignment (b = a) creates an alias, NOT a copy!
    a = [1, 2, 3]
    b = a
    b.append(99)
    print("Modifying alias 'b' also changes 'a':", a)

    # Safe copying methods for 1D lists: .copy(), list(a), or a[:]
    orig = [1, 2, 3]
    safe_copy = orig.copy()
    safe_copy.append(999)
    print("Original list remained untouched:", orig)
    print("Independent safe copy:", safe_copy)


    print("\n--- 10. LIST COMPREHENSION ---")
    # Syntax: [expression for item in iterable if condition]
    # Example 1: Squares of numbers 1 through 5
    squares = [x**2 for x in range(1, 6)]
    print("Squares 1..5:", squares)

    # Example 2: Filtering even numbers
    evens = [x for x in range(10) if x % 2 == 0]
    print("Even numbers < 10:", evens)

    # Example 3: String transformation
    words = ["hello", "python", "marcus"]
    caps = [w.upper() for w in words]
    print("Uppercase strings:", caps)

if __name__ == "__main__":
    main()

