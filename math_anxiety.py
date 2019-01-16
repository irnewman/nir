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

from psychopy import visual, event  # sound, gui, core, data, logging
# import os
# import sys
# import csv
# from itertools import product
from nir.rating_scales import get_anxiety
from nir.save_to_file import save_to_file

# ---------------------------------------------


# ---------------------------------------------
# ---- Math Anxiety Scales
# ---------------------------------------------

class MathScale(object):

    """
        Class: object to present and record responses to math anxiety scales (AMAS or AEMAS)
        Arguments:
            win = psychopy window
            participant_number = current participant number
            scale = AMAS or AEMAS scale to run
    """

    # init
    def __init__(self, win, participant_number, scale):

        self.scale = scale
        self.math_scale = []
        self.win = win
        self.participant_number = participant_number
        self.participant = []
        self.item_num = []
        self.item_text = []
        self.anxiety = []
        self.anxiety_rt = []  # maybe convert to a dictionary instead of all these arrays
        self.data = []
        self.items = []

        # initial instructions
        self.inst_text = ('In the following, you will be presented with some everyday situations.\n\n'
                          'Please rate each item in terms of how anxious you would feel during the event specified.\n\n'
                          'Use the scale below to record your answer.'
                          )
        self.instructions = visual.TextStim(win=self.win,
                                            text=self.inst_text,
                                            pos=(0, 0),
                                            height=0.075,
                                            color=u'white', colorSpace='rgb',
                                            wrapWidth=1.5)
        press_to_cont = visual.TextStim(win=self.win,
                                        text="<<Press any key to continue.>>",
                                        pos=(0, -0.75),
                                        height=0.075,
                                        color=u'white', colorSpace='rgb',
                                        wrapWidth=1.5)

        # draw instructions to screen
        self.instructions.draw()
        press_to_cont.draw()
        self.win.flip()
        event.waitKeys()

        # AMAS scale items
        self.amas_items = [
            'Having to use the tables in the back of a math book.',
            'Thinking about an upcoming math test one day before.',
            'Watching a teacher work an algebraic equation on the blackboard.',
            'Taking an examination in a math course.',
            'Being given a homework assignment of many difficult problems which is due the next class meeting.',
            'Listening to a lecture in math class.',
            'Listening to another student explain a math formula.',
            'Being given a "pop" quiz in a math class.',
            'Starting a new chapter in a math book.'
        ]

        # AEMAS scale items
        self.aemas_items = [
            'Having to work with fractions.',
            'Having to work with percentages.',
            'Having to work out a 15% tip.',
            'Figuring out how much a shirt will cost if it is 25% off.',
            'Having to work out prices in a foreign currency.',
            'Looking at tables and graphs when reading the newspaper.',
            'Being presented with numerical information about different mobile phone subscription options.',
            'Having to choose between financial investment options.',
            'Reading your bank\'s leaflet about changes in the terms of using your credit card.',
            'Having to complete a math course as part of your work training.',
            'Having to take a numeracy test as part of a job application process.',  # changed "sit" to "take"
            'Having to present numerical information at a work meeting.',
            'Making an important decision at your workplace based on last year\'s statistics.',
        ]

    def run_scale(self):

        """
            Function: run the scale and collect/save responses to file
        """

        # determine which scale to run
        if self.scale.upper() == "AMAS":
            self.items = self.amas_items
        elif self.scale.upper() == "AEMAS":
            self.items = self.aemas_items
        else:
            return

        # run the scale
        for this_item in range(0, len(self.items)):
            # wait for response
            anxiety_resp, anxiety_resp_rt = get_anxiety(self.win, self.items[this_item], see_mouse_after=True)

            # save response, rt
            self.item_num.append("item" + str(this_item + 1))
            self.item_text.append(self.items[this_item])
            self.anxiety.append(anxiety_resp)
            self.anxiety_rt.append(anxiety_resp_rt)
            self.participant.append(self.participant_number)
            self.math_scale.append(self.scale)

        # define data to save and column header
        self.data = [self.participant, self.math_scale, self.item_num, self.item_text, self.anxiety, self.anxiety_rt]
        header = ['participant', 'scale', 'item_number', 'item_text', 'anxiety', 'anxiety_rt']

        # save results to file
        current_file = self.scale + '_p' + self.participant_number + '.csv'
        save_to_file(self.data, header, current_file, self.participant_number)
