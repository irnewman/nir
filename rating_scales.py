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

from psychopy import visual, event  # core, data, sound, gui, core, logging
# import os
# import sys
# import csv
# from itertools import product

# ---------------------------------------------


# ---------------------------------------------
# ---- Confidence Rating
# ---------------------------------------------

def create_confidence_scale(window):

    """
        Function: create a rating scale to rate confidence
        Arguments:
             window = psychopy window
    """

    conf = visual.RatingScale(win=window, name='rating',
                              marker=u'triangle',
                              size=2.0, pos=[0, 0],
                              low=0, high=100, markerStart=50,
                              labels=[u'0%', u'100%'],
                              scale=u'Rate how right you feel about your response',
                              tickHeight=u'-0.0',
                              singleClick=False)
    return conf


def get_confidence(window, see_mouse_after=False):

    """
        Function: collect confidence rating and confidence response time
        Arguments:
             window = psychopy window
             see_mouse_after = boolean for visible mouse cursor after rating
    """

    # clear the screen
    window.flip()

    # center the mouse
    mouse = event.Mouse()
    mouse.setPos((0,0))

    # gather response
    conf_rating = create_confidence_scale(window)  # create the confidence scale
    while conf_rating.noResponse:
        conf_rating.draw()
        window.flip()

    # save response and rt
    confidence = conf_rating.getRating()
    conf_rt = conf_rating.getRT()
    event.Mouse(visible=see_mouse_after, newPos=[0,0])
    return confidence, conf_rt

# ---------------------------------------------


# ---------------------------------------------
# ---- Anxiety Rating
# ---------------------------------------------

def create_anxiety_scale(window):

    """
        Function: create a rating scale to rate math anxiety
        Arguments:
             window = psychopy window
    """
    anxiety_rating = visual.RatingScale(win=window,
                                        name='rating',
                                        marker=u'triangle',
                                        size=1.25, pos=[0.0, -0.5],
                                        low=1, high=5,
                                        labels=[u'Low Anxiety', u'High Anxiety'],
                                        scale=u'Rate how anxious you would feel',
                                        tickHeight=u'-0.5')
    return anxiety_rating


def get_anxiety(window, item_text, see_mouse_after=False):

    """
        Function: collect anxiety rating and response time
        Arguments:
             window = psychopy window
             see_mouse_after = boolean for visible mouse cursor after rating
    """
    
    anxiety_scale_text = ('Scale:\n'
                          '1 = Low Anxiety\n'
                          '2 = Some Anxiety\n'
                          '3 = Moderate Anxiety\n'
                          '4 = Quite a bit of Anxiety\n'
                          '5 = High Anxiety'
                          )

    anxiety_scale_values = visual.TextStim(win=window,
                                         text=anxiety_scale_text,
                                         pos=(0.75, 0.75),
                                         height=0.06,
                                         color=u'white', colorSpace='rgb',
                                         wrapWidth=1.5)
    
    item_display = visual.TextStim(win=window, name='anx_item',
                               text=item_text,
                               font=u'Arial',
                               pos=(0, 0.1), height=0.1, wrapWidth=1.5, ori=0,
                               color=u'white', colorSpace='rgb', opacity=1,
                               depth=0.0)

    # gather response
    anx_rating = create_anxiety_scale(window)
    while anx_rating.noResponse:
        anxiety_scale_values.draw()
        item_display.draw()
        anx_rating.draw()
        window.flip()

    # save response and rt
    anxiety = anx_rating.getRating()
    anxiety_rt = anx_rating.getRT()
    event.Mouse(visible=see_mouse_after)
    return anxiety, anxiety_rt

# ---------------------------------------------
