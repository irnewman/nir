# nir v0.1.3.1
A suite of functions for use with Psychopy experiments.

## Project Status
On hold. Due to the COVID-19 pandemic, use of in person testing (in particular, eye-tracking methodology) has been greatly limited. As such, development of this library is suspended indefinitely.

## Support
Contact Ian Newman at ian.newman@usask.ca with questions or comments.

## Features
Simplifies several elements of creating and running psychology experiments (particularly reasoning and metacogitive), including the use of eye-tracking measures (only SMI eye-trackers currently).

## Requirements
Python and Psychopy. 

## Installation
Download and extract the nir folder to the same directory as your experiment script.

## Usage
The nir library assumes the use of default experiment handler and trial handler functions from Psychopy. See the nir_template.py file.

### counterbalance.py

### eye.py
```python
nir.run_calibration(participant=1, max_tries=10, deviation=1)  # calibrates the SMI eye-tracker
# participant = participant number
# max_tries = maximum number of calibration attempts
# deviation = maximum allowable horizontal or vertical deviation (in degrees) from the calibration target
```

### get_responses.py

### isi.py

### load_stimuli.py

### math_anxiety.py

### rating_scales.py

### ratio_bias.py

### run_instructions.py

### save_to_file.py

### word_problems.py
