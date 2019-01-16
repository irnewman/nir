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


# -----------------------------------------------------------------------

# Experiment Title

"""
    Experiment Description Here

    This is a general template for Psychopy tasks created
    in conjunction with the nir library. This will not run
    correctly "out-of-the-box" but will serve as a useful
    structure to creating your own Psychopy programs. To use
    the nir library, download the library folder from github
    and place the unzipped folder into your main experiment
    folder.

    https://github.com/irnewman/nir
"""

# This experiment was created using PsychoPy2 Experiment Builder
# If you publish work using this script please cite the relevant PsychoPy publications
# Peirce (2007) Journal of Neuroscience Methods 162:8-1
# Peirce (2009) Frontiers in Neuroinformatics, 2: 10"""

# -----------------------------------------------------------------------


# ---------------------------------------------
# ---- Import Libraries
# ---------------------------------------------

"""
    This section imports the necessary libraries to 
    run your experiment. The required libraries will
    depend on your experiment. Psychopy will give you 
    an error if the library is not found.
"""

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
# ---- Experiment Setup
# ---------------------------------------------

"""
    This section sets up necessary features of the experiment.
    
    Change expInfo list to change collected demographics window at 
    the start of the program. Edit filename if you want the data file
    saved to be named in another manner. Much of this is the default 
    settings for any Psychopy experiment and there is little use in 
    changing the majority of it.
"""

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



# ---------------------------------------------
# --- Participant and Counterbalancing
# ---------------------------------------------

"""
    This optional section allows for counterbalancing 
    certain features within the program, wherever possible.

    Example: half of participants see stimuli_A and half
    see stimuli_B. This section would create a Participant 
    structure and save their counterbalancing settings in 
    that structure (based on their participant number). To
    counterbalance more features, add them to cb_list.
"""

'''
# OPTIONAL: define a list of counterbalancing options
cb_list = [
    ['stimuli_A.csv', 'stimuli_B.csv'],  # example: two different item lists
]

# number of counterbalancing items
cb_num = len(cb_list)

# create participant structure
participant = nir.Participant(expInfo['participant'], cb_num)

# OPTIONAL: run the counterbalancer
nir.counter_balance(participant, cb_list)

# ---------------------------------------------
'''


# ---------------------------------------------
# --- Eye-tracking: Calibration
# ---------------------------------------------

"""
    This optional section will calibrate the eye-tracker
    when running an eye-tracking experiment.

    You must create a separate window (here, cal_win) for
    use during calibration and create calibration instructions
    as .txt file(s). This function will log a file of 
    information regarding eye-tracking calibration success,
    sampling rate of eye-tracker, and so on.
"""

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

"""
    This section creates the main program window and 
    runs the task instructions. You may also use the 
    run_instructions function at other points in the 
    program, if you choose. Specify the folder where
    the instruction .txt file(s) are located.
    
    Optional: run the function with a file that displays
    the end-of-calibration instructions.
"""

# create task window
win = visual.Window(
    size=(1920, 1200), pos=[0, 0],
    fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=u'black', colorSpace='rgb',
    blendMode='avg', useFBO=True)

# Eye-tracking: run end-of-calibration instructions
'''nir.run_instructions(win, _thisDir, folder = "calibration_instructions", filename = 'cal_complete.txt')'''

# run task instructions
nir.run_instructions(win, _thisDir, folder="instructions")

# ---------------------------------------------


# ---------------------------------------------
# ---- load stimuli
# ---------------------------------------------

"""
    This section will load the stimuli you have created
    in a .csv file. It is simplest to name your stimuli
    files practice.csv and trials.csv but you may change
    that if you wish. See load_stimuli.py for more 
    information. Store the practice and trial files in
    a stimuli folder in your experiment folder.
"""

stim_file = "trials.csv"  # the function default is also trials.csv

# if counterbalancing stimuli files
'''stim_file = participant.cb[0]'''

practice_stimuli, test_stimuli = nir.load_stimuli_files(_thisDir, folder='stimuli', trials_filename=stim_file)

# ---------------------------------------------


# ---------------------------------------------
# ---- setup the trial handler
# ---------------------------------------------

"""
    This section creates the trial handler for looping
    through your items/problems. It is part of the 
    Psychopy program/library and makes storing and 
    outputting your data very simple. The below format
    is the default for most Psychopy experiments.
"""

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(trialList=test_stimuli, nReps=1, method='random',
                           originPath=None,
                           seed=None, name='trials')
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values

# ---------------------------------------------


# ---------------------------------------------
# ---- run the trial sequence
# ---------------------------------------------

"""
    This section is the main body of your experiemnt.
    What follows below will depend on the experiment 
    you wish to run. The basic architecture is a for
    loop that loops through each row in the trial handler,
    which is the same as the stimuli.csv file you 
    created and loaded above. A basic structure is 
    given below as an example.
    
    1. a loop that runs through each row of trialHandler
    2. add the current loop the thisExp
    3. run the inter stimulus interval
    4. create the trial to be presented to the screen
        - in this example, a CRT trial
    5. present that trial to the window
    6. run a function to collect your response
        - keyboard press, mouseclick, eye-track
    7. repeat for another measure (e.g. confidence rating)
    8. save the variables to the trial handler
    
    NOTE: for simplicity, the below does not contain any 
    eye-tracking measures. In the future, another template
    with eye-tracking will be created.
"""

# Initialize components for Routine "trial"
trialClock = core.Clock()

# start the eye-tracker
# iViewXAPI.iV_StartRecording()
'''optional: start eye-tracker'''

# loop through each row in the trial handler
for thisTrial in trials:

    thisExp.addLoop(trials)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec('{} = thisTrial[paramName]'.format(paramName))

    # create key response variables
    key_list = ["a", "d"]

    # run ISI
    nir.isi(win)

    # create the trial
    crt_read = nir.WordProblem(win, 3, thisTrial['premise1'], thisTrial['premise2'], thisTrial['premise3'])
    crt_resp = nir.LastTermOnly(win, thisTrial['conclusion'], thisTrial['option1'], thisTrial['option2'],
                                option1_x, option2_x)


    # Response and RT
    # ---------------------------------------------

    # draw the response trial
    crt_resp.draw()
    win.flip()

    # get response, response time, and eye-tracking time-course
    resp, rt = nir.get_keypress_resp(key_list=key_list)


    # Confidence and RT
    # ---------------------------------------------

    # wait for response
    confidence, conf_rt = nir.get_confidence(win)

    # save response and rt
    trials.addData('confidence', confidence)
    trials.addData('conf_rt', conf_rt)

    # Save Variables
    # ---------------------------------------------

    # responses and rt
    trials.addData('key_reading', key_reading)
    trials.addData('reading.rt', reading.rt)
    trials.addData('resp', resp)
    trials.addData('rt', rt)

    # save accuracy
    if key_resp.keys == correct_resp:
        trials.addData('accuracy', 1)
    else:
        trials.addData('accuracy', 0)

    # move to next trial
    thisExp.nextEntry()



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

thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit


# ---------------------------------------------
# ---- close the experiment
# ---------------------------------------------

# end of this routine
window.close()
core.quit()
