import os
import pandas as pd
from datetime import datetime

# Function to convert BLG to CSV based on file type
def blg_to_csv(input_folder, output_folder, file_type):
    for file in os.listdir(input_folder):
        if file.endswith(f"_{file_type}.blg"):
            df = pd.read_csv(os.path.join(input_folder, file), delimiter='\t')
            csv_filename = os.path.splitext(file)[0] + ".csv"
            df.to_csv(os.path.join(output_folder, csv_filename), index=False)

# Function to remove holiday and weekend data, and filter time range
def preprocess_data(csv_folder):
    df_list = []
    for file in os.listdir(csv_folder):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(csv_folder, file))
            
            # Convert timestamp column to datetime
            df['Timestamp'] = pd.to_datetime(df['Timestamp'])
            
            # Remove holiday data (assuming holidays is a list of datetime objects)
            holidays = [datetime(2024, 2, 1)]  # Example: New Year's Day
            df = df[~df['Timestamp'].dt.date.isin(holidays)]
            
            # Remove weekend data (Saturday: 5, Sunday: 6)
            df = df[df['Timestamp'].dt.weekday < 5]
            
            # Filter time range (8:30 to 17:15)
            df = df[(df['Timestamp'].dt.time >= datetime.strptime('08:30', '%H:%M').time()) &
                    (df['Timestamp'].dt.time <= datetime.strptime('17:15', '%H:%M').time())]
            
            df_list.append(df)
    
    merged_df = pd.concat(df_list, ignore_index=True)
    return merged_df

# Function to merge CSV files
def merge_csv_files(csv_folder):
    df_list = []
    for file in os.listdir(csv_folder):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(csv_folder, file))
            df_list.append(df)
    
    merged_df = pd.concat(df_list, ignore_index=True)
    return merged_df

# Main function
def main():
    input_folder = ["C:\Users\Ariake\Desktop\full-02\20240304\AP-FOLDER\AP",
                    "C:\Users\Ariake\Desktop\full-02\20240304\DB-FOLDER\DB",
                    "C:\Users\Ariake\Desktop\full-02\20240304\DB-FOLDER\FL"]
    csv_output_folder = "C:\Users\Ariake\Desktop\full-02\20240304"
    
    # Convert BLG to CSV for CPU data
    blg_to_csv(input_folder, csv_output_folder, "cpu")
    
    # Convert BLG to CSV for Memory data
    blg_to_csv(input_folder, csv_output_folder, "mem")
    
    # Convert BLG to CSV for Network data
    blg_to_csv(input_folder, csv_output_folder, "net")

    # Merge CSV files
    merged_df = merge_csv_files(csv_output_folder)
    
    # Preprocess data
    preprocessed_df = preprocess_data(csv_output_folder)
    
    # Export preprocessed data to CSV
    preprocessed_df.to_csv("preprocessed_data.csv", index=False)
    print("Preprocessed data saved to preprocessed_data.csv")

if __name__ == "__main__":
    main()
