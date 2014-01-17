# -*- coding: utf-8 -*-
# Filename: XradiaConverter.py
""" Main program for convert SLS data into dataExchange.
"""
import dataio.data_spe as spe
from dataio.data_exchange import DataExchangeFile, DataExchangeEntry

import numpy as np
import os

import scipy

from dataio.data_convert import Convert

import re

#def main():

file_name = '/local/data/databank/APS_13_BM/run2_soln1_2_2.SPE'
white_file_name = '/local/data/databank/APS_13_BM/run2_soln1_2_1.SPE'
hdf5_file_name = '/local/data/databank/dataExchange/microCT/run2_soln1_3.h5'
# log_file = '/local/data/databank/dataExchange/TXM/20130731_004_Stripe_Solder_Sample_Tip1.log'

verbose = True

if verbose: print file_name
if verbose: print white_file_name
if verbose: print hdf5_file_name
#if verbose: print log_file

mydata = Convert()
# Create minimal hdf5 file
if verbose: print "Reading data ... "
mydata.single_stack(file_name,
               hdf5_file_name = hdf5_file_name,
               projections_data_type='SPE',
               white_file_name = white_file_name,
               white_data_type='SPE',
               #sample_name = 'Stripe_Solder_Sample_Tip1'
               )
if verbose: print "Done reading data ... "

 
# Add extra metadata if available

##if verbose: print "Adding extra metadata ..."
##reader = xradia.xrm()
##array = dstruct
##reader.read_txrm(file_name,array)
##
### Read angles
##n_angles = np.shape(array.exchange.angles)
##if verbose: print "Done reading ", n_angles, " angles"
##theta = np.zeros(n_angles)
##theta = array.exchange.angles[:]



# Open DataExchange file
f = DataExchangeFile(hdf5_file_name, mode='a') 

# Create HDF5 subgroup
# /measurement/instrument
f.add_entry( DataExchangeEntry.instrument(name={'value': 'APS 13-BM'}) )

### Create HDF5 subgroup
### /measurement/instrument/source
f.add_entry( DataExchangeEntry.source(name={'value': "Advanced Photon Source"},
                                    date_time={'value': "2013-11-30T19:17:04+0100"},
                                    beamline={'value': "13-BM"},
                                    )
)

# Create HDF5 subgroup
# /measurement/experimenter
f.add_entry( DataExchangeEntry.experimenter(name={'value':"Mark Rivers"},
                                            role={'value':"Project PI"},
                )
    )

f.close()
if verbose: print "Done converting ", file_name

###if __name__ == "__main__":
###    main()

