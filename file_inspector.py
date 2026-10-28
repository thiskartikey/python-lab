import pandas as pd

# Get CSV/TSV filename from user
csv_file = input("Enter CSV/TSV file name: ")

# Load dataset
dataset = pd.read_csv(csv_file)

# Display dataset summary
print("\nDataset:")
print(dataset)

print("\nRows and Columns:", dataset.shape)
print("\nData Types:")
print(dataset.dtypes)

# Filter rows based on user criteria
target_col = input("\nEnter column name for filtering: ")
min_threshold = float(input("Enter minimum value: "))

filtered_records = dataset[dataset[target_col] >= min_threshold]

# Display filtered results
print("\nFiltered Data:")
print(filtered_records)

# Export results to cleaned CSV
output_filename = "cleaned_data.csv"
filtered_records.to_csv(output_filename, index=False)
print(f"\nFiltered data saved as {output_filename}")
