from reader import reader
from cmdwrapper import Cmd
import os
import numpy as np
import matplotlib.pyplot as plt
import time

read = reader()
games = np.empty((0, 0))
pgn_files = os.listdir("E:\\python projects\\PGN files")
maxRow = 0

savefile = "E:\\python projects\\Raw_data\\Sample_Games.npy"

for i in pgn_files:
    if i[-4:]==".pgn":
        currGame = read.readfile(i, 10, " ")
        if maxRow<currGame.shape[0]:
            maxRow = currGame.shape[0]
            #add columns to games to reflect the largest needed column
            games = np.pad(games, ((0, 0), (0, (maxRow)-games.shape[1])), mode='constant', constant_values=np.nan)
        #pad the currGame if needed, in order to match the columns in games
        currGame = np.pad(currGame, (0, maxRow-len(currGame)), mode='constant', constant_values=np.nan)
        #stack the arrays
        games = np.vstack((games, [currGame]))


#ensure proper formatting
time.sleep(.1)
np.set_printoptions(suppress=True, precision=3)
print("\n", np.nanmean(games, axis=0))


#save array to file
np.save(savefile, games)