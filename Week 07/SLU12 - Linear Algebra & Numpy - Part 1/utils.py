# import all the necessary libraries
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image  # for the visuals
import time  # python module with time-related functions



# Whatever you do here... remember: The code written in this file is not intended to be used for learning purposes.


def plot_school_functions():
    
    # create a decent size figure
    plt.figure(figsize=(16, 4));

    # function descriptions
    function_names = ['Linear Function: f(x) = mx + b\n', 
                      'Quadratic Function: f(x) = x ** 2\n',
                      'Exponential Function: f(x) = b ** x\n']
    
    # x values
    x = np.linspace(-5, 5)
    
    # plot each function
    function_index = 0
    while function_index < 3:
        
        # add subplot with grid and axis
        ax = plt.subplot(1, 3, function_index+1);
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        # y limits
        plt.xlim([-4, 4])
        plt.ylim([-5, 20])
        
        # plot function
        plt.title(function_names[function_index], fontsize=14);
        if function_index == 0:
            plt.plot(x, 6*x);
        elif function_index == 1:
            plt.plot(x, x**2);
        else:
            plt.plot(x, 2**x);
        
        # increment index for next function name
        function_index += 1


# simulation - perform linear combination using Python lists
def lincomb_numpy():
    
    # think big
    m = 1000000
    
    # simulation start time
    start_time = time.time()
    
    # create two vectors with m entries (we'll learn about arrays next)
    u = np.zeros(m)
    v = np.ones(m)
    
    # perform a linear combination
    w_array = 2*u + 2*v
    
    # simulation duration
    return time.time() - start_time


# simulation - perform linear combination using NumPy arrays
def lincomb_lists():
    
    m = 1000000
    
    # simulation start time
    start_time = time.time()
    
    # create vector with m entries using list comprehension
    u = [0 for i in range(m)]
    v = [1 for j in range(m)]
    
    # perform a linear combination
    w_list = [2*uu + 2*vv for (uu, vv) in zip(u, v)]
    
    # simulation duration
    return time.time() - start_time
    

        
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

    
# fail panda
def plot_sad_panda():
    
    sad_panda = np.array(Image.open(os.path.join('data', 'sad_panda.png')))
    plt.imshow(sad_panda)