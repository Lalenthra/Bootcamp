def parse_fen(fen): # INPUT "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    fen_pieces, to_move, castling_rights, ep, hm, fm = fen.split(" ")
    pieces = [[]]  
    for char in fen_pieces: # only takes out the board
        if char.isdigit(): # checks if the character is a digit
            pieces[-1].extend(["."] * int(char)) # makes  a list of . 
        elif char == "/":
            pieces.append([])
        else:
            pieces[-1].append(char) # appends the char to the last list----- to avoid swapimg the couple

    return pieces, to_move # OUTPUT [[r, n, b, q, k, b, n, r], [p, p, p,...], [.,.,.,.,]], who's turn it is
def print_board(fen):
    # check output of parse_fen is producing the right thing
    board = parse_fen(fen)
    
    for i , row in enumerate(board[0]): #pieces is index 0 to_move is index 1
        rank = 8 - i # rank is row from 0
        row_0 = ' '.join(row)     
        print(f"{rank}   {row_0}")
        # print(row[0])
    print('    a b c d e f g h')

def main_function():
    print_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    print()
    pawn_move(parse_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"), 2,0,1)
    
def pawn_move(parse_fen,r,c,num_of_move): # define funtction
    board = parse_fen[0]      
    player = parse_fen[1]
    w_pawn = board[1]
    b_pawn = board[6]
    
    if player == 'w': #if the player is white
        if board[r][c]=='.': #if space is empty == dot
            board[r][c] = 'p' #move the paawn to empty space
            board[r-num_of_move][c] = "."#since pawn move replace with dot
            
    for i , row in enumerate(board): #pieces is index 0 to_move is index 1
        rank = 8 - i # rank is row from 0
        row_0 = ' '.join(row)     
        print(f"{rank}   {row_0}")        
    
    
    return board

main_function()    
    
    
# print_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")


# def generate_moves(board,to_move):
    
# def moves(board, r, c):
    
#     moves = 0
#     for i in range(8):
#         for t in range(8):
#             piece = board[i][t]

        
    
        #board[1][1]
        
    
    # raise NotImplementedError("This function is not implemented yet.")

    
    # function that calculates the amount of moves pawn moves_pawn()
    # def moves_pawn():
    #
         
    # function that calculates knight moves moves_knight()
    
    ## looping through the board, finding pieces to move
    # for i in range(len(board)): # for each row
        # for j in range(len(board[i])): # for each block
        #   if board[i][j] == '.'
                #continue # if empty,
            # elif board[i][j] == 'p' or board[i][j] == 'P':
                # if capital P then we need to move it negatively
                # else we move it positively
            #   #call on the function that calc how many moves a pawn has
            #   # moves +=1
            # elif board[i][j] == 'n' or board[i][j] == 'N':
            #   #call on the function that calc how many moves a knight has
            #   # moves +=1
             # elif board[i][j] == 'r' or board[i][j] == 'R'
            #   #call on the function that calc how many moves a pawn has
        # def piece_moves(board, piece, r, c)
        # if 


# OUTPUT integer with number of possible moves
#     return moves


# def apply_move(board, move):
#     raise NotImplementedError("This function is not implemented yet.")
    #  if  that char is w or b: "deciding which pieces need to be moved"
# move either
# for each piece can that piece move?
#lOOP if not, move to the next piece (continue)
# increase number of possible moves


# print(parse_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"))