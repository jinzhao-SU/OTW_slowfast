import pandas as pd
import cv2
import os
annotation_path = "/home/luban/data/otw/homes/annotations.csv"
frame_path = '/nfs/cold_project/jinzhao/OTW/homes/frames/'
train_file = 'train.csv'
val_file = 'test.csv'

csv_data = pd.read_csv(annotation_path,dtype=str)
#img_list = [i for i in range(580)]
ann = []
for row in csv_data.itertuples():
    if  int(row[1]) not in ann:
        ann.append(int(row[1]))
    if int(row[1]) == 407:
        break
print(len(ann))
#res = list(set(img_list).difference(set(ann)))
#res.sort()
#print(res)

train_data = pd.read_csv(train_file,dtype=str,sep=" ")
train_list = []
for row in train_data.itertuples():
    if  int(row[1]) not in train_list:
        train_list.append(int(row[1]))
    if int(row[1]) == 407:
        break
print(len(train_list))
#[16, 19, 21, 30, 40, 52, 63, 66, 67, 83, 96, 168, 214, 227, 262, 289, 377, 403, 440, 510, 540, 565]