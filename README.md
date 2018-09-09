# nir
A suite of functions for use with Psychopy experiments. v0.1
(the readme will be updated in the near future)

## Project Status
In development.

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
nir.run_calibration(participant=1, max=10, deviation=1)  # calibrates the SMI eye-tracker
# participant = participant number
# max = maximum number of calibration attempts
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
