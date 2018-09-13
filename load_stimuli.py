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
# ian.newman@usask.ca
#
# -----------------------------------------------------------------------


# ---------------------------------------------
# ---- Import Libraries
# ---------------------------------------------

from psychopy import data  # visual, event, sound, gui, core, logging
import os
# import sys
# import csv
# from itertools import product

# ---------------------------------------------


# ---------------------------------------------
# ---- Load Stimuli Files
# ---------------------------------------------

def load_stimuli_files(working_dir, practice_filename="practice.csv", trials_filename="trials.csv", folder='stimuli'):

    """
        Function: load both the practice and test stimuli files
        Arguments:
            working_dir = current working directory of script
            practice_filename = name of practice stimuli file (default practice.csv)
            trials_filename = name of trial stimuli file (default trials.csv)
            folder = subdirectory where stimuli files are stored
    """

    stimuli_folder = working_dir + os.sep + folder
    practice_stimuli = load_practice(stimuli_folder, practice_filename)
    test_stimuli = load_trials(stimuli_folder, trials_filename)
    return practice_stimuli, test_stimuli


def load_practice(stimuli_folder, file="practice.csv"):

    """
        Function: load practice file
        Arguments:
            stimuli_folder = directory where stimuli files are stored
            file = name of practice stimuli file (default practice.csv)
    """

    practice_file = stimuli_folder + os.sep + file
    return data.importConditions(practice_file)


def load_trials(stim_folder, file="trials.csv"):

    """
        Function: loads both the practice and test stimuli files
        Arguments:
            file = name of trial stimuli file (default trial.csv)
    """

    stimuli_file = stim_folder + os.sep + file
    return data.importConditions(stimuli_file)

# ---------------------------------------------
