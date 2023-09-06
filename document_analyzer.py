# import pandas as pd
import os as os
import signal
import glob
import csv
import sys
from inputimeout import inputimeout
from pathlib import Path
from collections import Counter

TIMEOUT = 5 # number of seconds your want for timeout
docsPath = Path('/docs')
os.chdir(docsPath)

def interrupted(signum, frame):
    "called when read times out"
    print('interrupted!')
signal.signal(signal.SIGALRM, interrupted)
path = ''
try:
    path = Path(inputimeout(prompt='You have 30 seconds to enter path to documents.\n', timeout=TIMEOUT).strip())
    if path.exists():
        print('Path exists.')
    print("Entered path is: "+str(path))
    os.chdir(path)
except:
    if path == "" or path is None:
        print("Will continue with default documents path.")
    else:
        print('Path is not valid')
    print('Will be used default path: '+str(docsPath))
    path == docsPath
list_of_files = sorted(glob.glob(str(os.getcwd())+'/*.csv'), key=os.path.getctime, reverse=True)
doc = 0
commonWords = ['']
if len(list_of_files) == 0:
    sys.exit("Path doesnt contain specific documents.");
while doc < 4:
    currentDoc = csv.reader(str(list_of_files[doc]))
    currentDoc = str(currentDoc).split()
    commonWords += Counter(currentDoc).most_common()
    doc += 1
commonWords = str(commonWords).split()
print(Counter(commonWords).most_common())
print(len(Counter(commonWords).most_common()))