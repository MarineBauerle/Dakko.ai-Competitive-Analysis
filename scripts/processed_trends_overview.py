import pandas as pd

# Function to load data
def load_data(filepath):
    # Read the file as a list of lines
    with open(filepath, 'r') as f:
        lines = f.readlines()

    # Join broken lines based on the quotes and semi-colons
    reconstructed_lines = []
    temp_line = ""
    for line in lines:
        temp_line += line.strip()
        if temp_line.count('"') % 2 == 0:  # If even quotes, the line is complete
            reconstructed_lines.append(temp_line)
            temp_line = ""

    # Convert the reconstructed lines back to a CSV string and then to a dataframe
    csv_string = '\n'.join(reconstructed_lines)
    from io import StringIO
    return pd.read_csv(StringIO(csv_string), delimiter=';')

# Function to handle K and M formats
def convert_k_m(value):
    if 'K' in value:
        return float(value.replace('K', '')) * 1e3
    elif 'M' in value:
        return float(value.replace('M', '')) * 1e6
    else:
        return float(value)


# Convert 'mm:ss' format 
def convert_duration_to_seconds(value):
    try:
        minutes, seconds = value.split(":")
        return f"{int(minutes):02d}:{int(seconds):02d}"
    except:
        return "00:00"


# Clean data function
def clean_data(df):
    # Handle different formats
    df['Visits'] = df['Visits'].apply(convert_k_m)
    df['Unique Visitors'] = df['Unique Visitors'].apply(convert_k_m)
    df['Bounce Rate'] = df['Bounce Rate'].str.rstrip('%').astype(float) / 100.0
    
    # Convert Avg. Visit Duration to total seconds
    df['Avg. Visit Duration'] = df['Avg. Visit Duration'].apply(convert_duration_to_seconds)
    
    return df

# Main function
if __name__ == "__main__":
    filepath = 'trends_overview_sep23.csv'
    data = load_data(filepath)

    print("Columns in the loaded dataframe:", data.columns)
    cleaned_data = clean_data(data)
    print(cleaned_data)

    cleaned_data.to_csv('processed_trends.csv', index=False)



### This Python script is a data-cleaning utility designed for processing CSV files with specific formatting issues and converting various data representations into a uniform format for easier analysis. 
Here's a step-by-step description of the script:

1. Import pandas: The script imports the pandas library, which is used for handling and manipulating data structures and performing data analysis in Python.

2. Load Data Function (`load_data`):
   - It defines a function to read a CSV file where lines may be broken across multiple lines.
   - The function reads the file into a list of strings, ensuring that lines broken by newlines but contained within quotes are reconstructed into complete lines.
   - These complete lines are then joined into a single string representing the CSV data.
   - The string is converted back into a pandas DataFrame, using a semicolon (`;`) as the delimiter.

3. Convert K and M Function (`convert_k_m`):
   - This function converts strings containing 'K' (thousands) and 'M' (millions) to their numeric equivalents.

4. Convert Duration to Seconds (`convert_duration_to_seconds`):
   - It takes a string in 'mm:ss' format and converts it to a formatted string representation with leading zeros if needed.
   - In case of an error (likely due to incorrect formatting), it returns "00:00".

5. Clean Data Function (`clean_data`):
   - This function applies the previously defined conversion functions to specific columns (e.g., 'Visits', 'Unique Visitors').
   - It also processes the 'Bounce Rate' column by stripping the percentage sign and converting the values into a float representation.
   - The 'Avg. Visit Duration' column is converted to a standardized duration format.

6. Main Execution Block:
   - If the script is run directly (not imported as a module), it will execute the code in this block.
   - It calls the `load_data` function to load the data from 'trends_overview_sep23.csv'.
   - It prints out the column names of the loaded data frame.
   - It then calls the `clean_data` function to clean the loaded data.
   - Finally, it prints the cleaned data and saves it to 'processed_trends.csv' without the index.

Overall, the script is structured to handle specific data cleaning tasks and ensure that the CSV data is in a consistent and analyzable format, particularly for fields with non-standard numeric representations and time durations. This cleaned data can then be used for further analysis or visualization tasks.
