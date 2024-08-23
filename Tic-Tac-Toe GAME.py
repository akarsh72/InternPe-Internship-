                                 ### Tic-Tac-Toe GAME ###
'''
1. Input player name
2. Instructions
2. Put sign to each player ['X'/'O']
3. Create a BOARD
4. Take user desigerd spot number
5. Put sign ['X'/'O'] of the user at his desigred spot number
6. Print Board after each input
7. Calculate and diaplay the result

'''
# -----------------------------------------------------------------------------------------------


def calculate_result(player_one, player_two):
    if ( spot[0]==spot[1]==spot[2] == 'X' or
         spot[3]==spot[4]==spot[5] == 'X' or
         spot[6]==spot[7]==spot[8] == 'X' or
         spot[0]==spot[3]==spot[6] == 'X' or
         spot[1]==spot[4]==spot[7] == 'X' or
         spot[2]==spot[5]==spot[8] == 'X' or
         spot[0]==spot[4]==spot[8] == 'X' or
         spot[2]==spot[4]==spot[6] == 'X'    ):
        print(f'Congratulations " {player_one} " you are the WINNER  !!! ')
        quit()
    
    elif( spot[0]==spot[1]==spot[2] == 'O' or
          spot[3]==spot[4]==spot[5] == 'O' or
          spot[6]==spot[7]==spot[8] == 'O' or
          spot[0]==spot[3]==spot[6] == 'O' or
          spot[1]==spot[4]==spot[7] == 'O' or
          spot[2]==spot[5]==spot[8] == 'O' or
          spot[0]==spot[4]==spot[8] == 'O' or
          spot[2]==spot[4]==spot[6] == 'O'    ) :
        print(f'Congratulations " {player_two} " you are the WINNER  !!! ')
        quit()



used_spot = []
def desired_spot_no(name):
    while(True):
        spot_no = int(input(f'{name} : '))
        INDEX = spot_no - 1
        if 0<= INDEX <= 8:
            if INDEX in used_spot:
                print('This Spot number is BOOKED : Enter another Spot Number : ')
                continue
            else:
                used_spot.append(INDEX)
                return INDEX

        else:
            print('Please enter a number between (1-9)')



spot = []                   # empty list
for i in range(9): 
    spot.append(' ')
def game_board():
    board = f'''
                    ______________
                   |    |    |    |
                   |  {spot[0]} |  {spot[1]} | {spot[2]}  |
                   |----|----|----|
                   |  {spot[3]} |  {spot[4]} | {spot[5]}  |
                   |----|----|----|
                   |  {spot[6]} |  {spot[7]} | {spot[8]}  |
                   |____|____|____|
            '''
    
    print(board)



instructions = ''' 
____________________________________________________________
          
          This will be our Tic-Tac-Toe Board
                    ______________
                   |    |    |    |
                   |  1 |  2 | 3  |
                   |----|----|----|
                   |  4 |  5 | 6  |
                   |----|----|----|
                   |  7 |  8 | 9  |
                   |____|____|____|
                
INSTRUCTIONS :
1. Insert the spot number(1-9) to put your sign
2. You must fill all 9 spots to get the result
3. Player 1 will go first
____________________________________________________________

'''



def main():
    print('\n\n\t\tWELCOME to Tic-Tac-Toe GAME.... !!!')
    player_one = input("Enter Player One Name : ")
    player_two = input("Enter Player Two Name : ")
    print(f'\n{player_one} and {player_two}, please read the INSTRUCTIONS before get started.')

    print(instructions)

    print(f"{player_one}'s sign will be ---> 'X' ")
    print(f"{player_two}'s sign will be ---> 'O' ")

    game_board()

    print('\nGive your Desigred spot number')
    for i in range(9):
        if i%2==0:
            index = desired_spot_no(player_one)                                            
            spot[index] = 'X'
        else:
            index = desired_spot_no(player_two)                                             
            spot[index] = 'O'
        
        game_board()                 # putting sign ['X'/'O'] of the user at his desigred spot number

        calculate_result(player_one, player_two)

    print('Its a TIE !!!')



main()