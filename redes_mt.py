#import pandas as pd
import re
#import numpy
import sys


if sys.argv[1] is not None:
    print('route is:' + sys.argv[1])
    with open(sys.argv[1]) as fp:
        line = fp.readline()