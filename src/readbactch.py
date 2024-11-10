from reader import reader
from cmdwrapper import Cmd
import os
import numpy as np

read = reader()
games = np.empty((1000,200))
pgn_files = os.listdir("E:\\python projects\\PGN files")

for i in pgn_files:
    if i[-4:]==".pgn":
        game = read.readfile(i, 10, "")
        if 200-len(game)<0:
            raise Exception("Game too large")
        game_padded = np.pad(game, (0, 200-len(game)), mode='constant', constant_values=np.nan)
        games = np.vstack((games, [game_padded]))
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
print(games)