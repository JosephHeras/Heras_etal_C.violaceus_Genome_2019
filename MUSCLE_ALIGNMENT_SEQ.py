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