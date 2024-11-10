from stockfish import Stockfish
from cmdwrapper import Cmd
import numpy as np

class reader:
    def readfile(self, file, outputfile, depth, name):
        stockfish = Stockfish(
            path="E:\\python projects\\StockfishEngine\\stockfish-windows-x86-64-avx2.exe",
            depth=depth,
            parameters={
                "Hash":2048,
                "Threads":2
            }
        )
        cmd = Cmd()
        cmd.cd('E:\\python projects\\PGN files')
        players = (cmd.getNames(file))
        moves = (cmd.pgnExtract(file)).split(" ")
        white, black = False, False
        if name in players[0]:
            white = True
        elif name in players[1]:
            black = True


        ##gets rid of 0-1, 1-0, 1/2-1/2, * at end of pgn
        moves.pop(len(moves)-1)

        mcounter = 2
        lastEval = ""
        pmoves = []
        stockfish._prepare_for_new_position()
        stockfish.set_fen_position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

        ##points for data analysis
        text_file = open(outputfile, "w")
        maxAdv=-9
        minAdv=9
        avgAdv=0
        totmov=len(moves)
        advList = []


        for i in moves:
            ##spacing and move count
            if mcounter%2==0:
                print((mcounter//2),". ", end = "")
                dum = str((mcounter//2))
                text_file.write(dum + ". ")
            else:
                print("    ", end="")
                text_file.write("   ")
            mcounter+= 1

            ##stockfish wrapper is dumb, wont take moves unless formated in this way
            dum = "\"",i,"\""
            stockfish.make_moves_from_current_position(dum)

            stockdict = stockfish.get_evaluation()
            if(stockdict["type"]=="cp"):
                adv = stockdict["value"]/100
                if adv>0:
                    print("+",adv)
                    text_file.write("+ "+str(adv)+"\n")
                else:
                    print(adv)
                    text_file.write(str(adv)+"\n")
            else:
                print("Mate in", stockdict["value"])
                text_file.write("Mate in " + str(stockdict["value"]) + "\n")

            if mcounter%2==0:
                print("\n")
                text_file.write("\n")

        text_file.close()
        return