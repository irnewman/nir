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

def run_calibration(participant=0, max_tries=10, deviation=1):

    """
        Function: connect to SMI eye-tracker, calibrate, validate, and create log file
        Arguments:
            participant = current participant number
            max_tries = maximum calibration attempts
            deviation = acceptable horizontal and vertical deviation from the target
    """

    # variables
    calibrated = False
    attempts = 1
    max_attempts = max_tries
    calibration_deviation = deviation

    # set up the log file
    calibration_dir = os.getcwd()
    calibration_filename = calibration_dir + os.sep + "data" + os.sep + str(participant) + "_calibration" + ".txt"
    calibration_log = open(calibration_filename, 'w')
    res = iViewXAPI.iV_SetLogger(c_int(1), c_char_p(str(participant) + "_log.txt"))

    # connect to iViewX
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
    """
    Arguments:
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
    calibrationData = CCalibration(5, 1, 0, 0, 1, 250, 0, 2, 20, b"")
    res = iViewXAPI.iV_SetupCalibration(byref(calibrationData))
    calibration_log.write("Setup Calibration: " + str(res) + "\n")

    # calibrate eye-tracker within accepted deviation
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
            iViewXAPI.iV_GetSample(byref(sampleData))
            t1 += sample_rate  # increment t1 by the sample rate
            t = timestamp - start
            xPos_left.append(sampleData.leftEye.gazeX)
            xPos_right.append(sampleData.rightEye.gazeX)
            yPos_left.append(sampleData.leftEye.gazeY)
            yPos_right.append(sampleData.rightEye.gazeY)
            pDiam_left.append(sampleData.leftEye.diam)
            pDiam_right.append(sampleData.rightEye.diam)
            t_sample.append(t)
            t_num.append(counter)
            counter += 1
            
    return key_press, rt



# unused:
    # left_eye = CEye(0,0,0)
    # right_eye = CEye(0,0,0)
    # eye_sample = CSample(0,left_eye,right_eye,0)
    # position_x_left = eye_sample.leftEye.gazeX
    # print "position x left: " + str(position_x_left)
    # iViewXAPI.iV_GetSample(byref(sampleData))
    # position_x_left = sampleData.leftEye.gazeX
    # print "position x left: " + str(position_x_left)

    # key_pressed = psychopy.event.waitKeys(keyList=["left", "right"])
    # change to getkeys loop, possibly all within a function call
    # it would take the lists and the sample rate as arguments (so 9 arguments already, plus maybe the sample data)

    # xPos_left.append(sampleData.leftEye.gazeX)
    # xPos_right.append(sampleData.rightEye.gazeX)
    # yPos_left.append(sampleData.leftEye.gazeY)
    # yPos_right.append(sampleData.rightEye.gazeY)
    # pDiam_left.append(sampleData.leftEye.diam)
    # pDiam_right.append(sampleData.rightEye.diam)
    # t_sample.append(t0)
    # t_num.append(counter)

    '''while len(key_pressed) < 1:  # add counter with t_number (0 to N)

        # sample 
        #eye_sample = iV_GetSample()

        # diam = pupil diamter, gazeX/Y = position on screen
        position_x_left = eye_sample.leftEye.gazeX
        print "position x left: " + position_x_left

        position_y_left = eye_sample.leftEye.gazeY
        position_x_right = eye_sample.rightEye.gazeX
        position_y_right = eye_sample.rightEye.gazeY
        diameter_pupil_left = eye_sample.leftEye.diam
        diameter_pupil_right = eye_sample.rightEye.diam

        timestamp = trialClock.getTime()  # iV_GetCurrentTimestamp()
        t_num = counter

        #if timestamp > t1:  # not sure if this if statement is strictly necessary yet (may be redundant code here)
        t1 += sample_rate
        t = timestamp - start
        x_left = position_x_left
        x_right = position_x_right
        y_left = position_y_left
        y_right = position_y_right
        pd_left = diameter_pupil_left
        pd_right = diameter_pupil_right

        xList_left.append(x_left)
        xList_right.append(x_right)
        yList_left.append(y_left)
        yList_right.append(y_right)
        pList_left.append(pd_left)
        pList_right.append(pd_right)
        tList.append(t)
        tList_num.append(t_num)
            # THEN: save these arrays to the trial handler

        counter += 1'''