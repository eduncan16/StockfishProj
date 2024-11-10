from reader import reader
from cmdwrapper import Cmd
cmd = Cmd()

read = reader()
print(read.readfile("Sample.pgn", 20, "Lifted_Truck_Swoas"))