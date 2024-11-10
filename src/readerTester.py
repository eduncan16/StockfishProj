from reader import reader
from cmdwrapper import Cmd
cmd = Cmd()

read = reader()
read.readfile("Sample.pgn", "SampleOutput.txt", 20, "Lifted_Truck_Swoas")