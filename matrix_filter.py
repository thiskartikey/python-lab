# Remove negative values from each row using filter()
def filter_negative(data_grid):
    return [list(filter(lambda num: num >= 0, row)) for row in data_grid]

# Square every element in the grid using map()
def square_matrix(data_grid):
    return [list(map(lambda val: val * val, row)) for row in data_grid]

# Sort each row in ascending order
def sort_rows(data_grid):
    return [sorted(row) for row in data_grid]

# Sort matrix rows according to row sum
def sort_by_sum(data_grid):
    return sorted(data_grid, key=lambda row: sum(row))

# Convert each row list into an immutable tuple
def convert_to_tuples(data_grid):
    return [tuple(row) for row in data_grid]

# Main demonstration matrix
grid = [
    [5, -2, 8, 1],
    [-4, 7, 3, -1],
    [9, 2, -6, 4]
]

print("Original Matrix:")
print(grid)

# Step 1: Remove negative values
filtered_grid = filter_negative(grid)
print("\nAfter Filtering Negative Values:")
print(filtered_grid)

# Step 2: Square remaining positive numbers
squared_grid = square_matrix(filtered_grid)
print("\nAfter Squaring Elements:")
print(squared_grid)

# Step 3: Sort each row
sorted_grid = sort_rows(squared_grid)
print("\nRows Sorted in Ascending Order:")
print(sorted_grid)

# Step 4: Sort rows according to their sum
ordered_grid = sort_by_sum(sorted_grid)
print("\nRows Sorted According to Their Sum:")
print(ordered_grid)

# Step 5: Convert rows into tuples
tuple_grid = convert_to_tuples(ordered_grid)
print("\nFinal Matrix as Tuples:")
print(tuple_grid)
