# ======================= To change csv col name using python ========================

import pandas as pd

# Read the CSV file
df = pd.read_csv('fl-combine-net.csv', encoding_errors="ignore", low_memory=False)

# Rename col
df= df.rename(columns={'(PDH-CSV 4.0) (Tokyo Standard Time)(-540)':'DateTime'})
df= df.rename(columns={r'\\20SVNN\Network Interface(HPE Ethernet 1Gb 4-port 366FLR Adapter)\Bytes Total/sec':'bytes total'})

# Save the modified DataFrame back to a new CSV file or overwrite the existing one
output_file_path = 'fl-combine-net-col.csv'  
df.to_csv(output_file_path, index=False)

#Delete unnecessary columns
excel_file_path = 'fl-combine-net-col.csv'  # Replace with the path to your Excel file
df = pd.read_csv(excel_file_path, encoding_errors='ignore')

df=df[df.columns[df.columns.isin(['DateTime','bytes total'])]]
df.to_csv('fl-combine-net-col-col-d.csv', index=False)