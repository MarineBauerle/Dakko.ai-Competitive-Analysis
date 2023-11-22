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
