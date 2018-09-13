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


# general functions
from .rating_scales import *
from .load_stimuli import *
from .run_instructions import *
from .counterbalance import *
from .isi import *
from .get_responses import *
from .save_to_file import *

# reasoning tasks
from .word_problems import *
from .ratio_bias import *

# eye-tracking
from .eye import *

# follow-up tests
from .math_anxiety import *


"""
Coming:

1. Tasks
    c. water jugs
    d. anagrams
    e. numerical cognition tasks

2. follow-up
    a. Markovits diagnostic
    
3. other
    a. clickable sitmuli
    b. mouse tracking
    c. other response scale options

"""