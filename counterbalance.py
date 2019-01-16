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
# ian.newman@usask.ca
#
# -----------------------------------------------------------------------


# ---------------------------------------------
# ---- Import Libraries
# ---------------------------------------------

# from psychopy import visual, data, event  # sound, gui, core, logging
# import os
# import sys
# import csv
from itertools import product

# ---------------------------------------------


# ---------------------------------------------
# ---- Counterbalance
# ---------------------------------------------

class Participant(object):

    """
        Class: participant object to store individual information
    """

    def __init__(self, p_num, cb_num):
        self.p_num = p_num  # the current participant number
        self.cb = [0] * cb_num  # init counterbalance array


def counter_balance(participant, cb_list):  # pass the participant class to the counterbalancer

    """
        Function: select counterbalance options per participant, store in participant class
        Arguments:
             participant = object of class Participant
            cb_list = list of counterbalancing arrays containing all options

        Example:
            cb_list = [
                [0, 1],
                [yes, no]
                }

            # 1 = [0, yes]
            # 2 = [0, no]
            # 3 = [1, yes]
            # 4 = [1, no]
    """

    if cb_list is 0:
        return

    # participants required for each full counterbalance cycle
    balance_factor = len(cb_list)
    full_counterbalance = 1
    for i in range(balance_factor):
        full_counterbalance *= len(cb_list[i])

    # create a matrix of all the combinations
    f = []
    for j in product(*cb_list):
        f.append(j)

    # select the row
    modulo_value = int(participant.p_num) % full_counterbalance
    if modulo_value == 0:
        row = full_counterbalance - 1
    else:
        row = modulo_value - 1

    # set the result
    participant.cb = f[row]
    return

# ---------------------------------------------
