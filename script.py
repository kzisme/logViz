import sys
import glob
import os
import re

path = '/home/kzisme/irclogs/blackbox/*'
filesToParse = os.listdir(path)

logFiles = {
        "blackbox-2016-05-09"
}


files = glob.glob(path)
for log in logs:
    file = os.path.join(path, file)
    text = open(log, 'r')
    for line in text:
         prefix, sep, inner = line.partition('<'); 
         inner, sep, suffix = inner.rpartition('>')
            print inner[0]
    print '%s' % f.readlines()
    f.close()


