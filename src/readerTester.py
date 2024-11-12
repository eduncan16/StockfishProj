from reader import reader
from cmdwrapper import Cmd
cmd = Cmd()

read = reader()

print(read.readfile("stlrap24.pgn", 10, ""))