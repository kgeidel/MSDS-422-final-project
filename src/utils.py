''' Functions for use in TDSP ML Projects '''
# Native imports
import os

# Third-part imports
import matplotlib.pyplot as plt
import numpy as np

# MSDS-422-final-project imports
from settings import IMAGES_PATH

#### Visualization functions

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    ''' Save pyplot figure to disk '''
    path = os.path.join(IMAGES_PATH, f"{fig_id}.{fig_extension}")
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

#### Data wrangling functions

