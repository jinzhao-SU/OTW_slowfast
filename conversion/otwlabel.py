import pandas as pd
import cv2
import os
import multiprocessing

"""
    1           2           3       4                           5           6   7       8   9       10
# Video ID, Activity ID, Actor ID, Activity or Object Type, Frame Number, XMin, YMin, XMax, YMax, Labeled
00000,	    0,              00039,	bicycle,				252,            82,   1229,  255,   1586,    True

video_name, frame_sec ，  x1,   y1,       x2,         y2      label     score
5KQ66BBWC4,   0902,     0.326,  0.185,   0.470,     0.887,  80,        0.996382

"""
annotation_path = "/home/luban/data/otw/homes/annotations.csv"
frame_path = '/nfs/cold_project/jinzhao/OTW/homes/frames/'

csv_data = pd.read_csv(annotation_path,dtype=str)

index_to_class = []
class_to_index = {}

train = pd.DataFrame(data = None, index = None, columns = None)
val = pd.DataFrame(data = None, index = None, columns = None)
#test = pd.DataFrame(data = None, index = None, columns = None)

#train_index = 405
#val_index = 405
train_index = 412#405
val_index = 579#579
#test_end = 5

frame_list = os.listdir(frame_path)
frame_list.sort(key=lambda x: int(x))
print(frame_list)

index_to_class = ['','bicycle', 'person', 'dismounting bike', 'car', 'loading vehicle', 'unloading vehicle', 'carrying (small)', 'opening trunk', 'truck', 'carrying (large)', 'closing trunk', 'opening door', 'texting on phone', 'closing door', 'cell phone', 'exiting', 'entering', 'light object', 'mounting bike', 'riding bike', 'motorcycle/scooter', 'conversation', 'talking on phone', 'heavy object', 'pushing cart', 'wheeled cart']
class_to_index = {}
for i in range(1,len(index_to_class)):
    class_to_index[index_to_class[i]] = i

def add_row(df, row_df):
    df = df.append([row_df], ignore_index=True)
    return df

def convert_int(df):
    return
    #df[0] = df[0].astype("int")
    #df[1] = df[1].astype("int")
    #df[6] = df[6].astype("int")

def main(start_index, end_index):
    csv_dataanno = pd.read_csv(annotation_path, dtype=str)
    # img_list = [i for i in range(580)]
    ann = []
    for row in csv_dataanno.itertuples():
        if int(row[1]) <= 412:
            continue
        if int(row[1]) not in ann:
            ann.append(int(row[1]))

    print(len(ann))
    train = pd.DataFrame(data=None, index=None, columns=None)
    val = pd.DataFrame(data=None, index=None, columns=None)
    #print("from {} to {}".format(start_index,end_index))
    csv_data = pd.read_csv(annotation_path, dtype=str)
    first_row = csv_data.iloc[start_index]
    cur_video = first_row[0]
    count = 0
    res_train = []
    #print("curr video", cur_video)
    path = os.path.join(os.path.join(frame_path, first_row[0]), first_row[0] + '_000001.jpg')
    im = cv2.imread(str(path))
    h, w, _ = im.shape
    #print("hw",h,w)
    tmp = pd.DataFrame(data=None, index=None, columns=None)
    #df = add_row(df, tmp)
    for row in csv_data.itertuples():
        if row[1] not in frame_list:
            continue
        frame_num = int(row[5])
        if frame_num % 30 != 0:
            continue
        if cur_video != row[1]:
            tmp = tmp.sort_values(by=[1], ascending = True)
            #count+=1
            #df = add_row(df,tmp)
            cur_video = row[1]
            #print("curr Video",cur_video)
            if (int(tmp[0][1]) <= int(start_index)):
                print("push {} to train".format(tmp[0][1]))
                #print("count", count)
                # if int(tmp[0][1]) not in res_train:
                #     res_train.append(int(tmp[0][1]))
                train = add_row(train, tmp)
            elif (int(tmp[0][1]) < int(end_index)):
                print("push {} to val".format(tmp[0][1]))
                if int(tmp[0][1]) not in res_train:
                    res_train.append(int(tmp[0][1]))
                val = add_row(val, tmp)
            else:
                break
            #print(cur_video)
            path = os.path.join(os.path.join(frame_path, row[1]), row[1] + '_000001.jpg')
            #print(path)
            im = cv2.imread(str(path))
            h, w, _ = im.shape
            #print("hw",h,w)
            tmp = pd.DataFrame(data=None, index=None, columns=None)
        curr_label = class_to_index[row[4]]
        new_row = pd.Series([row[1], int(frame_num/30), float(row[6])/w, float(row[7])/h, float(row[8])/w, float(row[9])/h, int(curr_label),1])
        row_df = pd.DataFrame([new_row])
        tmp = add_row(tmp, row_df)
    #last
    tmp = tmp.sort_values([1], ascending=True)
    print("push last to val")
    val = add_row(val, tmp)
    train.to_csv('otw_train_predicted_boxes.csv', sep=",", index=False, doublequote=1, header=False)
    val.to_csv('otw_val_predicted_boxes.csv', sep=",", index=False, doublequote=1, header=False)
    res = list(set(ann).difference(set(res_train)))
    print(res)


if __name__ == '__main__':
    #main()
    # convert_int(train)
    # convert_int(val)
    # convert_int(test)

    #train.to_csv("otw_train_predicted_boxes.csv",sep=",",index=False, doublequote=1,header = False)
    #val.to_csv("otw_val_predicted_boxes.csv",sep=",",index=False, doublequote=1,header = False)
    # for row in val.itertuples():
    #     print(row[2])
    #test.to_csv("otw_test_predicted_boxes.csv",sep=",",index=False, doublequote=1,header = False)
   #print(index_to_class)
    #print(len(index_to_class))
    main(train_index, val_index)
    #p1 = multiprocessing.Process(target=main, args=(train,1,train_index,"otw_train_predicted_boxes.csv",))
    #p2 = multiprocessing.Process(target=main, args=(val,val_index,580,"otw_val_predicted_boxes.csv",))
    #p1.start()
    #p2.start()
    #p1.join()
    #p2.join()

