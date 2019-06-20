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


