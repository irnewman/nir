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

from psychopy import visual, core, event  # sound, gui, data, logging
import os
# import sys
# import csv
# from itertools import product

# eye-tracking libraries
from iViewXAPI import *  # iViewX library
from iViewXAPIReturnCodes import *

# ---------------------------------------------


# ---------------------------------------------
# ---- RunCalibration (not totally finished: change calibration arguments and file logging)
# ---------------------------------------------

def run_calibration(participant=0, max=10, deviation=1):

    """
        Function: connect to SMI eye-tracker, calibrate, validate, and create log file
        Arguments:
            participant = current participant number
            max = maximum calibration attempts
            deviation = acceptable horizontal and vertical deviation from the target
    """

    # variables
    calibrated = False
    attempts = 1
    max_attempts = max
    calibration_deviation = deviation

    # set up the log file
    calibration_dir = os.getcwd()
    calibration_filename = calibration_dir + os.sep + "P" + str(participant) + ".txt"
    calibration_log = open(calibration_filename, 'w')

    # to do:
    # cur_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep + folder
    # save the logfile to the data folder (currently goes to the main program folder)
    # overwrites the file with the same name - maybe change
    # alternative: use 'x' in open(calibration_filename, 'w'), then it will fail if the file already exists

    # connect to iViewX - set logfile name to something else (add argument expname or something)
    res = iViewXAPI.iV_SetLogger(c_int(1), c_char_p("temp_CRT.txt"))
    """use this somehow"""


    res = iViewXAPI.iV_Connect(c_char_p('127.0.0.1'), c_int(4444), c_char_p('127.0.0.1'), c_int(5555))
    if res != 1:
        HandleError(res)
        exit(0)

    # log system info
    res = iViewXAPI.iV_GetSystemInfo(byref(systemData))
    calibration_log.write("iV_GetSystemInfo: " + str(res) + "\n")
    calibration_log.write("Samplerate: " + str(systemData.samplerate) + "\n")
    calibration_log.write(
        "iViewX Version: " + str(systemData.iV_MajorVersion) + "." + str(systemData.iV_MinorVersion) + "." + str(
            systemData.iV_Buildnumber) + "\n")
    calibration_log.write(
        "iViewX API Version: " + str(systemData.API_MajorVersion) + "." + str(systemData.API_MinorVersion) + "." + str(
            systemData.API_Buildnumber) + "\n")

    # create calibration parameters
    calibrationData = CCalibration(5, 1, 0, 0, 1, 250, 0, 2, 20, b"")
    res = iViewXAPI.iV_SetupCalibration(byref(calibrationData))
    calibration_log.write("Setup Calibration: " + str(res) + "\n")
    """
    Arguments: (change these to variables)
    
    1. method
    2. visualization
    3. display device
    4. speed
    5. autoaccept
    6. foreground brightness
    7. background brightness
    8. target shape
    9. target size
    10. target filename
    """

    while not calibrated and attempts < max_attempts:

        cali = iViewXAPI.iV_Calibrate()
        vali = iViewXAPI.iV_Validate()
        acc = iViewXAPI.iV_GetAccuracy(byref(accuracyData), 1)

        LX = accuracyData.deviationLX
        LY = accuracyData.deviationLY
        RX = accuracyData.deviationRX
        RY = accuracyData.deviationRY

        if all([
            LX < calibration_deviation,
            LY < calibration_deviation,
            RX < calibration_deviation,
            RY < calibration_deviation,
            LX > 0.0,
            LY > 0.0,
            RX > 0.0,
            RY > 0.0
        ]):
            calibrated = True

        # create window to print results
        calibration_win = visual.Window(
            size=(1920, 1200), fullscr=True, screen=0,
            allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=u'black', colorSpace='rgb',
            blendMode='avg', useFBO=True)

        calibration_text = ("Deviation left x: " + str(LX) + "\n"
                            "Deviation left y: " + str(LY) + "\n"
                            "Deviation right x: " + str(RX) + "\n"
                            "Deviation right y: " + str(RY) + "\n\n\n"
                            "Calibration Success: " + str(calibrated)
                            )

        calibration_rerun_text = ("Calibration will begin again shortly.\n\n"
                                  "Please remain as still as possible. Do your best to focus directly on the dot.\n\n\n"
                                  "Attempts remaining: " + str(max_attempts - attempts)
                                  )

        calibration_results = visual.TextStim(win=calibration_win,
                                              text=calibration_text,
                                              pos=(0, 0.25),
                                              height=0.075,
                                              color=u'white', colorSpace='rgb',
                                              wrapWidth=1.5)

        calibration_rerun = visual.TextStim(win=calibration_win,
                                            text=calibration_rerun_text,
                                            pos=(0, 0.25),
                                            height=0.075,
                                            color=u'white', colorSpace='rgb',
                                            wrapWidth=1.5)

        # display results to screen
        calibration_results.draw()
        calibration_win.flip()
        core.wait(5)

        if not calibrated:
            calibration_rerun.draw()
            calibration_win.flip()
            core.wait(5)

        calibration_win.close()
        attempts += 1

    # write to log file
    if calibrated:
        calibration_log.write("Calibration Success: " + str(cali) + "\n")
        calibration_log.write("Validation Success: " + str(vali) + "\n")
        calibration_log.write("Accuracy: " + str(acc) + "\n")
        calibration_log.write("deviationXLeft: " + str(accuracyData.deviationLX) + "\n")
        calibration_log.write("deviationYLeft: " + str(accuracyData.deviationLY) + "\n")
        calibration_log.write("deviationXRight: " + str(accuracyData.deviationRX) + "\n")
        calibration_log.write("deviationYRight: " + str(accuracyData.deviationRY) + "\n")
        res = iViewXAPI.iV_ShowTrackingMonitor()
        calibration_log.write("Tracking Monitor: " + str(res) + "\n")
        calibration_log.close()


# ---------------------------------------------


def timecourse_eyetracking(xPos_left, yPos_left, xPos_right, yPos_right,
                           pDiam_left, pDiam_right, t_sample, t_num, sample_rate, key_list):

    eyetrack_timecourse = True
    counter = 1
    event.clearEvents(eventType='keyboard')  # clear keyboard buffer
    
    # init timer
    timer = core.Clock()  
    timer.reset()
    t0 = start = timer.getTime()
    t1 = t0 + sample_rate
    rt = 0
    key_press = event.BuilderKeyResponse()

    while eyetrack_timecourse:
    
        # get timestamp for current loop iteration
        timestamp = timer.getTime()
        
        # check for response
        key_press = event.getKeys(keyList=key_list)
        
        # if response given, end loop
        if len(key_press) > 0:
            rt = timer.getTime()
            eyetrack_timecourse = False
            
        # gather eye-tracking data here
        if timestamp > t1:
            t1 += sample_rate  # increment t1 by the sample rate
            t = timestamp - start
            xPos_left.append(0)  # (sampleData.leftEye.gazeX)
            xPos_right.append(0)  # (sampleData.rightEye.gazeX)
            yPos_left.append(0)  # (sampleData.leftEye.gazeY)
            yPos_right.append(0)  # (sampleData.rightEye.gazeY)
            pDiam_left.append(0)  # (sampleData.leftEye.diam)
            pDiam_right.append(0)  # (sampleData.rightEye.diam)
            t_sample.append(t)
            t_num.append(counter)
            counter += 1
            
    return key_press, rt






"""
EYE-Tracking notes

If you want to put the whole task into the library:
    1. boolean argument for eye-tracking
    2. if true:
            a. run calibration and connection
            b. start recording
            c. send image every trial
                i. need to have image column in the stimuli file then
            d. pause recording where necessary
            e. run online-measure routine on each trial
            f. close connection
            g. save the data
"""

# maybe
# evenntually define a drift correction function (test with begaze first before trying that)
# a setting to re-calibrate and re-open the file with 'a' instead of 'w' (append instead of write)
