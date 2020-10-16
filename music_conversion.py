from glob import glob
import pandas as pd
import pickle

import music21 as m21

from config import DATA_PATH, FILENAME

def parse_files(data_path):
    df_list = []
    for item in glob('{}/*/*/*xml'.format(data_path)):
        piece = m21.converter.parse(item)
        onsets = [note.offset for note in piece.flat.notes]
        pitches = [note.pitch.midi for note in piece.flat.notes]
        if not pitches:
            print(item)
            continue
        df = pd.DataFrame.from_dict({'onset': onsets, 'pitch': pitches})
        df_list.append({'filename': item, 'notes': df})
    return df_list


def if __name__ == "__main__":
    df_list = parse_files(DATA_PATH)
    with open(FILENAME, 'wb') as f:
        pickle.dump(df_list, f)
