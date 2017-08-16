#!/usr/bin/env python
import subprocess
import os
import sys 

"""
THIS FUNCTION USE SIGPROC TO READ THE BASIC PARAMETERS OF A .fil FILE 
by machos

RUN CONVENTION:
reader.py folder file.fil parameter

PARAMETERS:
fch1: Frequency of channel 1
foff: Channel Frequency in MHz
nchans: Number of channels
tstart: Time stamp of first sample (MJD)
tsamp: Sample time (us)
nbits: Number of bits per sample
tobs: Length of observation (s)
"""

def reader(pathtopulsar, parameter):

#folder = 'J0811+0225_PART1_8bit_allbeams'
#pulsar = '6729_0001'
	"""
	READ THE PARAMETERS
	"""
	fch1_string = subprocess.check_output("header %s -fch1" % (pathtopulsar), shell=True)
	fch1 = float(fch1_string)

	foff_string = subprocess.check_output("header %s -foff" % (pathtopulsar), shell=True)
	foff = float(foff_string)

	nchans_string = subprocess.check_output("header %s -nchans" % (pathtopulsar), shell=True)
	nchans = int(nchans_string)

	tstart_string = subprocess.check_output("header %s -tstart" % (pathtopulsar), shell=True)
	tstart = float(tstart_string)

	tsamp_string = subprocess.check_output("header %s -tsamp" % (pathtopulsar), shell=True)
	tsamp = float(tsamp_string)

	nbits_string = subprocess.check_output("header %s -nbits" % (pathtopulsar), shell=True)
	nbits = int(nbits_string)

	tobs_string = subprocess.check_output("header %s -tobs" % (pathtopulsar), shell=True)
	tobs = float(tobs_string)
	"""
	CHOOSE WHAT PARAMETER TO RETURN
	"""
	if parameter == "fch1":
		result = fch1
	elif parameter == "foff":
		result = foff
	elif parameter == "nchans":
		result = nchans
	elif parameter == "tstart":
		result = tstart
	elif parameter == "tsamp":
		result = tsamp
	elif parameter == "nbits":
		result = nbits
	elif parameter == "tobs":
		result = tobs
	else:
		print "Can't read parameter"

#print fch1, foff, nchans, tstart, tsamp, nbits, tobs
	return result

if __name__ == "__main__":
	pathtopulsar = sys.argv[1]
	parameter = sys.argv[2]
	y = reader(pathtopulsar, parameter)
	print y
