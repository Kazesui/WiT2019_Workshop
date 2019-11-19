import numpy as np
import matplotlib
import warnings


warnings.simplefilter('ignore', category=FutureWarning)


# Load a binary blob of specified data type (defaults to float32)
def load_binary(filename, **kwargs):
    data_type = kwargs.pop('data_type', np.float32)
    with open(filename, 'rb') as fp:
        data = np.fromfile(fp, dtype=data_type)
    return data


# Quick and dirty way of converting our string labels to numbers for conversion to 1-hot encoded vectors
def train_to_id(train_type):
    tt_lut = {'train_a': 0, 'train_b': 1, 'train_c': 2, 'train_d': 3, 'unknown': 4}
    return tt_lut[train_type]


def plot_size(width, height):
    matplotlib.rcParams['figure.figsize'] = width, height
