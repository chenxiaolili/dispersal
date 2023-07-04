#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH -p C032M0128G
#SBATCH --qos=high
#SBATCH -J My_Job
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1

python shannon_index_adjusted-0.py
python shannon_index_adjusted-0.1.py
python shannon_index_adjusted-0.3.py
python shannon_index_adjusted-0.5.py
python shannon_index_adjusted-0.7.py
python shannon_index_adjusted-0.9.py
python shannon_index_adjusted-0.999.py
python shannon_index_adjusted-0.999999.py
python shannon_index_adjusted-1.py