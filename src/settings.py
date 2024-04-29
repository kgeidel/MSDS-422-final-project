''' Settings for TDSP ML Projects '''
# Native imports
import os

# Third-part imports
import matplotlib.pyplot as plt


#### General settings

BASE_PATH = os.path.dirname(os.getcwd())
DATA_PATH = os.path.join(BASE_PATH, 'data')

#### pyplot settings
plt.rc('font', size=10)
plt.rc('axes', labelsize=10, titlesize=10)
plt.rc('legend', fontsize=10)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)

IMAGES_PATH = os.path.join(BASE_PATH, 'img')


#### 