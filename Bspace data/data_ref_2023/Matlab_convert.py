import numpy as np
import os
import pandas as pd
import scipy as sc
from scipy.io import loadmat

raw = loadmat('data.mat')['PWSignals'][0][0]     # this gives the 1x7 array with time and 6 features
time, A, R, E, CNTS, D, RMS = raw.transpose()   # extract all the features
time, A, R, E, CNTS, D, RMS = time[0], A[0], R[0], E[0], CNTS[0], D[0], RMS[0]
os.mkdir('Opened_Files')

for i in range(len(time[0])):
    os.mkdir(f'Opened_Files\\Experiment{i+1}')
    for j in range(len(time[0][i])):
        window = np.reshape([time[0][i][j][0], A[0][i][j][0], R[0][i][j][0], E[0][i][j][0],
                            CNTS[0][i][j][0], D[0][i][j][0], RMS[0][i][j][0]], (7, len(time[0][i][j][0]))).transpose()
        df = pd.DataFrame(window, columns=['Time', 'A', 'R', 'E', 'CNTS', 'D', 'RMS'])
        df.to_csv(f'Opened_Files\\Experiment{i+1}\\Exp{i+1}_Win{j+1}.csv')