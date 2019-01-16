# -----------------------------------------------------------------------
#
# nir library v0.1.3
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

from psychopy import visual, event  # data, sound, gui, core, logging
import os
# import sys
# import csv
# from itertools import product

# ---------------------------------------------


# ---------------------------------------------
# ---- Present Instructions
# ---------------------------------------------

def run_instructions(window, working_dir, folder='instructions', filename=""):

    """
        Function: present instruction from file or all files in directory
        Arguments:
            window = psychopy window
            working_dir = current working directory of script
            folder = subdirectory where instruction files are stored (default instructions)
            filename = name of instruction file to present
        Note: keep files in a single directory
            currently returns an error if folder specified contains any subfolders
    """

    cur_dir = working_dir + os.sep + folder

    if not filename:  # no filename specified
        inst_list = os.listdir(cur_dir)
        for inst_file in inst_list:
            cur_file = cur_dir + os.sep + inst_file
            print_instructions(window, cur_file)
    else:
        file = cur_dir + os.sep + filename
        print_instructions(window, file)
    return


def print_instructions(window, file):

    """
        Function: print instructions to the window, wait for keypress to continue
        Arguments:
             window = psychopy window
            file = name of text file
    """

    # load the file
    inst = open(file, 'r')
    inst_text = inst.read()

    task_instructions = visual.TextStim(win=window,
                                        text=inst_text,
                                        pos=(0, 0.25),
                                        height=0.075,
                                        color=u'white', colorSpace='rgb',
                                        wrapWidth=1.5)
    press_to_cont = visual.TextStim(win=window,
                                    text="<<Press any key to continue.>>",
                                    pos=(0, -0.75),
                                    height=0.075,
                                    color=u'white', colorSpace='rgb',
                                    wrapWidth=1.5)

    # draw to window
    task_instructions.draw()
    press_to_cont.draw()
    window.flip()
    event.waitKeys()

# ---------------------------------------------
