import numpy as np
import warnings

warnings.simplefilter('ignore', category=FutureWarning)


# Load a binary blob of specified data type (defaults to float32)
def load_binary(filename, **kwargs):
    data_type = kwargs.pop('data_type', np.float32)
    with open(filename, 'rb') as fp:
        data = np.fromfile(fp, dtype=data_type)
    return data
