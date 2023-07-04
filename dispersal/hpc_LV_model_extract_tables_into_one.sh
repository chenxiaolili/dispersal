#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH -p C032M0128G
#SBATCH --qos=high
#SBATCH -J My_Job
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1

python Extract_multiple_tables_into_one-0.py
python Extract_multiple_tables_into_one-0.1.py
python Extract_multiple_tables_into_one-0.3.py
python Extract_multiple_tables_into_one-0.5.py
python Extract_multiple_tables_into_one-0.7.py
python Extract_multiple_tables_into_one-0.9.py
python Extract_multiple_tables_into_one-0.999.py
python Extract_multiple_tables_into_one-0.999999.py
python Extract_multiple_tables_into_one-1.py