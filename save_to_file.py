# -----------------------------------------------------------------------
#
# nir library
# ------------------
# (Newman, Ian R = nir)
# https://github.com/irnewman/nir
#
# This is a library of tools for the Cognitive Science Lab at the
# University of Saskatchewan. Please note that this is a work in progress
# and is written by an amateur; use at your own risk!
#
# All correspondence should be directed to:
#
# Ian R. Newman
# University of Saskatchewan
# ian.newman@usask.ca
#
# -----------------------------------------------------------------------


# ---------------------------------------------
# ---- Import Libraries
# ---------------------------------------------

from psychopy import event  #visual, data, sound, gui, core, logging
import os
# import sys
# import csv
# from itertools import product
import pandas

# ---------------------------------------------


# ---------------------------------------------
# ---- Save Data to File
# ---------------------------------------------

def save_to_file(data_frame, header, file_name, p_num):

    """
        Function: save data frame to file
        Arguments:
            data_frame = list of arrays, each array is a variable/column
            header = list of length data, column names for the data frame
            file_name = full path to save the file
        Note: if the arrays are of different lengths, this will not work properly
    """

    # create directory for participant
    folder = 'data' + os.sep + str(p_num)
    if not os.path.isdir(folder):
        os.makedirs(folder)

    # transpose the data and add header
    df_temp = pandas.DataFrame(data_frame)
    df = df_temp.transpose()
    df.columns = header

    # save to file
    save_file = folder + os.sep + file_name
    df.to_csv(save_file, index=False)
    return

# ---------------------------------------------


# ---------------------------------------------
# ---- Save Screen to Image File
# ---------------------------------------------

def save_to_image(win, image_name):

    """
        Function: save stimuli screenshot as png
        Arguments:
            win = psychopy window
            image_name = name of image file to save
        Note: may change to save to particular folder in the future
    """

    # file name as png
    save_name = image_name + ".png"

    # save the image
    win.getMovieFrame(buffer='front')
    win.saveMovieFrames(save_name)

    # clear buffer
    event.clearEvents()

    return

# ---------------------------------------------
