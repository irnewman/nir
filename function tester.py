


# ---------------------------------------------
# ---- import libraries
# ---------------------------------------------

import psychopy.visual  # to prevent avbin.dll warning (not sure why necessary yet)
import os
import sys
#import imageCap
import random
from psychopy import  sound, gui, visual, core, data, event, logging
from itertools import product

import nir


# ---------------------------------------------
# ---- experiment handler - INCOMPLETE (very messy too)
# ---------------------------------------------


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)


"""change this to allow for other p numbers, because the rest should
have an error if it isn't an integer (or add that to it)

"""
# Store info about the experiment session
expName = 'function_tester'
expInfo = {'participant':''}
while not expInfo['participant']:
    dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    #dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName


# create data folder
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
    os.makedirs('data' + os.sep + str(expInfo['participant']))

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s/%s_p%s' % (expInfo['participant'], expName, expInfo['participant'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
    
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp


win = visual.Window(
    size=(1920, 1200), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=u'black', colorSpace='rgb',
    blendMode='avg', useFBO=True)










"""
# ---------------------------------------------
# ---- trial handler
# ---------------------------------------------



# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(trialList=test_stimuli, nReps=1, method='random',
                           originPath=-1,
                           seed=None, name='trials')
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values

# ADD SOME ISI before EACH CRT problem
# perhaps drift correction?

for thisTrial in trials:  # currently logs resp/rt properly, need to add eyetracking values too, plus FOR (keep within same trial)
    thisExp.addLoop(trials)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec('{} = thisTrial[paramName]'.format(paramName))
            # exec(paramName + '= thisTrial.' + paramName)

    key_resp = event.BuilderKeyResponse()


    thisExp.nextEntry()

"""

# ---------------------------------------------
# ---- Testing Section
# ---------------------------------------------



#nir.run_instructions(win, _thisDir, folder = "instructions")
#math_scale = nir.MathScale(win = win, participant_number = expInfo['participant'], scale = "AMAS")
#math_scale.run_scale()
#nir.isi(win)




# TEST TIMECOURSE

#timer = core.Clock()  
#eyetrack_timecourse = True

'''
sample_rate = 0.025
xPos_left = []
yPos_left = []
xPos_right = []
yPos_right = []
pDiam_left = []
pDiam_right = []
t_sample = []
t_num = []'''


#crt_trial = nir.WordProblem(win, terms = 4, term1='premise1', term2='premise2', term3='premise3', term4='conclusion',
                                option1='option1', option2='option2', option1_x=-0.7, option2_x=0.7, borders=True)
                                
#crt_trial.draw()
#event.clearEvents(eventType='keyboard')  # clear keyboard buffer
#win.flip()

#resp, rt = nir.timecourse_eyetracking(xPos_left, yPos_left, xPos_right, yPos_right, pDiam_left, pDiam_right, t_sample, t_num, sample_rate, key_list=None)  # ["a", "d"])
    # for the first "image", this would be reading time and any button press or whatever buttons I allow in the program (any would be best)
    

#read_image = "item1" + "_read"


#nir.save_to_image(win, read_image + 'read' )
 


#resp, rt = nir.get_keypress_resp(key_list=None) 
    

'''
timer.reset()
t0 = start = timer.getTime()
t1 = t0 + sample_rate
while eyetrack_timecourse:
    
    # get timestamp for current loop iteration
    timestamp = timer.getTime()
    
    # check for response
    key_press = event.getKeys(keyList = ["a", "d"])
    
    # if response given, end loop
    if len(key_press) > 0:
        RT = timer.getTime()
        eyetrack_timecourse = False
        
    # gather eye-tracking data here
    if timestamp > t1:
        t1 += sample_rate  # increment t1 by the sample rate
        t = timestamp - start
        x = 1
        xList_left.append(x)
        tList.append(t)'''


# arguments:
    # keylist is a list of keys to wait for
    # sample rate in ms
    # all the lists and just edit them inside?



'''
print xPos_left 
print xPos_right
print yPos_left
print yPos_right
print pDiam_left
print pDiam_right
print t_sample
print t_num
print str(len(xPos_left))
print resp
print rt'''





'''
# The eye tracking - STILL TESTING
t0 = start = exp.time()
t1 = t0 + sample_rate
#resp = 0 # MAYBE PUT THE KEYBOARD RESPONSE HERE SOMEHOW
#timed_out = False
#slow_start = False

# TESTING FOR NOW - a limit to the problem so the loop isn't infinite	
max_response_time = 50 # remove later


while 1: # NOTE - there needs to be some way to close this loop
	position_x, position_y = eyetracker.sample()
	timestamp = exp.time()
	if timestamp > t1:
	# then record eye position
		t1 += sample_rate
		t = timestamp - start
		x = position_x
		y = position_y
		#xList.append(x) # SAVE THESE 3 VALUES
		#yList.append(y)
		#tList.append(t)
		if t > max_response_time:
#			# Out of time, record a null response.
#			timed_out = True
#			resp = -1
#			rt = None
			print 'Timeout' # NOTE: this doesn't print anything here, not sure why
			break

# sample rate duration
sample_dur = core.StaticPeriod(screenHz=60)
sample_dur.start(0.025)  # start a period of 25 ms
sample_dur.complete()            
            
'''






'''
response_trial = nir.last_term_only(win, term='premise1')
response_trial.draw()
win.flip()
core.wait(0.5)
response_trial = nir.last_term_only(win, term='premise1', option1='option1', option2='option2')
response_trial.draw()
win.flip() 
event.waitKeys()'''




    


















# ---------------------------------------------
# ---- Instructions routine
# ---------------------------------------------









"""
    while not calibrated and attempts < max_attempts: 
        
        cali = iViewXAPI.iV_Calibrate()
        vali = iViewXAPI.iV_Validate()
        acc = iViewXAPI.iV_GetAccuracy(byref(accuracyData), 1)
        
        LX = accuracyData.deviationLX
        LY = accuracyData.deviationLY
        RX = accuracyData.deviationRX
        RY = accuracyData.deviationRY
        
        # create window to print results
        val_win = visual.Window(
                            size=(1920, 1200), fullscr=True, screen=0,
                            allowGUI=False, allowStencil=False,
                            monitor='testMonitor', color=u'black', colorSpace='rgb',
                            blendMode='avg', useFBO=True)
        
        if all( [LX < 1, LY < 1, RX < 1, RY < 1] ):
            calibrated = True
            
        attempts += 1
"""



"""




#RunInstructions(win, folder = "calibration_instructions", filename = 'cal_complete.txt')



# define a list of counterbalancing options
cb_list = [
]

# number of counterbalancing items
cb_num = len(cb_list)


# create an instance of the Participant class from library
participant = nir.Participant(expInfo['participant'], cb_num)
print(participant.p_num)
print(participant.cb)

# run the counterbalancer
nir.CounterBalancer(participant, cb_list)



#nir.CounterBalancer(1, 0)
"""


"""
conf_rating = nir.ConfidenceScale()

# conf_rating = PsyIRN.ConfidenceScale()


while conf_rating.noResponse:
    conf_rating.draw()
    win.flip()
confidence = conf_rating.getRating()
conf_rt = conf_rating.getRT()
"""

#y = os.getcwd() + "\\stimuli\\stimuli.csv"

#x = psychopy.data.importConditions(y, selection='0:2') 
#print x




#trials.addData('confidence', confidence)
#trials.addData('conf.rt', conf_rt)

#thisExp.nextEntry()


