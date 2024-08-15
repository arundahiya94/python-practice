import pandas as pd
import numpy as np

# Step 1: Read the original CSV file
original_csv = 'DBtrainrides.csv'
df = pd.read_csv(original_csv)

# Step 2: Determine how to split the data
# In this example, we split the DataFrame into three equal parts (or nearly equal if not divisible by 3)
df_split = np.array_split(df, 3)

# Step 3: Save the split DataFrames to new CSV files
for i, chunk in enumerate(df_split):
    chunk.to_csv(f'output_part_{i+1}.csv', index=False)

print("CSV file split into 3 parts successfully!")