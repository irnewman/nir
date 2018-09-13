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

from psychopy import core, event  # visual, sound, gui, visual, data, logging
# import os
# import sys
# import csv
# from itertools import product

# ---------------------------------------------


# ---------------------------------------------
# ---- Response Collection
# ---------------------------------------------

def get_keypress_resp(key_list=None):

    """
        Function: record keyboard response to trial
        Arguments:
            key_list = allowable keys, None allows any key press
    """

    get_key = True
    event.clearEvents(eventType='keyboard')  # clear keyboard buffer

    # init timer
    timer = core.Clock()
    timer.reset()
    rt = 0
    key_press = event.BuilderKeyResponse()

    while get_key:

        # check for response
        key_press = event.getKeys(keyList=key_list)

        # if response given, end loop
        if len(key_press) > 0:
            rt = timer.getTime()
            get_key = False

    return key_press, rt

# ---------------------------------------------


def get_mouseclick_resp():  # UNFINISHED

    get_click = True
    event.clearEvents(eventType='mouse')  # clear mouse buffer

    # init timer
    timer = core.Clock()
    timer.reset()
    rt = 0

    # while get_click:

    # needs list of clickable objects
        # so that comes from the WordProblem, the borders
    # also need to know other features of the objects (correct, counterbalancing, etc)
        # so maybe play with this a bit to get it working, would be nice to have
    return rt

# ---------------------------------------------


def get_response():  # might not be useful, but would standardize the functions (argument for response input)
    # if eyetracking:
        # get timecourse response (only use keypresses)
    # if mousetracking:
        # get mousetrack response (only use clicks)
    # if keyboard:
        # get keyboard response
    # if mouseclick:
        # get mouseclick response
    # if typed:
        # get multiple keypress response
            # not sure how to do that yet
    return

# ---------------------------------------------
