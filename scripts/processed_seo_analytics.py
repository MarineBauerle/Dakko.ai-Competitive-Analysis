import pandas as pd

# Read the CSV file with semicolon as delimiter
df = pd.read_csv('seo_analytics.csv', delimiter=';')

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
df.to_csv('processed_seo_analytics.csv', sep=';', index=False)


### The Python script displayed in the image is designed to manipulate and clean a CSV file containing SEO analytics data. Here's a breakdown of its functionality:

1. Import Pandas Library: The script starts by importing the pandas library, which is essential for data manipulation and analysis in Python.

2. Read the CSV File: It reads a CSV file named 'seo_analytics.csv' using pandas. The delimiter specified is a semicolon (`;`), indicating that the data fields in the CSV are separated by semicolons.

3. Define a Conversion Function: A function named `convert_to_int` is defined to convert string values that contain shorthand for thousands ('K') and millions ('M') into their full numeric equivalents. It checks if the value is a string and contains 'K' or 'M', replacing these characters with an empty string and then converting the result to an integer, multiplying by 1,000 for 'K' or 1,000,000 for 'M'.

4. Apply the Conversion Function: This function is applied across all columns in the data frame. It iterates over each column, applying the `convert_to_int` function to each value. This suggests that the dataset may contain numeric values represented as strings with 'K' or 'M' suffixes, which this script converts to an integer representation.

5. Save the Processed Data: After converting all the relevant values, the script saves the modified data frame back to a new CSV file named 'processed_seo_analytics.csv', using a semicolon as the delimiter and not writing the index into the file.

This script is useful for preprocessing SEO data, particularly in making the data easier to analyze numerically by converting shorthand notations to actual numbers. This preprocessing step would be essential before performing any sort of quantitative analysis, as it ensures that all numeric data is in a consistent format.
