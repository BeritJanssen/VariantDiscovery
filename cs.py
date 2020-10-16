from collections import Counter
import re
import os.path as op

import pandas as pd
from tqdm import tqdm


def evaluate_cs(original, generated):
    '''Given a original and generated events, calculate precision, recall, and
    F1 of the cardinality score. It is expected that `original` and `generated`
    are pandas dataframes containing columns 'onset' and 'pitch' and that they
    have been deduplicated.

    Parameters
    ----------
    original : pd.DataFrame
        A dataframe containing columns 'onset' and 'pitch' representing the
        true continuation
    generated : pd.DataFrame
        A dataframe containing columns 'onset' and 'pitch' representing the
        generated continuation to be evaluated

    Returns
    -------
    output : dict[float]
        A dictionary containing three keys: 'rec', 'prec' and 'F1', the recall
        precision and the F1 of the cardinality score.
    '''
    translation_vectors = []
    generated_vec = generated[['onset', 'pitch']].values
    original_list = original[['onset', 'pitch']].values.tolist()
    for point in original_list:
        vectors = generated_vec - point
        translation_vectors.extend([tuple(v) for v in vectors])
    vector_counts = Counter(translation_vectors)
    most_common_vector, count = vector_counts.most_common(1)[0]
    recall = (count - 1) / float(len(original) - 1)
    precision = (count - 1) / float(len(generated) - 1)
    if precision + recall == 0:
        f1 = 0.0
    else:
        f1 = (2 * recall * precision) / (
            recall + precision
        )
    output = {'rec': recall, 'prec': precision, 'F1': f1}
    return output