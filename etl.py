import glob
import pandas as pd
from datetime import datetime
import json
def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process)
    return dataframe
columns=['Name','Market Cap (US$ Billion)']
### extraction
def extract():
    extracted_data = pd.DataFrame(columns=columns)
    for jsonfile in ["bank_market_cap_1.json", "bank_market_cap_2.json"]:#glob.glob("*.json"):
        print(jsonfile)
        extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)
    return extracted_data
    # Write your code here
extracted_data = extract()

extracted_data.head() 

df = pd.read_csv('exchange_rates.csv', index_col=[0])
for index,row in df.iterrows():
    if(index == 'GBP'):
        print('Rates', row.Rates)
        exchange_rate = row.Rates
def transform(data):
    # Write your code here
    data['Market Cap (US$ Billion)']=round(data['Market Cap (US$ Billion)']*exchange_rate,3)
    data.rename(columns={"Market Cap (US$ Billion)":"Market Cap (GBP$ Billion)"}, inplace = True)
    return data
transformed_data = transform(extracted_data)

transformed_data.head() 
targetfile="bank_market_cap_gbp.csv"
## loading data

def load(targetfile,data_to_load):
    data_to_load.to_csv(targetfile, index=False)
#### the log message

def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt","a") as f:
        f.write(timestamp + ',' + message + '\n')
    # Call the function here
transformed_data = transform(extracted_data)
# Print the first 5 rows here
transformed_data.head() 

