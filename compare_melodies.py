from os.path import join, basename, splitext
import pickle

import pandas as pd
from tqdm import tqdm

from config import FILENAME
import cs

def compare_all_melodies(dfs_pickled=FILENAME, threshold=.2):
    with open(dfs_pickled, 'rb') as f:
        df_list = pickle.load(f)
    index = 0
    while len(df_list)>2:
        index += 1
        print(index)
        scores = [cs.evaluate_cs(df_list[0]['notes'], item['notes'])
            for item in df_list[1:]]
        output = pd.DataFrame({
            'a_region': [get_region(df_list[0]['filename'])]*len(df_list[1:]),
            'a_name': [get_basename(df_list[0]['filename'])]*len(df_list[1:]),
            'a_noten': [len(df_list[0]['notes'])]*len(df_list[1:]),
            'b_region': [get_region(item['filename']) for item in df_list[1:]],
            'b_name': [get_basename(item['filename']) for item in df_list[1:]],
            'b_noten': [len(item['notes']) for item in df_list[1:]],
            'F1': [score['F1'] for score in scores],
            'prec': [score['prec'] for score in scores],
            'rec': [score['rec'] for score in scores]
        })
        output.to_csv('output.csv', mode='a', index=False, header=index==1)
        filtered_output = output.loc[output['F1']>threshold]
        filtered_output.to_csv('filtered_output.csv', mode='a', index=False, header=index==1)
        df_list.pop(0)
        with open('remaining_dfs.pkl', 'wb') as f:
            # dump remaining files to be able to resume after crash
            pickle.dump(df_list, f)


def get_region(full_name):
    return full_name.split('/')[-3].split(' ')[0]


def get_basename(full_name):
    return splitext(basename(full_name))[0]
            

if __name__ == '__main__':
    compare_all_melodies()