import os, pandas as pd
import subprocess
import shutil
#FOR counting
counter=1000

#for relog
def run_filecpu(path):

    global counter 
    counter=counter+1
    subprocess.run(f'relog -f csv {path} -o {str(counter)+'cpu'}.csv' ) 
    
def run_filemem(path):

    global counter 
    counter=counter+1
    subprocess.run(f'relog -f csv {path} -o {str(counter)+'mem'}.csv' ) 
    
def run_filenet(path):

    global counter 
    counter=counter+1
    subprocess.run(f'relog -f csv {path} -o {str(counter)+'net'}.csv' ) 
    
# for all file
#r"C:\\Users\\Ariake\\Desktop\\20230214\\log\\\13svnnap\\cpu"

def run_all_files(folder_path):

    for filename in os.listdir(folder_path):
        if filename.endswith(".blg"):
            if 'cpu' in filename.lower():
                joined_file = os.path.join(folder_path,filename)
                run_filecpu(joined_file)
            elif 'mem' in filename.lower():
                joined_file = os.path.join(folder_path,filename)
                run_filemem(joined_file)
            elif 'net' in filename.lower():
                joined_file = os.path.join(folder_path,filename)
                run_filenet(joined_file)
            else:
                 ''   
 
# Merge CSV
def merge_csv(folder):
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

folder_path = r"C:\Users\Ariake\Desktop\20240304\AP-FOLDER\AP"
            
target_folder = r"C:\Users\Ariake\Desktop\full-02"




run_all_files(folder_path)


if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# Get a list of CSV files in the source folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

# Move each CSV file to the target folder
for csv_file in csv_files:
    source_filepath = os.path.join(folder_path, csv_file)
    target_filepath = os.path.join(target_folder, csv_file)
    shutil.move(source_filepath, target_filepath)

merge_csv(target_folder)

