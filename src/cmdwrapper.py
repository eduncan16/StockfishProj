import subprocess
import sys
import re

class Cmd(subprocess.Popen):
    def __init__(self, cmd_path='C:\\WINDOWS\\system32\\cmd'):
        subprocess.Popen.__init__(
            self,
            cmd_path,
            universal_newlines=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE)

    def send(self, command):
        self.stdin.write(command + '\n')
        self.stdin.flush()

    def cd(self, dir):
        self.send('cd /d ' + dir)

    def ls(self):
        self.send('ls')
        line = self.stdout.readline().strip()
        if not line == "":
            return line
        else:
            raise Exception("empty line exception")

    def readline(self):
        line = self.stdout.readline().strip()
        return line


    def pgnExtract(self, file):
        self.send('pgn-extract -Wuci ' + file)
        while True:
            line = self.stdout.readline()
            if len(line) > 2:
                if line[2] == 'n':
                    line = self.stdout.readline().strip()
                    line = self.stdout.readline().strip()
                    return line
                
    def getNames(self, file):
        self.send('pgn-extract -Wuci ' + file)
        ret = []
        while True:
            line = self.stdout.readline()
            if len(line) > 2:
                if line[1]=='W':
                    ret.append(line)
                if line[1]=='B':
                    ret.append(line)
                    break
        for i in range(2):
            start = ret[i].find('"') + 1
            end = ret[i].find('"', start)
            ret[i] = ret[i][start:end]
        return ret
            
    
    def getGameInFormat(self):
        self.stdin.write()
