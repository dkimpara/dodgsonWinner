from writeup.experimentCode import *
from datetime import datetime
import numpy as np


if __name__ == '__main__':
    #collect_data([20,30,40], np.linspace(2.05, 2.45, 5))
    #collect_data([20,30,40], np.linspace(2.23, 2.26, 2))
    for m in [85, 100]:
        startTime = datetime.now()
        collect_data([m], np.linspace(2.1, 2.5, 9))
        print(datetime.now() - startTime)
