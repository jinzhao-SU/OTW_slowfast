import pandas as pd
import os

test_path = "ava_test_predicted_boxes.txt"
csv_data = pd.read_csv(test_path)

s = set([])
for row in csv_data.itertuples():
    print(row[1])
    s.add(row[1])

print(len(s))
