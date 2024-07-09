#!/bin/bash -l
#Edit this script to suit your purposes
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=1000G
#SBATCH --job-name=Bunya_AutoEncode
#SBATCH --time=40:00:00
#SBATCH --partition=general
#SBATCH --account=a_rahimi
#SBATCH -o SpaceLinClassiferOut.txt
#SBATCH -e SpaceLinClassifierError.txt


module load anaconda3/2022.05
source /sw/auto/rocky8.6/epyc3/software/Anaconda3/2022.05/etc/profile.d/conda.sh
conda activate myenv
cd /scratch/user/benwalters/Morse\ Code\ Dataset

python LinClass.py