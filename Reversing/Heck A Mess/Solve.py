from pwn import *
import chess
import chess.engine
engine = chess.engine.SimpleEngine.popen_uci("./stockfish/stockfish-ubuntu-x86-64")  # Use the Stockfish engine
engine.configure({
    "Skill Level": 20
})

def board_to_fen(board):
    fen = ""
    empty_count = 0
    for row in board:
        for square in row:
            if square == ".":
                empty_count += 1
            else:
                if empty_count > 0:
                    fen += str(empty_count)
                    empty_count = 0
                fen += square
        if empty_count > 0:
            fen += str(empty_count)
            empty_count = 0
        fen += "/"
    return fen[:-1]

def agh():
    io.readuntil(b"Current Board:")
    io.readline()
    data = ""
    for i in range(8):
        data += io.readline().decode("utf-8")
    adds = io.readline().decode("utf-8").split(":")[1]
    
    rows = data.strip().split("\n")
    board = [list(row.split()) for row in rows]
    
    fen_string = board_to_fen(board)
    fen_string += adds
    
    board = chess.Board(fen_string)
    best_move_uci = engine.analyse(board, chess.engine.Limit(time=0.1))['pv'][0]
    board.push(best_move_uci)
        
    print(fen_string)
    print(board.fen())
    io.readuntil(b'Enter your best move data: ')
    io.sendline(board.fen())
    print(io.readline())


#io = remote('<IP>','<Port>')
io = process('./File.py')
for i in range(2):
    for i in range(2):
        agh()
    print(io.readuntil(b"Current Board:"))
    print(io.readline())
    print(io.readline())
    print(io.readline())
agh() 
#io.sendline(b'1')
#io.sendline(b'624')
io.interactive()