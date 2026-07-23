def parse_fen(fen): # INPUT "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    fen_pieces, to_move, castling_rights, ep, hm, fm = fen.split(" ")
    pieces = [[]]
    for char in fen_pieces: # only takes out the board
        if char.isdigit(): # checks if the character is a digit
            pieces[-1].extend(["."] * int(char)) # makes  a list of . 
        elif char == "/":
            pieces.append([])
        else:
            pieces[-1].append(char)

    return pieces # OUTPUT [[r, n, b, q, k, b, n, r], [p, p, p,...], [.,.,.,.,]]


def generate_moves(board):
    # raise NotImplementedError("This function is not implemented yet.")
    moves = 0
    # function that moves pawn move_pawn()
         
    # function that moves knight move_pawn()
    # 

# OUTPUT integer with number of possible moves
    return moves


def apply_move(board, move):
    raise NotImplementedError("This function is not implemented yet.")
    #  if  that char is w or b: "deciding which pieces need to be moved"
# move either
# for each piece can that piece move?
#lOOP if not, move to the next piece (continue)
# increase number of possible moves


print(parse_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"))