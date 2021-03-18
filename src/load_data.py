#read data from data_source(get_data.py file)
#save itin data\raw for further process
# # op - save file at path(data\raw) 

import pandas as pd 
import os 
from get_data import get_data , read_params
import argparse 
import yaml 

def load_and_save_data(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    cols = [col.replace(" ","_") for col in df.columns]   # replacing space by the ("_")
    raw_data_path = config['load_data']['raw_dataset_csv']
    # save the df at raw_data_path 
    df.to_csv(raw_data_path , sep ="," , encoding ='utf-8' , header=cols)



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config" , default = "params.yaml")
    parsed_args = args.parse_args()
    load_and_save_data(config_path = parsed_args.config)
    
    
