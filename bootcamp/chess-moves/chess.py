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
def print_board(fen):
    # check output of parse_fen is producing the right thing
    board = parse_fen(fen)
    for i , row in enumerate(board):
        rank = 8 - i
        print(rank, ' ', ' '.join(row))
    print(('    a b c d e f g h'))
    
print_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")


def generate_moves(board):
    # raise NotImplementedError("This function is not implemented yet.")
    moves = 0
    # function that moves pawn move_pawn()
         
    # function that moves knight move_pawn()
    
    ## looping through the board, finding pieces to move
    # for i in range(len(board)): # for each row
        # for j in range(len(board[i])): # for each block
        #   if board[i][j] == '.'
                #continue # if empty,
            # elif board[i][j] == 'p' or board[i][j] == 'P':
            #   #call on the function that calc how many moves a pawn has
            #   # moves +=1
            # elif board[i][j] == 'n' or board[i][j] == 'N':
            #   #call on the function that calc how many moves a knight has
            #   # moves +=1
             # elif board[i][j] == '' or board[i][j] == 
            #   #call on the function that calc how many moves a pawn has



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