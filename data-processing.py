import pandas as pd #handles csv
import glob #finds all csv files in a folder(finds patternss)
import os #folder paths

#current working directory + data folder
datapath= os.path.join(os.getcwd(),'data')

#find all files ending with csv and then print them 
#folder path + /*csv means all files ending with csv
#data/file1.csv, data/file2.csv->glob.glob->['data/file1.csv','data/file2.csv']
csv_files=glob.glob(os.path.join(datapath,'*csv'))
print("found csv files:",csv_files)

dfs=[] #list of dataframes

for file in csv_files:
    df=pd.read_csv(file) 
    #tells number of rows before filtering
    print(f"Processing file:{file}), rows before filtering:", len(df))

    #we only need pink morsels
    #df[product]
    #df[df[]]-> this is like a boolean mask it checks true or false for each row
    df=df[df['product']=='pink morsel']
    print(f"Processing file:{file}), rows after keeping pink morsel:", len(df))
#   
    #total sales= quantity * price
    df['price']=df['price'].replace('[\$,]','',regex=True).astype(float) #remove $ sign and convert to float
    df['Sales']=df['quantity']*df['price']

    df=df[['Sales','date','region']]
    dfs.append(df)

final_df=pd.concat(dfs,ignore_index=True) #takes the list of dataframes and combines them into one big table.
print("Total rows combined:",len(final_df))

#saving the final file
os.makedirs('output',exist_ok=True) #makes output folder if it doesn't exist
final_df.to_csv('output/pinkmorselssales.csv',index=False) #don't write row numbers in a separate column
print("Saved succesfully!")



