from reader import reader
from cmdwrapper import Cmd
cmd = Cmd()

read = reader()

print(read.readfile("Sample.pgn", 10, "Lifted_Truck_Swoas"))
print(read.readfile("SampleCopy(2).pgn", 10, "Lifted_Truck_Swoas"))