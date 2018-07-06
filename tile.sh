#!/bin/bash 
## Job Name 
#SBATCH --job-name=tile
## Resources 
## Nodes 
#SBATCH --nodes=4
## Tasks per node (Slurm assumes you want to run 28 tasks per node unless explicitly told otherwise)
#SBATCH --ntasks-per-node=28 
## Walltime (hr:min:sec) 
#SBATCH --time=700:00:00 
## Memory per node 
#SBATCH --mem=240G 
## Specify the working directory for this job 
#SBATCH --workdir=/gscratch/choe/dssg/data 
#SBATCH --mail-type=ALL 

module load anaconda3_4.3.1
source activate dssg

python tileTiff.py mosaic.tif mosaic_tiles 
