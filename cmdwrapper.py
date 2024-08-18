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

    def pgnExtract(self, file):
        self.send('pgn-extract -Wuci ' + file)
        while True:
            line = self.stdout.readline().strip()
            if not line == "":
                if line[2] == 'n':
                    line = self.stdout.readline().strip()
                    line = self.stdout.readline().strip()
                    return line
    
    def getGameInFormat(self):
        self.stdin.write()
