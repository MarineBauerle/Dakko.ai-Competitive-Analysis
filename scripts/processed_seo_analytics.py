import pandas as pd

# Read the CSV file with semicolon as delimiter
df = pd.read_csv('1backlinks.csv', delimiter=';')

# Define a function to convert values with 'K' and 'M' to integers
def convert_to_int(value):
    if isinstance(value, str):  # Check if the value is a string
        if 'K' in value:
            return int(float(value.replace('K', '')) * 1e3)  # Convert 'K' to a thousand
        elif 'M' in value:
            return int(float(value.replace('M', '')) * 1e6)  # Convert 'M' to a million
    return value

# Apply the function to each column in the dataframe
for col in df.columns:
    df[col] = df[col].apply(convert_to_int)

# Save the modified dataframe back to a CSV file with semicolon as delimiter
df.to_csv('1backlinks_modified.csv', sep=';', index=False)
