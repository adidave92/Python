import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from scipy import ndimage
import seaborn.apionly as sns

import warnings
warnings.filterwarnings("ignore")

iris = sns.load_dataset('iris')
print(iris.columns)

