## read the params 
## process 
## return dataframe
import os
import yaml 
import pandas as pd 
import argparse 


#read the params from "params.yaml" file s
def read_params(config_path):
    with open(config_path) as yaml_file:
       config = yaml.safe_load(yaml_file)
    return config
    #print(config_path)
    #print(config)

def get_data(config_path):
    config = read_params(config_path)
    data_source = config["data_source"]["s3_source"]
    df = pd.read_csv(data_source, sep = "," , encoding = "utf-8")
    # print(df.head())
    return df 
   
     

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config" , default = "params.yaml")
    parsed_args = args.parse_args()
    get_data(config_path = parsed_args.config)
    

