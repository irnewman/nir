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


# -----------------------------------------------------------------------

# Experiment Title

"""
    Experiment Description
"""

# This experiment was created using PsychoPy2 Experiment Builder
# If you publish work using this script please cite the relevant PsychoPy publications
# Peirce (2007) Journal of Neuroscience Methods 162:8-1
# Peirce (2009) Frontiers in Neuroinformatics, 2: 10"""

# -----------------------------------------------------------------------


# ---------------------------------------------
# ---- import libraries
# ---------------------------------------------

import psychopy.visual
from psychopy import sound, gui, visual, core, data, event, logging
import os
import sys
from numpy import *  # many different maths functions
from numpy.random import *  # maths randomisation functions
import psychopy.logging  # import like this so it doesn't interfere with numpy.log
# import random
# from psychopy import locale_setup
# from psychopy import core, data, event, visual, gui

# eye-tracking libraries
# from iViewXAPI import  *            #iViewX library
# from iViewXAPIReturnCodes import *

import nir

# ---------------------------------------------


# ---------------------------------------------
# ---- experiment setup
# ---------------------------------------------

expName = 'SET EXP NAME'
expInfo = {'participant': '', 'age': '', 'gender': ''}

# store info about the experiment session
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# create data folder
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
    os.makedirs('data' + os.sep + str(expInfo['participant']))

# relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# output files
filename = _thisDir + os.sep + u'data/%s/%s_p%s' % (expInfo['participant'], expName, expInfo['participant'])
logFile = logging.LogFile(filename + '.log', level=logging.EXP)

# create experiment handler
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=None,
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)

logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
endExpNow = False  # flag for 'escape' or other condition => quit the exp

# ---------------------------------------------


# OPTIONAL
# ---------------------------------------------
# --- Participant and Counterbalancing
# ---------------------------------------------
'''
# OPTIONAL: define a list of counterbalancing options
cb_list = [
    ['stimuli_A.csv', 'stimuli_B.csv'],  # example: two different item lists
] # note: should probably do stimuli files first, or be aware of which number in the array is the stim files?

# number of counterbalancing items
cb_num = len(cb_list)

# create participant structure
participant = nir.Participant(expInfo['participant'], cb_num)

# OPTIONAL: run the counterbalancer
nir.counter_balance(participant, cb_list)

# ---------------------------------------------
'''

# OPTIONAL
# ---------------------------------------------
# --- Eye-tracking: Calibration
# ---------------------------------------------
'''
# create a calibration instructions window
cal_win = visual.Window(
    size=(1920, 1200), pos = [0,0],
    fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='PrimaryMonitor', color=u'black', colorSpace='rgb',
    blendMode='avg', useFBO=True)

# run calibration instructions
nir.run_instructions(cal_win, folder = "calibration_instructions")

# close the window before calibration
cal_win.close()
""" calibration routine creates and closes it's own windows """

# calibrate the eye-tracker
    # change this value to the participant struct
nir.run_calibration(participant = participant.p_num)

# ---------------------------------------------
'''

# NOTE: the instructions folder must only contain files, no subfolders (for now)
# ---------------------------------------------
# --- Task Instructions
# ---------------------------------------------

# create task window
win = visual.Window(
    size=(1920, 1200), pos=[0, 0],
    fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=u'black', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# units = u'pix', # units for folder with images? what is this?


# Eye-tracking: run end-of-calibration instructions
'''nir.run_instructions(win, _thisDir, folder = "calibration_instructions", filename = 'cal_complete.txt')'''

# run task instructions
nir.run_instructions(win, _thisDir, folder="instructions")

# ---------------------------------------------


# ---------------------------------------------
# ---- load stimuli
# ---------------------------------------------

stim_file = "trials.csv"  # the function default is also trials.csv, so this argument is optional

# if counterbalancing stimuli files
'''stim_file = participant.cb[0]'''

practice_stimuli, test_stimuli = nir.load_stimuli_files(_thisDir, folder='stimuli', trials_filename=stim_file)

# ---------------------------------------------


# ---------------------------------------------
# ---- setup the trial handler
# ---------------------------------------------

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(trialList=test_stimuli, nReps=1, method='random',
                           originPath=None,
                           seed=None, name='trials')
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values

# ---------------------------------------------


# ---------------------------------------------
# ---- run the trial sequence - INCOMPLETE
# ---------------------------------------------

# the main body of the task goes here, dependent on the task you want to run
# some features will be universal (see below)

# currently available in nir:
# CRT
# ratio bias
# confidence ratings

# soon: 
# math anxiety
# water jugs

# eventually:
# henry's diagnostic test
# syllogisms
# conditionals
# anagrams
# numerical tasks


# ---------------------------------------------
# ---- follow-up tasks
# ---------------------------------------------

# for example, run the math anxiety scale
# this is done outside the main trial sequence


# OPTIONAL
# ---------------------------------------------
# ---- stop recording and disconnect from iViewX
# ---------------------------------------------

'''
iViewXAPI.iV_StopRecording()
outputfile = path + filename + ".idf"
res = iViewXAPI.iV_SaveData(str(outputfile), str(description), str(user), 1)
print "iV_SaveData " + str(res)
print "data saved to: " + outputfile

iViewXAPI.iV_Disconnect()
'''

# ---------------------------------------------
# ---- save and output the data
# ---------------------------------------------


# ---------------------------------------------
# ---- close the experiment
# ---------------------------------------------

# end of this routine
window.close()
core.quit()
