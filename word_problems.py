# -----------------------------------------------------------------------
#
# nir library
# ------------------
# (Newman, Ian R = nir)
#
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

from psychopy import visual  # sound, gui, visual, core, data, event, logging
# import os
# import sys
# import csv
# from itertools import product

# ---------------------------------------------


# ---------------------------------------------
# ---- Word Problems
# ---------------------------------------------


# change name to something other than word problems
# maybe move the below to response gathering script
    # or maybe not, some is in eye-tracking?

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


def get_keypress_resp():
    # needs keylist as argument
    # draw stimuli with other functions, get responses with this
    # getkeys, return key and rt
    pass
    return

def get_mouseclick_resp():
    # needs list of clickable objects
        # so that comes from the WordProblem, the borders
    # also need to know other features of the objects (correct, counterbalancing, etc)
        # so maybe play with this a bit to get it working, would be nice to have
    return




class WordProblem(object):

    """
        Class: object to display word problems in two to four terms
        Arguments:
            win = psychopy window
            terms = number of terms in the problem (default 2, min 2, max 4)
            term1 = first term
            term2 = second term
            term3 = third term
            term4 = fourth term
            option1 = one response option
            option2 = other response option
            option1_x = x-coord (side) to present option 1
            option2_x = x-coord (side) to present option 2
            borders = boolean to draw rectangle around terms
    """

    # init
    def __init__(self, win, terms=2, term1='', term2='', term3='', term4='', option1='', option2='', option1_x=-0.7, option2_x=0.7,
                 borders=False):
        self.win = win
        self.term1 = term1
        self.term2 = term2
        self.term3 = term3
        self.term4 = term4
        self.option1 = option1
        self.option2 = option2
        self.option1_x = option1_x
        self.option2_x = option2_x
        self.text_height = 0.1
        self.text_width = 1.5
        self.border_width = 1.55
        self.border_height = 0.25
        self.answer_height = 0.1
        self.answer_width = 0.5
        self.borders = borders
        
        # set separation of terms on screen
        if terms == 4:
            self.term_sep = 0.35
        elif terms == 3:
            self.term_sep = 0.45
        else:
            self.term_sep = 0.55
        
        # set position of options
        self.option_pos = -0.75

        # create the premises for current trial
        self.t1 = visual.TextStim(win=self.win, name='text',
                                  text=self.term1,
                                  font=u'Arial',
                                  pos=(0, self.option_pos + (self.term_sep*(terms))), height=0.1, wrapWidth=self.text_width, ori=0,
                                  color=u'white', colorSpace='rgb', opacity=1,
                                  depth=0.0)
        self.t2 = visual.TextStim(win=self.win, name='text',
                                  text=self.term2,
                                  font=u'Arial',
                                  pos=(0, self.option_pos + (self.term_sep*(terms-1))), height=0.1, wrapWidth=self.text_width, ori=0,
                                  color=u'white', colorSpace='rgb', opacity=1,
                                  depth=0.0)
        self.t3 = visual.TextStim(win=self.win, name='text',
                                  text=self.term3,
                                  font=u'Arial',
                                  pos=(0, self.option_pos + (self.term_sep*(terms-2))), height=0.1, wrapWidth=self.text_width, ori=0,
                                  color=u'white', colorSpace='rgb', opacity=1,
                                  depth=0.0)
        self.t4 = visual.TextStim(win=self.win, name='text',
                                 text=self.term4,
                                 font=u'Arial',
                                 pos=(0, self.option_pos + (self.term_sep*1)), height=0.1, wrapWidth=self.text_width, ori=0,
                                 color=u'white', colorSpace='rgb', opacity=1,
                                 depth=0.0)

        # create the response options for current trial
        self.option1 = visual.TextStim(win=win, name='text',
                                       text=self.option1,
                                       font=u'Arial',
                                       pos=(option1_x, -0.75), height=0.1, wrapWidth=None, ori=0,
                                       color=u'white', colorSpace='rgb', opacity=1,
                                       depth=0.0)
        self.option2 = visual.TextStim(win=win, name='text',
                                       text=self.option2,
                                       font=u'Arial',
                                       pos=(option2_x, -0.75), height=0.1, wrapWidth=None, ori=0,
                                       color=u'white', colorSpace='rgb', opacity=1,
                                       depth=0.0)

        # create the borders
        if self.borders:
            self.t1border = visual.Rect(win=win,
                                        pos=(0, 0.8),
                                        width=self.border_width,
                                        height=0.25)
            self.t2border = visual.Rect(win=win,
                                        pos=(0, 0.5),
                                        width=self.border_width,
                                        height=0.25)
            self.t3border = visual.Rect(win=win,
                                        pos=(0, 0.2),
                                        width=self.border_width,
                                        height=0.25)
            self.t4border = visual.Rect(win=win,
                                       pos=(0, -0.1),
                                       width=self.border_width,
                                       height=0.25)
            self.option1_border = visual.Rect(win=win,
                                              pos=(self.option1_x, -0.75),
                                              width=self.answer_width,
                                              height=0.25)
            self.option2_border = visual.Rect(win=win,
                                              pos=(self.option2_x, -0.75),
                                              width=self.answer_width,
                                              height=0.25)

    # draw elements of the stimuli
    def draw(self):

        if self.borders:  # if borders = true, draw the borders
            self.t1border.draw()
            self.t2border.draw()
            self.t3border.draw()
            self.t4border.draw()
            self.option1_border.draw()
            self.option2_border.draw()

        self.t1.draw()
        self.t2.draw()
        self.t3.draw()
        self.t4.draw()
        self.option1.draw()
        self.option2.draw()


# ---------------------------------------------






class LastTermOnly(object):

    """
        Class: object to display final term/question and two response options
        Arguments:
            win = psychopy window
            term = text of final term1
            option1 = one response option
            option2 = other response option
            option1_x = x-coord (side) to present option 1
            option2_x = x-coord (side) to present option 2
            borders = boolean to draw rectangle around terms
    """
        
    # init
    def __init__(self, win, term, option1='', option2='', option1_x=-0.7, option2_x=0.7, borders=False):
        self.win = win
        self.term = term
        self.option1 = option1
        self.option2 = option2
        self.option1_x = option1_x
        self.option2_x = option2_x
        self.text_height = 0.1
        self.text_width = 1.5
        self.border_width = 1.55
        self.border_height = 0.25
        self.answer_height = 0.1
        self.answer_width = 0.5
        self.borders = borders
        
        # set positions
        self.term_pos = -0.75
        self.option_pos = 0.75

        # create the premises for current trial
        self.term = visual.TextStim(win=self.win, name='text',
                                  text=self.term,
                                  font=u'Arial',
                                  pos=(0, self.term_pos), height=0.1, wrapWidth=self.text_width, ori=0,
                                  color=u'white', colorSpace='rgb', opacity=1,
                                  depth=0.0)

        # create the response options for current trial
        self.option1 = visual.TextStim(win=win, name='text',
                                       text=self.option1,
                                       font=u'Arial',
                                       pos=(option1_x, self.option_pos), height=0.1, wrapWidth=None, ori=0,
                                       color=u'white', colorSpace='rgb', opacity=1,
                                       depth=0.0)
        self.option2 = visual.TextStim(win=win, name='text',
                                       text=self.option2,
                                       font=u'Arial',
                                       pos=(option2_x, self.option_pos), height=0.1, wrapWidth=None, ori=0,
                                       color=u'white', colorSpace='rgb', opacity=1,
                                       depth=0.0)

        # create the borders
        if self.borders:
            self.term_border = visual.Rect(win=win,
                                        pos=(0, 0.8),
                                        width=self.border_width,
                                        height=0.25)
            self.option1_border = visual.Rect(win=win,
                                              pos=(self.option1_x, -0.75),
                                              width=self.answer_width,
                                              height=0.25)
            self.option2_border = visual.Rect(win=win,
                                              pos=(self.option2_x, -0.75),
                                              width=self.answer_width,
                                              height=0.25)

    # draw elements of the stimuli
    def draw(self):

        if self.borders:  # if borders = true, draw the borders
            self.term_border.draw()
            self.option1_border.draw()
            self.option2_border.draw()

        self.term.draw()
        self.option1.draw()
        self.option2.draw()


# ---------------------------------------------
