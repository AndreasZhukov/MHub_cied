"""
-------------------------------------------------
MedicalHub - Apply a simple thresholding operation 
            to an input image for testing.
-------------------------------------------------

-------------------------------------------------
Author: Leonard Nürnberg
Email:  leonard.nuernberg@maastrichtuniversity.nl
-------------------------------------------------
"""

import sys, os
sys.path.append('.')

from mhubio.core import Config, DataType, FileType, CT, SEG
from mhubio.modules.importer.NrrdImporter import NrrdImporter
from mhubio.modules.organizer.DataOrganizer import DataOrganizer
from models.thresholder.utils.ThresholdingRunner import ThresholdingRunner

# clean-up
#import shutil
#shutil.rmtree("/app/data/sorted", ignore_errors=True)
#shutil.rmtree("/app/data/nifti", ignore_errors=True)
#shutil.rmtree("/app/tmp", ignore_errors=True)
#shutil.rmtree("/app/data/output_data", ignore_errors=True) # <-- we use in = out so not a good idea :D

# config
config = Config('/app/models/thresholder/config/config.yml')
config.verbose = True  # TODO: define levels of verbosity and integrate consistently. 
config.debug = True

# load NRRD file (ct:nrrd)
NrrdImporter(config).execute()

# execute model (ct:nrrd -> seg:nrrd)
ThresholdingRunner(config).execute()

# organize data into output folder
organizer = DataOrganizer(config, set_file_permissions=sys.platform.startswith('linux'))
organizer.setTarget(DataType(FileType.NRRD, SEG), "/app/data/output_data/output.nrrd")
organizer.execute()