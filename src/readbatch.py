from reader import reader
from cmdwrapper import Cmd
import numpy as np

cmd = Cmd()


cmd.cd('E:\\python projects\\PGN files')
cmd.ls()
##offset for lines not relevant
for i in range(5):
    print(cmd.readline(),i)
listfiles = []
currline = "end"
while not currline == "":
    if not currline == "png-extract.exe":
        listfiles.append(currline)
        print(currline)
    currline=cmd.readline()
print(listfiles)


currline = ""
depth = 10
end = False
name = "Lifted_Truck_Swoas"
evalList = np.array([])

read = reader()
for i in range(len(listfiles)-1):
    currline = listfiles[len(listfiles)-(i+1)]
    print(currline,i)
    if not currline=='end':
        evalList = np.append(evalList, read.readfile(currline, depth, name))

print(evalList)