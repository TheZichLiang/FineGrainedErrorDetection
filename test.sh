#!/bin/bash

# Lines that begin with #SBATCH specify commands to be used by SLURM for scheduling

#SBATCH --job-name=CometKiwiTest                                     # sets the job name
#SBATCH --output=cometKiwiTest.out                                   # indicates a file to redirect STDOUT to; %j is the jobid. If set, must be set to a file instead of a directory or else submission will fail.
#SBATCH --error=cometKiwiTest.err                                    # indicates a file to redirect STDERR to; %j is the jobid. If set, must be set to a file instead of a directory or else submission will fail.
#SBATCH --time=01:00:00                                              # how long you would like your job to run; format=dd-hh:mm:ss
#SBATCH --qos=default                                                # set QOS, this will determine what resources can be requested
#SBATCH --nodes=2                                                    # number of nodes to allocate for your job
#SBATCH --ntasks=4                                                   # request 4 cpu cores be reserved for your node total
#SBATCH --ntasks-per-node=2                                          # request 2 cpu cores be reserved per node
#SBATCH --mem=1g                                                     # memory required by job; if unit is not specified MB will be assumed. for multi-node jobs, this argument allocates this much memory *per node*

srun --nodes=1 --mem=512m bash -c "hostname; python3 --version" &    # use srun to invoke commands within your job; using an '&'
srun --nodes=1 --mem=512m bash -c "hostname; python3 --version" &    # will background the process allowing them to run concurrently
wait                                                                 # wait for any background processes to complete

# once the end of the batch script is reached your job allocation will be revoked