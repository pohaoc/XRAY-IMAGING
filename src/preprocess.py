import shutil
import pandas as pd
import os
import random
PATH_COVID = "/home/usr/workspace/pycharm-workspace/XRAY-IMAGING/data/covid-chestxray-dataset/metadata.csv"
IMAGES_COVID = "/home/usr/workspace/pycharm-workspace/XRAY-IMAGING/data/covid-chestxray-dataset/images"
PATH_NORMAL = '/home/usr/workspace/pycharm-workspace/XRAY-IMAGING/data/chest_xray_pneumonia/train/NORMAL'
#df = pd.read_csv(PATH_COVID)
#saved_folder = "/home/usr/workspace/pycharm-workspace/XRAY-IMAGING/post-processed/positive"
saved_folder2 = "/home/usr/workspace/pycharm-workspace/XRAY-IMAGING/post-processed/negative"

files = os.listdir(PATH_NORMAL)
random.shuffle(files)
###############
# NORMAL DATA #
###############
for i in range(180):
    filename = files[i]
    saved_to = os.path.join(saved_folder2, filename)
    path_to_img = os.path.join(PATH_NORMAL, filename)
    print('Copying', filename, '>>', saved_to)
    shutil.copy2(path_to_img, saved_to)

###############
# COVID DATA  #  Only 180 samples
###############
'''
for index, row in df.iterrows():
    if row['finding'] == 'COVID-19' and row['view'] == 'PA':
        filename = row['filename']
        path_to_img = os.path.join(IMAGES_COVID, filename)
        saved_to = os.path.join(saved_folder, filename)
        print('Copying', filename, '>>', saved_to)
        shutil.copy2(path_to_img, saved_to)
'''


