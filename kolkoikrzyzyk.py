#while loop to keep the game up
print('Welcome to Tic Tac Toe!')

while True:

#while True:
    # Set the game up here
    the_board = [" "]*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + " will go first")
    
    play_game = input("Ready to play? Y or N" )
    
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    
    #Gameplay
    while game_on:
        
        if turn == "Player 1":
            #show the board
            display_board(the_board)
            
            #choose position
            position = player_choice(the_board)
            
            #place the marker
            place_marker(the_board,player1_marker,position)
            
            #Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Player 1 has won!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game!")
                    break
                else:
                    turn = "Player 2"
        else:
            #show the board
            display_board(the_board)
            
            #choose position
            position = player_choice(the_board)
            
            #place the marker
            place_marker(the_board,player2_marker,position)
            
            #Check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("Player 2 has won!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game!")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        break