from suite2p import run_s2p, default_ops
import json
import sys
import os


# set your options for running
ops = default_ops() # populates ops with the default options


# VARIABLES TO SET
OPS_FILE_NAME = 'ops_1P_whole.json'


## Load s2p file
with open(OPS_FILE_NAME, 'r') as fp:
    input_ops = json.loads(fp.read())
ops.update(input_ops)


## Define the db
db = {'look_one_level_down': True, # whether to look in ALL subfolders when searching for tiffs
    'data_path': [ops.get('fish_input_path')], # a list of folders with tiffs 
                                            # (or folder of folders with tiffs if look_one_level_down is True, or subfolders is not empty)         
    'fast_disk': ops.get('fish_output_path'),
    'save_folder': ops.get('fish_output_path'),
}


## For logging and debugging
print(f'OPS FILE: {OPS_FILE_NAME}\ninput_ops: {input_ops}\n')


# Run suite2p
run_s2p(ops=ops, db=db)