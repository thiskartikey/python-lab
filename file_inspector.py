import pandas as pd

csv_file = input("Enter CSV/TSV file name: ")
dataset = pd.read_csv(csv_file)

print("\nDataset:")
print(dataset)

print("\nRows and Columns:", dataset.shape)
print("\nData Types:")
print(dataset.dtypes)

target_col = input("\nEnter column name for filtering: ")
min_threshold = float(input("Enter minimum value: "))

filtered_records = dataset[dataset[target_col] >= min_threshold]

print("\nFiltered Data:")
print(filtered_records)

output_filename = "cleaned_data.csv"
filtered_records.to_csv(output_filename, index=False)
print(f"\nFiltered data saved as {output_filename}")
