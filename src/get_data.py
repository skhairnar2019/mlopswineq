## read params
## process
## return dataframe
import os
from pathlib import Path

import yaml
import pandas as pd
import argparse

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    # print(config)
    data_path = Path(__file__).parent / config["data_source"]["s3_source"]
    print(data_path)
    df = pd.read_csv(data_path, sep=",", encoding='utf-8')
    return df



if __name__=="__main__":
    args = argparse.ArgumentParser()
    path=Path(__file__).parent / "../params.yaml"
    print(path)
    args.add_argument("--config", default=path)
    parsed_args = args.parse_args()
    data = get_data(config_path=parsed_args.config)