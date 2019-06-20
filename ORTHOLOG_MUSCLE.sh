#!/bin/bash

#$ -N MUSCLE

#$ -q free*,pub64,german

#$ -pe openmp 8-64

#$ -m beas



module load muscle/3.8

module load blast/2.2.22

python ALIGNMENT_SEQ.py FINAL.LIST.txt


