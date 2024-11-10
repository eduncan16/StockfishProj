from reader import reader
from cmdwrapper import Cmd
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
counter = 1
depth = 10
end = False


read = reader()
while not end:
    output = "output" + str(counter) + ".txt"
    print(output)
    currline = listfiles[len(listfiles)-counter]
    counter+=1
    print(currline,counter)
    if currline=='end':
        end = True
    else:
        read.readfile(currline, output, depth)
