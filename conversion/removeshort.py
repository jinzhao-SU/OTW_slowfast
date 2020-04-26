import pandas as pd
import cv2
import os

label = "train.csv"
short = [130,66,199,141,46]
csv_data = pd.read_csv(label,dtype=str,sep = " ")
for row in csv_data.itertuples():
    if  int(row[1]) in short:
        ann.append(int(row[1]))
    if int(row[1]) == 407:
        break