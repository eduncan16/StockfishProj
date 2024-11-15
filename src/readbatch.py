from reader import reader
from cmdwrapper import Cmd
import os
import numpy as np
import matplotlib.pyplot as plt
import time

savefile = "E:\\python projects\\Raw_data\\Alekhine_Alexander"
pgn_files = os.listdir("E:\\python projects\\PGN files")
read = reader()

prevSaveFile = ""
interupted = False
progress = 0

# Load existing data if the file exists
if interupted:
    if os.path.exists(f"{prevSaveFile}.npy"):
        games = np.load(f"{prevSaveFile}.npy")
        print(f"Loaded existing data from {f"{prevSaveFile}.npy"}")
        pgn_files = pgn_files[progress:]
        pgnOffset = progress
        maxRow = games.shape[1]
        print(maxRow)
        count = progress
    else:
        raise FileNotFoundError(f"The file {prevSaveFile}.npy does not exist.")
else:
    games = np.empty((0, 0))
    maxRow = 0
    count = 0
    pgnOffset = 0

for i in pgn_files:
    if i[-4:]==".pgn":
        currGame = read.readfile(i, 1, "Alekhine, Alexander")
        if maxRow<currGame.shape[0]:
            maxRow = currGame.shape[0]
            #add columns to games to reflect the largest needed column
            games = np.pad(games, ((0, 0), (0, (maxRow)-games.shape[1])), mode='constant', constant_values=np.nan)
        #pad the currGame if needed, in order to match the columns in games
        currGame = np.pad(currGame, (0, maxRow-len(currGame)), mode='constant', constant_values=np.nan)
        #stack the arrays
        games = np.vstack((games, [currGame]))
        #save progress
        count+=1
        savePath = f"{savefile}_{count}_of_{(len(pgn_files)-1)+pgnOffset}.npy"
        lastSavePath = f"{savefile}_{count-1}_of_{(len(pgn_files)-1)+pgnOffset}.npy"
        np.save(savePath, games)
        if os.path.exists(lastSavePath):
            os.remove(lastSavePath)
        print(games)


#ensure proper formatting
time.sleep(.1)
np.set_printoptions(suppress=True, precision=3)
print("\n", np.nanmean(games, axis=0))


#save array to file
np.save(savefile, games)