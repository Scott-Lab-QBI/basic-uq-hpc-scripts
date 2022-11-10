# basic-uq-hpc-scripts
A collection of scripts for processing calcium imaging data using the University of Queenslands HPC infrastructure.

# Main steps in processing data
- Connecting to / using HPC
- Run Suite2p
- Run ANTs
- Load data
- Create ANTs template

# Initial installation
- For now I will assume ANTs and Suite2p are installed already
- To initially install this repository log on the HPC (described below) then run
```
git clone https://github.com/Scott-Lab-QBI/basic-uq-hpc-scripts.git
```

# Connecting to the HPC
- Open Acaconda prompt
- Type (or copy and paste) the following into anaconda prompt
```
ssh <uqusername>@flashlight.rcc.uq.edu.au
```
- Replace `<uqusername>` with your uq username (e.g. uqjsmith or s4323534)
- If Bunya has been installed, replace the link to `flashlight.rcc.uq.edu.au` with the new link to bunya.
- Alternatively you can use VSCode instead of anaconda prompt but I will not supply instructions for that here


# Run Suite2p
- Log into the HPC
- Access to all RDP drives on the HPC is through the `/QRISdata/` directory. e.g. Q4414 (the pipeline drive) is located at `/QRISdata/Q4414/`.
- Find the fish that you wish to run Suite2p on in your RDM drive, you can use the ls command to list files in a directory e.g.
```
ls /QRISdata/Q4414/
```
- Update the path to fish data and other parameters in the ops file (default is `ops_1P_whole.json`)
- Update the job name and other run parameters in the `suite2p_hpc.pbs` file (optional)
- Submit the job file to the HPC queue
```
qsub suite2p_hpc.pbs
```
- To check the status of jobs you can use `qstat`


# Run ANTs
- log onto hpc
- Edit variables to set at top of `run_ANTs.pbs` script
- Launch job
```
qsub run_ANTs.pbs
```

# Create ANTs template



# Help disaster!?
- Contact Josh, even after I've left I will be happy to help with small quick fixes / questions