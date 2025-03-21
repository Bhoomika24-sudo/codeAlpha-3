import pandas as pd
import os

def clean_csv(file_path, output_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Fill missing values (you can customize this method)
    df.fillna(method='ffill', inplace=True)  # Forward fill

    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Save the cleaned DataFrame to a new CSV file
    df.to_csv(output_path, index=False)
    print(f'Cleaned data saved to: {output_path}')

if __name__ == "__main__":
    # Specify the directory containing CSV files
    input_directory = input("Enter the path of the directory containing CSV files: ")
    output_directory = input("Enter the path of the directory to save cleaned files: ")

    # Ensure output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Process each CSV file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.csv'):
            input_file_path = os.path.join(input_directory, filename)
            output_file_path = os.path.join(output_directory, f'cleaned_{filename}')
            clean_csv(input_file_path, output_file_path)