<<<<<<< HEAD:Vier-Gewinnt2.0.py

class Board:

    def __init__(self):
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def stacking_things(self, cell, player):
                cell = cell + 7
                if self.is_valid_turn(cell):
                    self.state[cell] = player.symbol
                    return True
                else:
                    if cell < 35:
                        self.stacking_things(cell, player)
                    else:
                        print("Invalid Move!")

    def make_turn(self, cell, player):
        if self.is_valid_turn(cell):
            self.state[cell] = player.symbol
        else:
            self.stacking_things(cell, player)
                   
    def is_valid_turn(self, cell):
        if self.state[cell] == 0:
            return True
        else:
            return False

    def sign_to_printable(self, sign):
        if sign == 0:
            return " "
        elif sign == 1:
            return "X"
        elif sign == -1:
            return "O"
        else:
            return "A"

    def is_full(self):
        for i in self.state:
            if i == 0:
                return False
        self.print_board()
        print("It's a tie.")      
        return True

    def print_board(self):
        print(
              "        "+"1"+"   "+"2"+"   "+"3"+"   "+"4"+"   "+"5"+"   "+"6"+"   "+"7" "\n"
              "     " + " | " + self.sign_to_printable(self.state[35]) + " | " + self.sign_to_printable(self.state[36]) + " | " + self.sign_to_printable(self.state[37]) + " | " + self.sign_to_printable(self.state[38]) + " | " + self.sign_to_printable(self.state[39]) +" | " + self.sign_to_printable(self.state[40]) +" | " + self.sign_to_printable(self.state[41]) +" | " + " \n" +
              "     " + " | " + self.sign_to_printable(self.state[28]) + " | " + self.sign_to_printable(self.state[29]) + " | " + self.sign_to_printable(self.state[30]) + " | " + self.sign_to_printable(self.state[31]) + " | " + self.sign_to_printable(self.state[32]) +" | " + self.sign_to_printable(self.state[33]) +" | " + self.sign_to_printable(self.state[34]) +" | " + " \n" +
              "     " + " | " + self.sign_to_printable(self.state[21]) + " | " + self.sign_to_printable(self.state[22]) + " | " + self.sign_to_printable(self.state[23]) + " | " + self.sign_to_printable(self.state[24]) + " | " + self.sign_to_printable(self.state[25]) +" | " + self.sign_to_printable(self.state[26]) +" | " + self.sign_to_printable(self.state[27]) +" | " + " \n" +
              "     " + " | " + self.sign_to_printable(self.state[14]) + " | " + self.sign_to_printable(self.state[15]) + " | " + self.sign_to_printable(self.state[16]) + " | " + self.sign_to_printable(self.state[17]) + " | " + self.sign_to_printable(self.state[18]) +" | " + self.sign_to_printable(self.state[19]) +" | " + self.sign_to_printable(self.state[20]) +" | " + " \n" +
              "     " + " | " + self.sign_to_printable(self.state[7]) + " | " + self.sign_to_printable(self.state[8]) + " | " + self.sign_to_printable(self.state[9]) + " | " + self.sign_to_printable(self.state[10]) + " | " + self.sign_to_printable(self.state[11]) +" | " + self.sign_to_printable(self.state[12]) +" | " + self.sign_to_printable(self.state[13]) +" | " + " \n" +
              "     " + " | " + self.sign_to_printable(self.state[0]) + " | " + self.sign_to_printable(self.state[1]) + " | " + self.sign_to_printable(self.state[2]) + " | " + self.sign_to_printable(self.state[3]) + " | " + self.sign_to_printable(self.state[4]) +" | " + self.sign_to_printable(self.state[5]) +" | " + self.sign_to_printable(self.state[6]) +" | " + " \n"
             )

    def check_win(self, player):
        s = player.symbol
        #Vertikal 1-7
        if self.state[0] == s and self.state[7] == s and self.state[14] == s and self.state[21] == s:
            self.state[0] = self.state[7] = self.state[14] =  self.state[21] = 3
            return True

        elif self.state[7] == s and self.state[14] == s and self.state[21] == s and self.state[28] == s:
            self.state[7] = self.state[14] = self.state[21] = self.state[28] = 8
            return True

        elif self.state[14] == s and self.state[21] == s and self.state[28] == s and self.state[35] == s:
            self.state[14] = self.state[21] = self.state[28] = self.state[35] = 8 
            return True

        elif self.state[1] == s and self.state[8] == s and self.state[15] == s and self.state[22] == s:
            self.state[1] = self.state[8] = self.state[15] = self.state[22] = 8
            return True

        elif self.state[8] == s and self.state[15] == s and self.state[22] == s and self.state[29] == s:
            self.state[8] = self.state[15] = self.state[22] = self.state[29] = 8
            return True

        elif self.state[15] == s and self.state[22] == s and self.state[29] == s and self.state[36] == s:
            self.state[15] = self.state[22] = self.state[29] = self.state[36] = 8
            return True  

        elif self.state[2] == s and self.state[9] == s and self.state[16] == s and self.state[23] == s:
            self.state[2] = self.state[9] = self.state[16] = self.state[23] = 8
            return True

        elif self.state[9] == s and self.state[16] == s and self.state[23] == s and self.state[30] == s:
            self.state[9] = self.state[16] = self.state[23] = self.state[30] = 8
            return True

        elif self.state[16] == s and self.state[23] == s and self.state[30] == s and self.state[37] == s:
            self.state[16] = self.state[23] = self.state[30] = self.state[37] = 8
            return True

        elif self.state[3] == s and self.state[10] == s and self.state[17] == s and self.state[24] == s:
            self.state[3] = self.state[10] = self.state[17] = self.state[24] = 8
            return True

        elif self.state[10] == s and self.state[17] == s and self.state[24] == s and self.state[31] == s:
            self.state[10] = self.state[17] = self.state[24] = self.state[31] = 8
            return True

        elif self.state[17] == s and self.state[24] == s and self.state[31] == s and self.state[38] == s:
            self.state[17] = self.state[24] = self.state[31] = self.state[38] = 8
            return True 

        elif self.state[4] == s and self.state[11] == s and self.state[18] == s and self.state[25] == s:
            self.state[4] = self.state[11] = self.state[18] = self.state[25] = 8
            return True

        elif self.state[11] == s and self.state[18] == s and self.state[25] == s and self.state[32] == s:
            self.state[11] = self.state[18] = self.state[25] = self.state[32] = 8
            return True

        elif self.state[18] == s and self.state[25] == s and self.state[32] == s and self.state[39] == s:
            self.state[18] = self.state[25] = self.state[32] = self.state[39] = 8
            return True  

        elif self.state[5] == s and self.state[12] == s and self.state[19] == s and self.state[26] == s:
            self.state[5] = self.state[12] = self.state[19] = self.state[26] = 8
            return True

        elif self.state[12] == s and self.state[19] == s and self.state[26] == s and self.state[33] == s:
            self.state[12] = self.state[19] = self.state[26] = self.state[33] = 8
            return True

        elif self.state[19] == s and self.state[26] == s and self.state[33] == s and self.state[40] == s:
            self.state[19] = self.state[26] = self.state[33] = self.state[40] = 8
            return True

        elif self.state[6] == s and self.state[13] == s and self.state[20] == s and self.state[27] == s:
            self.state[6] = self.state[13] = self.state[20] = self.state[27] = 8
            return True

        elif self.state[13] == s and self.state[20] == s and self.state[27] == s and self.state[34] == s:
            self.state[13] = self.state[20] = self.state[27] = self.state[34] = 8
            return True

        elif self.state[20] == s and self.state[27] == s and self.state[34] == s and self.state[41] == s:
            self.state[20] = self.state[27] = self.state[34] = self.state[41] = 8
            return True  

        #horizontal a-f
        elif self.state[0] == s and self.state[1] == s and self.state[2] == s and self.state[3] == s:
            self.state[0] = self.state[1] = self.state[2] = self.state[3] = 8
            return True

        elif self.state[1] == s and self.state[2] == s and self.state[3] == s and self.state[4] == s:
            self.state[1] = self.state[2] = self.state[3] = self.state[4] = 8
            return True

        elif self.state[2] == s and self.state[3] == s and self.state[4] == s and self.state[5] == s:
            self.state[2] = self.state[3] = self.state[4] = self.state[5] = 8
            return True

        elif self.state[3] == s and self.state[4] == s and self.state[5] == s and self.state[6] == s:
            self.state[3] = self.state[4] = self.state[5] = self.state[6] = 8
            return True 

        elif self.state[7] == s and self.state[8] == s and self.state[9] == s and self.state[10] == s:
            self.state[7] = self.state[8] = self.state[9] = self.state[10] = 8
            return True

        elif self.state[8] == s and self.state[9] == s and self.state[10] == s and self.state[11] == s:
            self.state[8] = self.state[9] = self.state[10] = self.state[11] = 8
            return True

        elif self.state[9] == s and self.state[10] == s and self.state[11] == s and self.state[12] == s:
            self.state[9] = self.state[10] = self.state[11] = self.state[12] = 8
            return True

        elif self.state[10] == s and self.state[11] == s and self.state[12] == s and self.state[13] == s:
            self.state[10] = self.state[11] = self.state[12] = self.state[13] = 8
            return True  

        elif self.state[14] == s and self.state[15] == s and self.state[16] == s and self.state[17] == s:
            self.state[14] = self.state[15] = self.state[16] = self.state[17] = 8
            return True

        elif self.state[15] == s and self.state[16] == s and self.state[17] == s and self.state[18] == s:
            self.state[15] = self.state[16] = self.state[17] = self.state[18] = 8
            return True

        elif self.state[16] == s and self.state[17] == s and self.state[18] == s and self.state[19] == s:
            self.state[16] = self.state[17] = self.state[18] = self.state[19] = 8
            return True

        elif self.state[17] == s and self.state[18] == s and self.state[19] == s and self.state[20] == s:
            self.state[17] = self.state[18] = self.state[19] = self.state[20] = 8
            return True 

        elif self.state[23] == s and self.state[24] == s and self.state[25] == s and self.state[26] == s:
            self.state[23] = self.state[24] = self.state[25] = self.state[26] = 8 
            return True

        elif self.state[22] == s and self.state[23] == s and self.state[24] == s and self.state[25] == s:
            self.state[22] = self.state[23] = self.state[24] = self.state[25] = 8
            return True

        elif self.state[23] == s and self.state[24] == s and self.state[25] == s and self.state[26] == s:
            self.state[23] = self.state[24] = self.state[25] = self.state[26] = 8
            return True

        elif self.state[24] == s and self.state[25] == s and self.state[26] == s and self.state[27] == s:
            self.state[24] = self.state[25] = self.state[26] = self.state[27] = 8
            return True  

        elif self.state[28] == s and self.state[29] == s and self.state[30] == s and self.state[31] == s:
            self.state[28] = self.state[29] = self.state[30] = self.state[31] = 8
            return True

        elif self.state[29] == s and self.state[30] == s and self.state[31] == s and self.state[32] == s:
            self.state[29] = self.state[30] = self.state[31] = self.state[32] = 8
            return True

        elif self.state[30] == s and self.state[31] == s and self.state[32] == s and self.state[33] == s:
            self.state[30] = self.state[31] = self.state[32] = self.state[33] = 8
            return True

        elif self.state[31] == s and self.state[32] == s and self.state[33] == s and self.state[34] == s:
            self.state[31] = self.state[32] = self.state[33] = self.state[34] = 8
            return True  

        elif self.state[35] == s and self.state[36] == s and self.state[37] == s and self.state[38] == s:
            self.state[35] = self.state[36] = self.state[37] = self.state[38] = 8
            return True

        elif self.state[36] == s and self.state[37] == s and self.state[38] == s and self.state[39] == s:
            self.state[36] = self.state[37] = self.state[38] = self.state[39] = 8
            return True

        elif self.state[37] == s and self.state[38] == s and self.state[39] == s and self.state[40] == s:
            self.state[37] = self.state[38] = self.state[39] = self.state[40] = 8
            return True

        elif self.state[38] == s and self.state[39] == s and self.state[40] == s and self.state[41] == s:
            self.state[38] = self.state[39] = self.state[40] = self.state[41] = 8
            return True  

        #diagonal links nach rechts
        elif self.state[14] == s and self.state[22] == s and self.state[30] == s and self.state[38] == s:
            self.state[14] = self.state[22] = self.state[30] = self.state[38] = 8
            return True

        elif self.state[15] == s and self.state[23] == s and self.state[31] == s and self.state[39] == s:
            self.state[15] = self.state[23] = self.state[31] = self.state[39] = 8
            return True

        elif self.state[16] == s and self.state[24] == s and self.state[32] == s and self.state[40] == s:
            self.state[16] = self.state[24] = self.state[32] = self.state[40] = 8
            return True

        elif self.state[17] == s and self.state[25] == s and self.state[33] == s and self.state[41] == s:
            self.state[17] = self.state[25] = self.state[33] = self.state[41] = 8
            return True  

        elif self.state[7] == s and self.state[15] == s and self.state[23] == s and self.state[31] == s:
            self.state[17] = self.state[15] = self.state[23] = self.state[31] = 8
            return True

        elif self.state[8] == s and self.state[16] == s and self.state[24] == s and self.state[32] == s:
            self.state[8] = self.state[16] = self.state[24] = self.state[32] = 8
            return True

        elif self.state[9] == s and self.state[17] == s and self.state[25] == s and self.state[33] == s:
            self.state[9] = self.state[17] = self.state[25] = self.state[33] = 8
            return True

        elif self.state[10] == s and self.state[18] == s and self.state[26] == s and self.state[34] == s:
            self.state[10] = self.state[18] = self.state[26] = self.state[34] = 8
            return True

        elif self.state[0] == s and self.state[8] == s and self.state[16] == s and self.state[24] == s:
            self.state[0] = self.state[8] = self.state[16] = self.state[24] = 8
            return True

        elif self.state[1] == s and self.state[9] == s and self.state[17] == s and self.state[25] == s:
            self.state[1] = self.state[9] = self.state[17] = self.state[25] = 8
            return True

        elif self.state[2] == s and self.state[10] == s and self.state[18] == s and self.state[26] == s:
            self.state[2] = self.state[10] = self.state[18] = self.state[26] = 8
            return True

        elif self.state[3] == s and self.state[11] == s and self.state[19] == s and self.state[27] == s:
            self.state[3] = self.state[11] = self.state[19] = self.state[27] = 8
            return True 

        #diagonal rechts nach links
        elif self.state[20] == s and self.state[26] == s and self.state[32] == s and self.state[38] == s:
            self.state[20] = self.state[26] = self.state[32] = self.state[38] = 8
            return True

        elif self.state[19] == s and self.state[25] == s and self.state[31] == s and self.state[37] == s:
            self.state[19] = self.state[25] = self.state[31] = self.state[37] = 8
            return True

        elif self.state[18] == s and self.state[24] == s and self.state[30] == s and self.state[36] == s:
            self.state[18] = self.state[24] = self.state[30] = self.state[36] = 8
            return True

        elif self.state[17] == s and self.state[23] == s and self.state[29] == s and self.state[35] == s:
            self.state[17] = self.state[23] = self.state[29] = self.state[35] = 8
            return True  

        elif self.state[13] == s and self.state[19] == s and self.state[25] == s and self.state[31] == s:
            self.state[13] = self.state[19] = self.state[25] = self.state[31] = 8
            return True

        elif self.state[12] == s and self.state[18] == s and self.state[24] == s and self.state[30] == s:
            self.state[12] = self.state[18] = self.state[24] = self.state[30] = 8
            return True

        elif self.state[11] == s and self.state[17] == s and self.state[23] == s and self.state[29] == s:
            self.state[1] = self.state[17] = self.state[23] = self.state[29] = 8
            return True

        elif self.state[10] == s and self.state[16] == s and self.state[22] == s and self.state[28] == s:
            self.state[10] = self.state[16] = self.state[22] = self.state[28] = 8
            return True  

        elif self.state[6] == s and self.state[12] == s and self.state[18] == s and self.state[24] == s:
            self.state[6] = self.state[12] = self.state[18] = self.state[24] = 8
            return True

        elif self.state[5] == s and self.state[11] == s and self.state[17] == s and self.state[23] == s:
            self.state[5] = self.state[11] = self.state[17] = self.state[23] = 8
            return True

        elif self.state[4] == s and self.state[10] == s and self.state[16] == s and self.state[22] == s:
            self.state[4] = self.state[10] = self.state[16] = self.state[22] = 8
            return True

        elif self.state[3] == s and self.state[9] == s and self.state[15] == s and self.state[21] == s:
            self.state[3] = self.state[9] = self.state[15] = self.state[21] = 8
            return True
        else:
            return False

class Player:
    def __init__(self, symbol):
        self.symbol = symbol


if __name__ == '__main__':
    player_a = Player(1)
    player_b = Player(-1)
    board = Board()
    active_player = player_a
    while not board.is_full():
        board.print_board()
        try:
            cell = int(input("Where do you want to place your sign? [1-7]"))
        except ValueError:
            continue
        cell = cell - 1
        
        if cell < 0 or cell > 6:
            print("Please enter a number between 1 and 7")
            continue
    
        board.make_turn(cell, active_player)
                               
        if board.check_win(active_player):
            board.print_board()
            print("You wonnered! GW.")            
            break
        
        if active_player == player_a:
            active_player = player_b
        else:
            active_player = player_a  


#Checkwin durch Funktion verkürzen?
=======

class Board:

    def __init__(self):
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def stacking_things(self, cell, player):
                cell = cell + 7
                if self.is_valid_turn(cell):
                    self.state[cell] = player.symbol
                    return True
                else:
                    if cell < 35:
                        self.stacking_things(cell, player)
                    else:
                        print("Invalid Move!")

    def make_turn(self, cell, player):
        if self.is_valid_turn(cell):
            self.state[cell] = player.symbol
        else:
            self.stacking_things(cell, player)
                   
    def is_valid_turn(self, cell):
        if self.state[cell] == 0:
            return True
        else:
            return False

    def sign_to_printable(self, sign):
        if sign == 0:
            return " "
        elif sign == 1:
            return "X"
        elif sign == -1:
            return "O"
        else:
            return "A"

    def is_full(self):
        for i in self.state:
            if i == 0:
                return False
        self.print_board()
        print("It's a tie.")      
        return True

    def print_board(self):
        print(
              "        "+"1"+"   "+"2"+"   "+"3"+"   "+"4"+"   "+"5"+"   "+"6"+"   "+"7" "\n"
              "     " + " | " + self.sign_to_printable(self.state[35]) + " | " + self.sign_to_printable(self.state[36]) + " | " + self.sign_to_printable(self.state[37]) + " | " + self.sign_to_printable(self.state[38]) + " | " + self.sign_to_printable(self.state[39]) +" | " + self.sign_to_printable(self.state[40]) +" | " + self.sign_to_printable(self.state[41]) +" | " + " \n" +
              "     " + " | " + self.sign_to_printable(self.state[28]) + " | " + self.sign_to_printable(self.state[29]) + " | " + self.sign_to_printable(self.state[30]) + " | " + self.sign_to_printable(self.state[31]) + " | " + self.sign_to_printable(self.state[32]) +" | " + self.sign_to_printable(self.state[33]) +" | " + self.sign_to_printable(self.state[34]) +" | " + " \n" +
              "     " + " | " + self.sign_to_printable(self.state[21]) + " | " + self.sign_to_printable(self.state[22]) + " | " + self.sign_to_printable(self.state[23]) + " | " + self.sign_to_printable(self.state[24]) + " | " + self.sign_to_printable(self.state[25]) +" | " + self.sign_to_printable(self.state[26]) +" | " + self.sign_to_printable(self.state[27]) +" | " + " \n" +
              "     " + " | " + self.sign_to_printable(self.state[14]) + " | " + self.sign_to_printable(self.state[15]) + " | " + self.sign_to_printable(self.state[16]) + " | " + self.sign_to_printable(self.state[17]) + " | " + self.sign_to_printable(self.state[18]) +" | " + self.sign_to_printable(self.state[19]) +" | " + self.sign_to_printable(self.state[20]) +" | " + " \n" +
              "     " + " | " + self.sign_to_printable(self.state[7]) + " | " + self.sign_to_printable(self.state[8]) + " | " + self.sign_to_printable(self.state[9]) + " | " + self.sign_to_printable(self.state[10]) + " | " + self.sign_to_printable(self.state[11]) +" | " + self.sign_to_printable(self.state[12]) +" | " + self.sign_to_printable(self.state[13]) +" | " + " \n" +
              "     " + " | " + self.sign_to_printable(self.state[0]) + " | " + self.sign_to_printable(self.state[1]) + " | " + self.sign_to_printable(self.state[2]) + " | " + self.sign_to_printable(self.state[3]) + " | " + self.sign_to_printable(self.state[4]) +" | " + self.sign_to_printable(self.state[5]) +" | " + self.sign_to_printable(self.state[6]) +" | " + " \n"
             )

    def check_win(self, player):
        s = player.symbol
        #Vertikal 1-7
        if self.state[0] == s and self.state[7] == s and self.state[14] == s and self.state[21] == s:
            self.state[0] = self.state[7] = self.state[14] =  self.state[21] = 3
            return True

        elif self.state[7] == s and self.state[14] == s and self.state[21] == s and self.state[28] == s:
            self.state[7] = self.state[14] = self.state[21] = self.state[28] = 8
            return True

        elif self.state[14] == s and self.state[21] == s and self.state[28] == s and self.state[35] == s:
            self.state[14] = self.state[21] = self.state[28] = self.state[35] = 8 
            return True

        elif self.state[1] == s and self.state[8] == s and self.state[15] == s and self.state[22] == s:
            self.state[1] = self.state[8] = self.state[15] = self.state[22] = 8
            return True

        elif self.state[8] == s and self.state[15] == s and self.state[22] == s and self.state[29] == s:
            self.state[8] = self.state[15] = self.state[22] = self.state[29] = 8
            return True

        elif self.state[15] == s and self.state[22] == s and self.state[29] == s and self.state[36] == s:
            self.state[15] = self.state[22] = self.state[29] = self.state[36] = 8
            return True  

        elif self.state[2] == s and self.state[9] == s and self.state[16] == s and self.state[23] == s:
            self.state[2] = self.state[9] = self.state[16] = self.state[23] = 8
            return True

        elif self.state[9] == s and self.state[16] == s and self.state[23] == s and self.state[30] == s:
            self.state[9] = self.state[16] = self.state[23] = self.state[30] = 8
            return True

        elif self.state[16] == s and self.state[23] == s and self.state[30] == s and self.state[37] == s:
            self.state[16] = self.state[23] = self.state[30] = self.state[37] = 8
            return True

        elif self.state[3] == s and self.state[10] == s and self.state[17] == s and self.state[24] == s:
            self.state[3] = self.state[10] = self.state[17] = self.state[24] = 8
            return True

        elif self.state[10] == s and self.state[17] == s and self.state[24] == s and self.state[31] == s:
            self.state[10] = self.state[17] = self.state[24] = self.state[31] = 8
            return True

        elif self.state[17] == s and self.state[24] == s and self.state[31] == s and self.state[38] == s:
            self.state[17] = self.state[24] = self.state[31] = self.state[38] = 8
            return True 

        elif self.state[4] == s and self.state[11] == s and self.state[18] == s and self.state[25] == s:
            self.state[4] = self.state[11] = self.state[18] = self.state[25] = 8
            return True

        elif self.state[11] == s and self.state[18] == s and self.state[25] == s and self.state[32] == s:
            self.state[11] = self.state[18] = self.state[25] = self.state[32] = 8
            return True

        elif self.state[18] == s and self.state[25] == s and self.state[32] == s and self.state[39] == s:
            self.state[18] = self.state[25] = self.state[32] = self.state[39] = 8
            return True  

        elif self.state[5] == s and self.state[12] == s and self.state[19] == s and self.state[26] == s:
            self.state[5] = self.state[12] = self.state[19] = self.state[26] = 8
            return True

        elif self.state[12] == s and self.state[19] == s and self.state[26] == s and self.state[33] == s:
            self.state[12] = self.state[19] = self.state[26] = self.state[33] = 8
            return True

        elif self.state[19] == s and self.state[26] == s and self.state[33] == s and self.state[40] == s:
            self.state[19] = self.state[26] = self.state[33] = self.state[40] = 8
            return True

        elif self.state[6] == s and self.state[13] == s and self.state[20] == s and self.state[27] == s:
            self.state[6] = self.state[13] = self.state[20] = self.state[27] = 8
            return True

        elif self.state[13] == s and self.state[20] == s and self.state[27] == s and self.state[34] == s:
            self.state[13] = self.state[20] = self.state[27] = self.state[34] = 8
            return True

        elif self.state[20] == s and self.state[27] == s and self.state[34] == s and self.state[41] == s:
            self.state[20] = self.state[27] = self.state[34] = self.state[41] = 8
            return True  

        #horizontal a-f
        elif self.state[0] == s and self.state[1] == s and self.state[2] == s and self.state[3] == s:
            self.state[0] = self.state[1] = self.state[2] = self.state[3] = 8
            return True

        elif self.state[1] == s and self.state[2] == s and self.state[3] == s and self.state[4] == s:
            self.state[1] = self.state[2] = self.state[3] = self.state[4] = 8
            return True

        elif self.state[2] == s and self.state[3] == s and self.state[4] == s and self.state[5] == s:
            self.state[2] = self.state[3] = self.state[4] = self.state[5] = 8
            return True

        elif self.state[3] == s and self.state[4] == s and self.state[5] == s and self.state[6] == s:
            self.state[3] = self.state[4] = self.state[5] = self.state[6] = 8
            return True 

        elif self.state[7] == s and self.state[8] == s and self.state[9] == s and self.state[10] == s:
            self.state[7] = self.state[8] = self.state[9] = self.state[10] = 8
            return True

        elif self.state[8] == s and self.state[9] == s and self.state[10] == s and self.state[11] == s:
            self.state[8] = self.state[9] = self.state[10] = self.state[11] = 8
            return True

        elif self.state[9] == s and self.state[10] == s and self.state[11] == s and self.state[12] == s:
            self.state[9] = self.state[10] = self.state[11] = self.state[12] = 8
            return True

        elif self.state[10] == s and self.state[11] == s and self.state[12] == s and self.state[13] == s:
            self.state[10] = self.state[11] = self.state[12] = self.state[13] = 8
            return True  

        elif self.state[14] == s and self.state[15] == s and self.state[16] == s and self.state[17] == s:
            self.state[14] = self.state[15] = self.state[16] = self.state[17] = 8
            return True

        elif self.state[15] == s and self.state[16] == s and self.state[17] == s and self.state[18] == s:
            self.state[15] = self.state[16] = self.state[17] = self.state[18] = 8
            return True

        elif self.state[16] == s and self.state[17] == s and self.state[18] == s and self.state[19] == s:
            self.state[16] = self.state[17] = self.state[18] = self.state[19] = 8
            return True

        elif self.state[17] == s and self.state[18] == s and self.state[19] == s and self.state[20] == s:
            self.state[17] = self.state[18] = self.state[19] = self.state[20] = 8
            return True 

        elif self.state[23] == s and self.state[24] == s and self.state[25] == s and self.state[26] == s:
            self.state[23] = self.state[24] = self.state[25] = self.state[26] = 8 
            return True

        elif self.state[22] == s and self.state[23] == s and self.state[24] == s and self.state[25] == s:
            self.state[22] = self.state[23] = self.state[24] = self.state[25] = 8
            return True

        elif self.state[23] == s and self.state[24] == s and self.state[25] == s and self.state[26] == s:
            self.state[23] = self.state[24] = self.state[25] = self.state[26] = 8
            return True

        elif self.state[24] == s and self.state[25] == s and self.state[26] == s and self.state[27] == s:
            self.state[24] = self.state[25] = self.state[26] = self.state[27] = 8
            return True  

        elif self.state[28] == s and self.state[29] == s and self.state[30] == s and self.state[31] == s:
            self.state[28] = self.state[29] = self.state[30] = self.state[31] = 8
            return True

        elif self.state[29] == s and self.state[30] == s and self.state[31] == s and self.state[32] == s:
            self.state[29] = self.state[30] = self.state[31] = self.state[32] = 8
            return True

        elif self.state[30] == s and self.state[31] == s and self.state[32] == s and self.state[33] == s:
            self.state[30] = self.state[31] = self.state[32] = self.state[33] = 8
            return True

        elif self.state[31] == s and self.state[32] == s and self.state[33] == s and self.state[34] == s:
            self.state[31] = self.state[32] = self.state[33] = self.state[34] = 8
            return True  

        elif self.state[35] == s and self.state[36] == s and self.state[37] == s and self.state[38] == s:
            self.state[35] = self.state[36] = self.state[37] = self.state[38] = 8
            return True

        elif self.state[36] == s and self.state[37] == s and self.state[38] == s and self.state[39] == s:
            self.state[36] = self.state[37] = self.state[38] = self.state[39] = 8
            return True

        elif self.state[37] == s and self.state[38] == s and self.state[39] == s and self.state[40] == s:
            self.state[37] = self.state[38] = self.state[39] = self.state[40] = 8
            return True

        elif self.state[38] == s and self.state[39] == s and self.state[40] == s and self.state[41] == s:
            self.state[38] = self.state[39] = self.state[40] = self.state[41] = 8
            return True  

        #diagonal links nach rechts
        elif self.state[14] == s and self.state[22] == s and self.state[30] == s and self.state[38] == s:
            self.state[14] = self.state[22] = self.state[30] = self.state[38] = 8
            return True

        elif self.state[15] == s and self.state[23] == s and self.state[31] == s and self.state[39] == s:
            self.state[15] = self.state[23] = self.state[31] = self.state[39] = 8
            return True

        elif self.state[16] == s and self.state[24] == s and self.state[32] == s and self.state[40] == s:
            self.state[16] = self.state[24] = self.state[32] = self.state[40] = 8
            return True

        elif self.state[17] == s and self.state[25] == s and self.state[33] == s and self.state[41] == s:
            self.state[17] = self.state[25] = self.state[33] = self.state[41] = 8
            return True  

        elif self.state[7] == s and self.state[15] == s and self.state[23] == s and self.state[31] == s:
            self.state[17] = self.state[15] = self.state[23] = self.state[31] = 8
            return True

        elif self.state[8] == s and self.state[16] == s and self.state[24] == s and self.state[32] == s:
            self.state[8] = self.state[16] = self.state[24] = self.state[32] = 8
            return True

        elif self.state[9] == s and self.state[17] == s and self.state[25] == s and self.state[33] == s:
            self.state[9] = self.state[17] = self.state[25] = self.state[33] = 8
            return True

        elif self.state[10] == s and self.state[18] == s and self.state[26] == s and self.state[34] == s:
            self.state[10] = self.state[18] = self.state[26] = self.state[34] = 8
            return True

        elif self.state[0] == s and self.state[8] == s and self.state[16] == s and self.state[24] == s:
            self.state[0] = self.state[8] = self.state[16] = self.state[24] = 8
            return True

        elif self.state[1] == s and self.state[9] == s and self.state[17] == s and self.state[25] == s:
            self.state[1] = self.state[9] = self.state[17] = self.state[25] = 8
            return True

        elif self.state[2] == s and self.state[10] == s and self.state[18] == s and self.state[26] == s:
            self.state[2] = self.state[10] = self.state[18] = self.state[26] = 8
            return True

        elif self.state[3] == s and self.state[11] == s and self.state[19] == s and self.state[27] == s:
            self.state[3] = self.state[11] = self.state[19] = self.state[27] = 8
            return True 

        #diagonal rechts nach links
        elif self.state[20] == s and self.state[26] == s and self.state[32] == s and self.state[38] == s:
            self.state[20] = self.state[26] = self.state[32] = self.state[38] = 8
            return True

        elif self.state[19] == s and self.state[25] == s and self.state[31] == s and self.state[37] == s:
            self.state[19] = self.state[25] = self.state[31] = self.state[37] = 8
            return True

        elif self.state[18] == s and self.state[24] == s and self.state[30] == s and self.state[36] == s:
            self.state[18] = self.state[24] = self.state[30] = self.state[36] = 8
            return True

        elif self.state[17] == s and self.state[23] == s and self.state[29] == s and self.state[35] == s:
            self.state[17] = self.state[23] = self.state[29] = self.state[35] = 8
            return True  

        elif self.state[13] == s and self.state[19] == s and self.state[25] == s and self.state[31] == s:
            self.state[13] = self.state[19] = self.state[25] = self.state[31] = 8
            return True

        elif self.state[12] == s and self.state[18] == s and self.state[24] == s and self.state[30] == s:
            self.state[12] = self.state[18] = self.state[24] = self.state[30] = 8
            return True

        elif self.state[11] == s and self.state[17] == s and self.state[23] == s and self.state[29] == s:
            self.state[1] = self.state[17] = self.state[23] = self.state[29] = 8
            return True

        elif self.state[10] == s and self.state[16] == s and self.state[22] == s and self.state[28] == s:
            self.state[10] = self.state[16] = self.state[22] = self.state[28] = 8
            return True  

        elif self.state[6] == s and self.state[12] == s and self.state[18] == s and self.state[24] == s:
            self.state[6] = self.state[12] = self.state[18] = self.state[24] = 8
            return True

        elif self.state[5] == s and self.state[11] == s and self.state[17] == s and self.state[23] == s:
            self.state[5] = self.state[11] = self.state[17] = self.state[23] = 8
            return True

        elif self.state[4] == s and self.state[10] == s and self.state[16] == s and self.state[22] == s:
            self.state[4] = self.state[10] = self.state[16] = self.state[22] = 8
            return True

        elif self.state[3] == s and self.state[9] == s and self.state[15] == s and self.state[21] == s:
            self.state[3] = self.state[9] = self.state[15] = self.state[21] = 8
            return True
        else:
            return False

class Player:
    def __init__(self, symbol):
        self.symbol = symbol


if __name__ == '__main__':
    player_a = Player(1)
    player_b = Player(-1)
    board = Board()
    active_player = player_a
    while not board.is_full():
        board.print_board()
        try:
            cell = int(input("Where do you want to place your sign? [1-7]"))
        except ValueError:
            continue
        cell = cell - 1
        
        if cell < 0 or cell > 6:
            print("Please enter a number between 1 and 7")
            continue
    
        board.make_turn(cell, active_player)
                               
        if board.check_win(active_player):
            board.print_board()
            print("You wonnered! GW.")            
            break
        
        if active_player == player_a:
            active_player = player_b
        else:
            active_player = player_a  


#Checkwin durch Funktion verkürzen?
>>>>>>> 1a4885328a5a8dc1d535f5ffa97422ff1a3df264:Vier-Gewinnt1.0.py
    