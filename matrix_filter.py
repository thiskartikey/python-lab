def filter_negative(data_grid):
    return [list(filter(lambda num: num >= 0, row)) for row in data_grid]

def square_matrix(data_grid):
    return [list(map(lambda val: val * val, row)) for row in data_grid]

def sort_rows(data_grid):
    return [sorted(row) for row in data_grid]

def sort_by_sum(data_grid):
    return sorted(data_grid, key=lambda row: sum(row))

def convert_to_tuples(data_grid):
    return [tuple(row) for row in data_grid]

grid = [
    [5, -2, 8, 1],
    [-4, 7, 3, -1],
    [9, 2, -6, 4]
]

print("Original Matrix:")
print(grid)

filtered_grid = filter_negative(grid)
print("\nAfter Filtering Negative Values:")
print(filtered_grid)

squared_grid = square_matrix(filtered_grid)
print("\nAfter Squaring Elements:")
print(squared_grid)

sorted_grid = sort_rows(squared_grid)
print("\nRows Sorted in Ascending Order:")
print(sorted_grid)

ordered_grid = sort_by_sum(sorted_grid)
print("\nRows Sorted According to Their Sum:")
print(ordered_grid)

tuple_grid = convert_to_tuples(ordered_grid)
print("\nFinal Matrix as Tuples:")
print(tuple_grid)
