

# ---------------------------------------------
# ---- Planned Additions
# ---------------------------------------------

"""
-readme file(s), other documentation
-response gathering functions
-save as image function
-tasks:
    -WMC
    -strategy diagnostic
    -water jug task updated
-R: create an R package that cleans the output of these tasks

"""

# potential features to add
"""
rating = ratingScale.getRating()
decisionTime = ratingScale.getRT()
choiceHistory = ratingScale.getHistory()

#check for quit (the [Esc] key)
if event.getKeys(["escape"]): core.quit()

"""

# ---------------------------------------------









# incomplete
'''
def save_as_file(canvas, filename, buffer='front'):
    """ Save the contents of the current screenbuffer to an image file.

	Parameters
	----------
	canvas : openexp.Canvas
		The canvas object to save the image from

	filename : string
		The location and filenam to save the image to. If an absolute path is
		provided, the file will be saved there. If a relative path is provided,
		the file will be saved to that folder relative to the location of the
		experiment file

	buffer : string, default 'front'
		Only relevant when using the psychopy backend. Indicates whether the
		front buffer or back buffer should be saved, so this value should be
		'front' or 'back'

	Returns
	-------
	string : The full path to the file that has just been saved

	Raises
	------
	libopensesame.exceptions.osexception if an incorrect file format or buffer
	value have been provided
	"""
    import os
    from libopensesame.exceptions import osexception

    # Check if supplied filename has a valid image extension
    if not os.path.splitext(filename)[1] in ['.jpg', '.jpeg', '.png', '.bmp' or '.tga']:
        raise osexception("The filename does not have a valid image extension. Use .jpg, .jpeg, .png, .bmp or .tga")

    if not buffer in ['front', 'back']:
        raise osexception("Invalid buffer value; the only options are 'front' or 'back'.")

    # Check if image file path is absolute, if not, find relative path to current experiment file
    if not os.path.isabs(filename):
        filename = os.path.abspath(os.path.join(self.experiment.experiment_path, filename))

    # Create any subfolders if necessary
    file_dir = os.path.dirname(filename)
    if not os.path.isdir(file_dir):
        os.makedirs(file_dir)

    # Backend specific saving of canvas to image file
    if self.experiment.get("canvas_backend") == "legacy":
        import pygame
        pygame.image.save(canvas.surface, filename)
    elif self.experiment.get("canvas_backend") == "xpyriment":
        canvas._canvas.save(filename)
    elif self.experiment.get("canvas_backend") == "psycho":
        win.getMovieFrame(buffer)
        win.saveMovieFrames(filename)

    # Return the abspath of the saved file (to easily reference it later)
    return filename
'''

























'''what are the arguments to this function?'''  # check this
# presumably, these are the number of points of calibration and x,y coords, and such?
# see documentation
''' basically, instead of print statements, would draw to window'''
# and save to a file as well? see what pygaze saves in smilog


# do the below, except write to file instead
"""
xres = iViewXAPI.iV_SetupCalibration(byref(calibrationData))
print
"iV_SetupCalibration " + str(res)
xres = iViewXAPI.iV_Calibrate()
print
"iV_Calibrate " + str(res)

res = iViewXAPI.iV_Validate()
print
"iV_Validate " + str(res)

res = iViewXAPI.iV_GetAccuracy(byref(accuracyData), 1)
print
"iV_GetAccuracy " + str(res)
print
"deviationXLeft " + str(accuracyData.deviationLX) + " deviationYLeft " + str(accuracyData.deviationLY)
print
"deviationXRight " + str(accuracyData.deviationRX) + " deviationYRight " + str(accuracyData.deviationRY)

res = iViewXAPI.iV_ShowTrackingMonitor()
print
"iV_ShowTrackingMonitor " + str(res)
"""


# 3.3 INCOMPLETE
# ---------------------------------------------
# ---- Water Jug Stimuli
# ---------------------------------------------


# IN PROGRESS
# ---------------------------------------------
# ---- Image Maker
# ---------------------------------------------


# I didn't write the below, but I will probably rewrite it myself

# then in the program, set a boolean and if statement, where if true:
# then capture the screen as a file
# could also comment it out after





# INCOMPLETE
# ---------------------------------------------
# ---- Eye/Mouse Online Tracker
# ---------------------------------------------


"""
    # create the premises for current trial
    p1 = visual.TextStim(win=win, name='text',
                        text=thisTrial['premise1'],
                        font=u'Arial',
                        pos=(0, 0.8), height=0.1, wrapWidth=text_width, ori=0,
                        color=u'white', colorSpace='rgb', opacity=1,
                        depth=0.0)
    p2 = visual.TextStim(win=win, name='text',
                        text=thisTrial['premise2'],
                        font=u'Arial',
                        pos=(0, 0.5), height=0.1, wrapWidth=text_width, ori=0,
                        color=u'white', colorSpace='rgb', opacity=1,
                        depth=0.0)
    p3 = visual.TextStim(win=win, name='text',
                        text=thisTrial['premise3'],
                        font=u'Arial',
                        pos=(0, 0.2), height=0.1, wrapWidth=text_width, ori=0,
                        color=u'white', colorSpace='rgb', opacity=1,
                        depth=0.0)
    c = visual.TextStim(win=win, name='text',
                        text=thisTrial['conclusion'],
                        font=u'Arial',
                        pos=(0, -0.1), height=0.1, wrapWidth=text_width, ori=0,
                        color=u'white', colorSpace='rgb', opacity=1,
                        depth=0.0)

    # create the response options for current trial
    option1 = visual.TextStim(win=win, name='text',
                                    text=thisTrial['option1'],
                                    font=u'Arial',
                                    pos=(option1_x, -0.75), height=0.1, wrapWidth=None, ori=0,
                                    color=u'white', colorSpace='rgb', opacity=1,
                                    depth=0.0)
    option2 = visual.TextStim(win=win, name='text',
                                text=thisTrial['option2'],
                                font=u'Arial',
                                pos=(option2_x, -0.75), height=0.1, wrapWidth=None, ori=0,
                                color=u'white', colorSpace='rgb', opacity=1,
                                depth=0.0)

    # create the borders (plan to remove these after the images are taken)
        # can make this a boolean T/F for whether to draw them or not
    p1border = visual.Rect(win=win,
                           pos=(0, 0.8),
                           width=border_width,
                           height=0.25)
    p2border = visual.Rect(win=win,
                           pos=(0, 0.5),
                           width=border_width,
                           height=0.25)
    p3border = visual.Rect(win=win,
                           pos=(0, 0.2),
                           width=border_width,
                           height=0.25)
    cborder = visual.Rect(win=win,
                      pos=(0, -0.1),
                      width=border_width,
                      height=0.25)
    option1_border = visual.Rect(win=win,
                             pos=(option1_x, -0.75),
                             width=answer_width,
                             height=0.25)
    option2_border = visual.Rect(win=win,
                          pos=(option2_x, -0.75),
                          width=answer_width,
                          height=0.25)

    # draw the text and borders
    p1.draw()
    p2.draw()
    p3.draw()
    c.draw()
    p1border.draw()
    p2border.draw()
    p3border.draw()
    cborder.draw()
    option1.draw()
    option1_border.draw()
    option2.draw()
    option2_border.draw()
    
"""
