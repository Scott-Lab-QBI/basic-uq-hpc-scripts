# basic-uq-hpc-scripts
A collection of scripts for processing calcium imaging data using the University of Queenslands HPC infrastructure.

# Main steps in processing data
- Connecting to / using HPC
- Run Suite2p
- Run ANTs

# Initial installation
- For now I will assume ANTs and Suite2p are installed already
- To initially install this repository log on the HPC (described below) then run
```
git clone https://github.com/Scott-Lab-QBI/basic-uq-hpc-scripts.git
```

## A few one of things to change
- Update line 5 of suite2p_hpc.pbs with your school name (it is likely one of: `UQ-QBI`, `UQ-SCI-SBMS` or `UQ-EAIT-ITEE`), use the `groups` command to see which group you belong to. 

# Connecting to the HPC
- Open Acaconda (or Powershell) prompt
- Type (or copy and paste) the following into anaconda prompt
```
ssh <uqusername>@tinaroo.rcc.uq.edu.au
```
- Replace `<uqusername>` with your uq username (e.g. uqjsmith or s4323534)
- If Bunya has been installed, replace the link to `tinaroo.rcc.uq.edu.au` with the new link to bunya.
- Alternatively, you can use VSCode, wsl, Putty or any other ssh client instead of anaconda prompt but I will not supply instructions for those here.


# Run Suite2p
- Log into the HPC
- Change directory into code folder 
```
cd basic-uq-hpc-scripts
```
- Access to all RDP drives on the HPC is through the `/QRISdata/` directory. e.g. Q4414 (the pipeline drive) is located at `/QRISdata/Q4414/`.
- Find the fish that you wish to run Suite2p on in your RDM drive, you can use the ls command to list files in a directory e.g.
```
ls /QRISdata/Q4414/
```
- Update the `fish_input_path` and `fish_output_path` parameters in the ops file (default is `ops_1P_whole.json`)
- A full path to a fish might look like
```
/QRISdata/Q2396/SPIM_120170/Spontaneous/AG_PipelineAuditory_20200910_scn1lab_fish01_spon_2Hz_range245_step5_exposure10_power60_range245_step5_exposure10_power60/
```
- Update the job name and other HPC parameters in the `suite2p_hpc.pbs` file (optional)
- Submit the job file to the HPC queue
```
qsub suite2p_hpc.pbs
```
- To check the status of jobs you can use `qstat`
- The HPC will log any errors in files in the HPC home directory, you can review these when things don't work.


# Run ANTs
- log onto hpc
- Change directory into code folder 
```
cd basic-uq-hpc-scripts
```
- Edit variables to set at top of `run_ANTs.pbs` script
- Note: filenames must have a step size in the filenames or ANTs will fail.
- Launch job
```
qsub run_ANTs.pbs
```
- As with suite2p `qstat` to check the state of a running (or queued) job, output and errors will be written to the HPC home directory


# Check suite2p ran correctly
- log onto hpc
- Change directory into code folder 
```
cd basic-uq-hpc-scripts
```
- Run the `write_fish_stats.py` file
```
python write_fish_stats.py <suite2p_output_path>
```
- Where `<suite2p_output_path>` is the folder of suite2p output for a single fish
- This file will create a text file in that suite2p output folder details the stats for each of the planes

# Kill a job
- log onto hpc
- Find the job number with command "qstat"
- Kill the job with command "qsub"

```
qsub JOBNUMBER
```
