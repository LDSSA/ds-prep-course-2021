# imports
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from PIL import Image



# Whatever you do here...

# This file is not intended to be used for learning purposes.

# Seriously. Don't take this code as an example.

        
# load panda
def load_panda():
    img = np.array(Image.open(os.path.join('data', 'panda.png')))[:, :, 0]
    return img


# plot grey image as 2D array
def plot_img(img_array):
    plt.imshow(img_array, cmap='gray');
        
        
# plot two images (2D arrays)
def plot_pandas(new_panda):
    
    # load original panda
    original = np.array(Image.open(os.path.join('data', 'panda.png')))[:, :, 0]
    
    # plot original vs. new panda
    plt.figure(figsize=(12, 6))
    ax1 = plt.subplot(1,2,1);
    plt.imshow(original, cmap='gray');
    ax1.set_title('original panda image');
    ax2 = plt.subplot(1,2,2);
    plt.imshow(new_panda, cmap='gray');
    ax2.set_title('new panda image');

# print panda message
def print_id():
    return "AI = A, for any matrix A, where I is the identity (multiplication rules!)"