#!/bin/bash -l
#Edit this script to suit your purposes
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=500G
#SBATCH --job-name=MCode
#SBATCH --time=2:00:00
#SBATCH --partition=general
#SBATCH --qos=normal
#SBATCH --account=a_rahimi
#SBATCH -o DatasetGeneratorOut.output
#SBATCH -e DatasetGeneratorError.error


module load anaconda3/2022.05
source $EBROOTANACONDA3/etc/profile.d/conda.sh
conda activate myenv
export PATH=/home/benwalters/.conda/envs/myenv/bin:$PATH
export PYTHONPATH=/home/benwalters/.conda/envs/myenv/lib/python3.11/site-packages:$PYTHONPATH
cd /scratch/user/benwalters/Morse\ Code\ Dataset

python NeuroMorse/Dataset\ Generation/DatasetGenerator.py