# nir
A suite of functions for use with Psychopy experiments.

## Usage
The nir library assumes the use of default experiment handler and trial handler functions from Psychopy. 

## Eye-tracking
```python
nir.run_calibration(participant=1, max=10, deviation=1)  # calibrates the SMI eye-tracker
# participant = participant number
# max = maximum number of calibration attempts
# deviation = maximum allowable horizontal or vertical deviation (in degrees) from the calibration target for each eye
```
