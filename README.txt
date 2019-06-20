MUSCLE_ALIGNMENT_SEQ.py

from sys import argv 

import os




script, filename = argv

f = open(filename)

for line in f:

   line = line.rstrip('\n')

   cmd1 = "muscle -seqtype protein -in %r -out %r.muscle.fasta" % (line, line)

   print cmd1

   os.system(cmd1)
       


f.close()


ORTHO3.sh


#!/bin/bash

#$ -N MUSCLE

#$ -q free*,pub64,german

#$ -pe openmp 8-64

#$ -m beas



module load muscle/3.8

module load blast/2.2.22




python ALIGNMENT_SEQ.py FINAL.LIST.txt


#with pal2nal

from sys import argv
import os

script, filename = argv
f = open(filename)
for line in f:
   line = line.rstrip('\n')
   cmd1 = 'perl pal2nal.pl %r -output fasta > pal2nal_%r' % (line, line)
   print cmd1
   os.system(cmd1)

f.close()

#command
python ALIGNMENT_SEQ.py PROT_NUC_List.txt

#single
perl pal2nal.pl PROT_ORTHO869_BLAST.txt.fasta.muscle.fasta NUC_ORTHO869_BLAST.txt.fasta -output fasta > test.pal