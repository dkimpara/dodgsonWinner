from experimentCode import *
from datetime import datetime
import numpy as np


if __name__ == '__main__':
    #collect_data([20,30,40], np.linspace(2.05, 2.45, 5))
    #collect_data([20,30,40], np.linspace(2.23, 2.26, 2))
    for m in [50, 60, 70]:
        startTime = datetime.now()
        collect_data([m], np.linspace(2.1, 2.5, 9))
        collect_data([m], [2.225, 2.275])
        print(datetime.now() - startTime)
    #collect_data([85,100], np.linspace(2.1, 2.5, 9))
