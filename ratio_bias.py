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

from psychopy import visual  # sound, gui, core, data, event, logging
# import os
# import sys
# import csv
# from itertools import product

# ---------------------------------------------


# ---------------------------------------------
# ---- RatioGrids
# ---------------------------------------------

class RatioGrids(object):

    """
        Class: object to display two grids of dots based on ratio arguments
        Arguments:
            win = psychopy window
            left_num = numerator of left ratio
            left_denom = denominator of left ratio
            right_num = numerator of right ratio
            right_denom = denominator of right ratio
            num_color = color of the numerator dots (default darkred)
            denom_color = color of the denominator dots (default darkblue)
    """

    # init
    def __init__(self, win, left_num, left_denom, right_num, right_denom,
                 num_color="darkred", denom_color="darkblue"):
        self.win = win
        self.num_color = num_color  # numerator colour
        self.denom_color = denom_color  # denominator colour
        self.row_length = 10
        self.left_num = left_num
        self.left_denom = left_denom
        self.right_num = right_num
        self.right_denom = right_denom

        # format on-screen position of grids
        self.half_width = (self.win.size[0] / 2)
        self.buffer_width = (self.win.size[0] / 12)  # size of margins, change denominator to alter dot size
        self.vertical_offset = (self.win.size[1] / 5)  # vertical position for dots to start

        # position for each grid array
        self.left_array_centre = self.half_width / 2
        self.right_array_centre = self.half_width + (self.half_width / 2)

        # dot sizes
        self.dot_area = self.half_width - (self.buffer_width * 2)
        self.dot_size = self.dot_area / self.row_length
        self.dot_space = self.dot_size

        # centres the grids
        self.left_offset = self.half_width - self.buffer_width - (self.dot_size / 2)
        self.right_offset = self.buffer_width + (self.dot_size / 2)

        # array variables for dot positions
        self.left_num_dot_xys = []
        self.left_denom_dot_xys = []
        self.right_num_dot_xys = []
        self.right_denom_dot_xys = []

        # left ratio
        self.left_ratio = visual.TextStim(win=win,
                                          pos=(-(self.half_width / 2), self.vertical_offset * 2),
                                          text='%1i / %1i' % (self.left_num, self.left_denom),
                                          color='white', height=self.dot_size, bold=True)

        # right ratio
        self.right_ratio = visual.TextStim(win=win,
                                           pos=((self.half_width / 2), self.vertical_offset * 2),
                                           text='%1i / %1i' % (self.right_num, self.right_denom),
                                           color='white', height=self.dot_size, bold=True)

        # left numerator dot positions
        for lndot in range(self.left_num):
            lndot_x = ((lndot % self.row_length) * self.dot_space) - self.left_offset
            lndot_y = ((lndot / self.row_length) * (-self.dot_space)) + self.vertical_offset
            self.left_num_dot_xys.append([lndot_x, lndot_y])

        # left numerator dots
        self.left_num_dot_stim = visual.ElementArrayStim(
            win=self.win,
            units="pix",
            nElements=self.left_num,
            elementTex=None,
            elementMask="circle",
            colors=self.num_color,
            xys=self.left_num_dot_xys,
            sizes=self.dot_size
        )

        # right numerator dot positions
        for rndot in range(self.right_num):
            rndot_x = ((rndot % self.row_length) * self.dot_space) + self.right_offset
            rndot_y = ((rndot / self.row_length) * (-self.dot_space)) + self.vertical_offset
            self.right_num_dot_xys.append([rndot_x, rndot_y])

        # right numerator dots
        self.right_num_dot_stim = visual.ElementArrayStim(
            win=self.win,
            units="pix",
            nElements=self.right_num,
            elementTex=None,
            elementMask="circle",
            colors=self.num_color,
            xys=self.right_num_dot_xys,
            sizes=self.dot_size
        )

        # left denominator dot positions
        for lddot in range(self.left_denom):
            lddot_x = ((lddot % self.row_length) * self.dot_space) - self.left_offset
            lddot_y = ((lddot / self.row_length) * (-self.dot_space)) + self.vertical_offset
            self.left_denom_dot_xys.append([lddot_x, lddot_y])

        # left denominator dots
        self.left_denom_dot_stim = visual.ElementArrayStim(
            win=self.win,
            units="pix",
            nElements=self.left_denom,
            elementTex=None,
            elementMask="circle",
            colors=self.denom_color,
            xys=self.left_denom_dot_xys,
            sizes=self.dot_size
        )

        # right denominator dot positions
        for rddot in range(self.right_denom):
            rddot_x = ((rddot % self.row_length) * self.dot_space) + self.right_offset
            rddot_y = ((rddot / self.row_length) * (-self.dot_space)) + self.vertical_offset
            self.right_denom_dot_xys.append([rddot_x, rddot_y])

        # right denominator dots
        self.right_denom_dot_stim = visual.ElementArrayStim(
            win=self.win,
            units="pix",
            nElements=self.right_denom,
            elementTex=None,
            elementMask="circle",
            colors=self.denom_color,
            xys=self.right_denom_dot_xys,
            sizes=self.dot_size
        )

    # draw elements of the grids
    def draw(self):
        self.left_ratio.draw()
        self.right_ratio.draw()
        self.left_denom_dot_stim.draw()
        self.left_num_dot_stim.draw()
        self.right_denom_dot_stim.draw()
        self.right_num_dot_stim.draw()


# ---------------------------------------------
