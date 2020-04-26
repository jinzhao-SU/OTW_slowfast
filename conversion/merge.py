import pandas as pd

train1 = "train1.csv"
train2 = "train2.csv"
train3 = "train3.csv"
train4 = "train4.csv"

# csv_data1 = pd.read_csv(train1,dtype=str,sep = " ")
# csv_data2 = pd.read_csv(train2,dtype=str,sep = " ")
# csv_data3 = pd.read_csv(train3,dtype=str,sep = " ")
# csv_data4 = pd.read_csv(train4,dtype=str,sep = " ")
# csv_data = csv_data1.append(csv_data2)
# csv_data = csv_data.append(csv_data3)
# csv_data = csv_data.append(csv_data4)
# csv_data.to_csv("train.csv", sep=" ", index=False, doublequote=1)

test1 = "test1.csv"
test2 = "test2.csv"
test3 = "test3.csv"
test4 = "test4.csv"
csv_data1 = pd.read_csv(test1,dtype=str,sep = " ")
csv_data2 = pd.read_csv(test2,dtype=str,sep = " ")
csv_data3 = pd.read_csv(test3,dtype=str,sep = " ")
csv_data4 = pd.read_csv(test4,dtype=str,sep = " ")
csv_data = csv_data1.append(csv_data2)
csv_data = csv_data.append(csv_data3)
csv_data = csv_data.append(csv_data4)
csv_data.to_csv("test.csv", sep=" ", index=False, doublequote=1)