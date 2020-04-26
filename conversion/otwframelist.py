import pandas as pd
import os
import multiprocessing


'''
original_vido_id    video_id    frame_id    path                                        labels
-5KQ66BBWC4         0               0       -5KQ66BBWC4/-5KQ66BBWC4_000001.jpg          ""
-5KQ66BBWC4 0 1 -5KQ66BBWC4/-5KQ66BBWC4_000002.jpg ""
'''

train = pd.DataFrame(data = None, index = None, columns = None)
test = pd.DataFrame(data = None, index = None, columns = None)

frame_path = '/nfs/cold_project/jinzhao/OTW/homes/frames/'




train_index = 390#405  from 0 to 389
val_index = 390#579   from 390 to 557

def append_df(df, row_df):
    df = df.append([row_df], ignore_index=True)
    return df


def main(df, start_index, end_index,name):
    video_id = start_index
    print("start from {}".format(start_index))
    global frame_path
    min_frame = 9999
    frame_list = os.listdir(frame_path)

    frame_list.sort(key=lambda x: int(x))
    print(frame_list)
    for dir in frame_list[start_index:end_index]:
        dir = os.path.join(frame_path, dir)
        if os.path.isdir(dir):
            print("find folder", dir)
            frame_id = 0
            parent_dir = os.path.basename(dir)
            #print("parent", parent_dir)
            img_list = os.listdir(dir)
            #print(img_list)
            img_list.sort(key=lambda image:  (image.split('.')[0]))
            #print(img_list)
            for image in img_list:
                #(dir_name, _) = os.path.splitext(dir)
                new_row = pd.Series([parent_dir, str(video_id), str(frame_id), str(os.path.join(parent_dir, image)),str('""')])
                #print("newrow",new_row)
                row_df = pd.DataFrame([new_row])
                df = append_df(df, row_df)
                frame_id += 1
            if frame_id < min_frame:
                min_frame = frame_id
            video_id += 1
    df.columns = ['original_vido_id', 'video_id', 'frame_id', 'path', 'labels']
    df.to_csv(name, sep=" ", index=False, doublequote=1)
    print(min_frame)
    #test.columns = ['original_vido_id', 'video_id', 'frame_id', 'path', 'labels']
#print(df.to_string(index=False))
#df.to_csv("framelist.csv",sep=" ",index=False, doublequote=1)


#train = df[:351]
#test = df[352:447]
if __name__ == '__main__':
    #p1 = multiprocessing.Process(target=main, args=(train,0,100,"train1.csv",))
    #p2 = multiprocessing.Process(target=main, args=(train, 100, 200, "train2.csv",))
    #p3 = multiprocessing.Process(target=main, args=(train, 200, 300, "train3.csv",))
    #p4 = multiprocessing.Process(target=main, args=(train, 300, 390, "train4.csv",))
    p5 = multiprocessing.Process(target=main, args=(test, 390, 430, "test1.csv",))
    p6 = multiprocessing.Process(target=main, args=(test,430,470,"test2.csv",))
    p7 = multiprocessing.Process(target=main, args=(test, 470, 510, "test3.csv",))
    p8 = multiprocessing.Process(target=main, args=(test, 510, 559, "test4.csv",))
    #p1.start()
    #p2.start()
    #p4.start()
    # p5.start()
    # p6.start()
    # p7.start()
    p8.start()
    #p3.start()
    #p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
    # p5.join()
    # p6.join()
    # p7.join()
    p8.join()


