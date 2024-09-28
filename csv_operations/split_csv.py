import pandas as pd

def split_csv(file_path, output_prefix):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Calculate the size of each split
    total_rows = len(df)
    split_size = total_rows // 3

    # Define the start and end index for each split
    splits = [
        (0, split_size),                             # First part
        (split_size, split_size * 2),                # Second part
        (split_size * 2, total_rows)                 # Third part
    ]

    # Iterate over each split and save as a separate CSV file
    for i, (start, end) in enumerate(splits):
        split_df = df[start:end]
        split_df.to_csv(f"{output_prefix}_part{i+1}.csv", index=False)
        print(f"Saved {output_prefix}_part{i+1}.csv with {len(split_df)} rows")

# Example usage
file_path = "D:/Study Material/Data_Management/GoalA/DBtrainrides.csv"
output_prefix = "split_file"
split_csv(file_path, output_prefix)
