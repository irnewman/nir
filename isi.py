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

from psychopy import visual, core  # sound, gui, visual, core, data, event, logging
# import os
# import sys
# import csv
# from itertools import product

# ---------------------------------------------
# ---- ISI (change to StaticPeriod)
# ---------------------------------------------

def isi(window, isi_time=2.0, fixation_duration=0.5, fixation=""):

    """
        Function: present an inter-stimulus interval
        Arguments:
            window = psychopy window
            isi = total interval length in seconds (default 2 seconds)
            fixation = fixation character (default blank)
            text = any text to be displayed to the screen (default "Next problem in X seconds.")
    """

    text_to_display = "Next problem in " + str(isi_time) + " seconds."
    isi_dur = isi_time - (fixation_duration+0.5)

    # make certain isi_duration is not zero or less
    if isi_dur <= 0:
        print('\nNIR Error: Total ISI time is less than fixation duration time.')
        return

    # draw the notification text
    text_display = visual.TextStim(win=window,
                                   text=text_to_display,
                                   pos=(0, 0),
                                   height=0.075,
                                   color=u'white', colorSpace='rgb',
                                   wrapWidth=1.5
                                   )
    text_display.draw()
    window.flip()
    core.wait(1)

    # flip to blank screen
    window.flip()
    core.wait(0.5)

    # draw fixation dot (if any)
    fixation_char = visual.TextStim(win=window,
                                    text=fixation,
                                    pos=(0, 0),
                                    height=0.075,
                                    color=u'white', colorSpace='rgb',
                                    wrapWidth=1.5
                                    )
    fixation_char.draw()
    window.flip()
    core.wait(fixation_duration)

    # flip to blank screen
    window.flip()
    core.wait(isi_dur)
    return
