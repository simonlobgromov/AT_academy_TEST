import numpy as np
import pandas as pd
import json
import argparse

with open('cars.json', 'r') as f:
    cars_dict = json.load(f)
print('---- DATA LOADING ----')

def main(seed, dict_):
    cars = pd.DataFrame(dict_)
    return cars.sample(100, random_state=seed).to_dict(orient='records')

parser = argparse.ArgumentParser(description="Script for creating data with seed parameter")
parser.add_argument("--seed", type=int, default=None, help="Seed for random number generation")
args = parser.parse_args()

result = main(args.seed, cars_dict)

with open('your_data.json', 'w') as f:
    json.dump(result, f, indent = 4)

print(f'SEED: {args.seed}')
print()
print('CHECK "your_data.json" IN DERICTORY')
print('END SCRIPT')
