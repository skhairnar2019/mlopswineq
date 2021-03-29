# split the raw data
# save it in data/processed folder
import os
import argparse
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from src.get_data import read_params

def split_and_saved_data(config_path):
    config = read_params(config_path)
    test_data_path = Path(__file__).parent /config["split_data"]["test_path"]
    train_data_path = Path(__file__).parent /config["split_data"]["train_path"]
    raw_data_path = Path(__file__).parent /config["load_data"]["raw_dataset_csv"]
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]

    df = pd.read_csv(raw_data_path, sep=",")
    train, test = train_test_split(
        df,
        test_size=split_ratio,
        random_state=random_state
        )
    train.to_csv(train_data_path, sep=",", index=False, encoding="utf-8")
    test.to_csv(test_data_path, sep=",", index=False, encoding="utf-8")

if __name__=="__main__":
    args = argparse.ArgumentParser()
    path = Path(__file__).parent / "../params.yaml"
    args.add_argument("--config", default=path)
    parsed_args = args.parse_args()
    split_and_saved_data(config_path=parsed_args.config)