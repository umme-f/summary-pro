import os
import glob
import pandas as pd
folder = r"C:\Users\Ariake\Desktop\full-02"
# Set the path to the folder containing CSV files
for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            if 'cpu' in filename.lower():
                combine_cpu=pd.concat([pd.read_csv(filename, encoding_errors='ignore')])
                combine_cpu.to_csv(os.path.join(folder, 'ap-combine.csv'), index=False)
            elif 'mem' in filename.lower():
                combine_mem=pd.concat([pd.read_csv(filename, encoding_errors='ignore')])
                combine_mem.to_csv(os.path.join(folder, 'db-combine.csv'), index=False)
            elif 'net' in filename.lower():
                combine_net=pd.concat([pd.read_csv(filename, encoding_errors='ignore')])
                combine_net.to_csv(os.path.join(folder, 'net-combine.csv'), index=False)
            else:
                 '' 

