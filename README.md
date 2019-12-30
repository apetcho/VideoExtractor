# VideoExtractor
A simple video clip extractor based on ffmpeg.

# Requirements and Usage
To be able to use this software, you must first install *ffmpeg* on
your system and have python 3 available. The software has only been
tested on MacOS.

After your system is properly set, you run the software as follows
from the command-line (aka Terminal):


    $ MY_INPUT=inputfile.mp4
    $ MY_OUTPUT=outputfile.mp4
    $ START_TIME=00:20:15    # We want the clip starting from 20min15
    $ DURATION=00:01:00      # The running time (duration) of our clip
    $ # Call the source
    $ python3 VideoExtractor.py \
    --infile=${MY_INPUT} \
    --outfile=${MY_OUTPUT} \
    --start=${START_TIME} \
    --duration=${DURATION}

To have more help on how to use this software, just run the following
code:

    $ python3 VideoExtractor.py --help
