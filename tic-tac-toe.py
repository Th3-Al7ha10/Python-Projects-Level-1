"""
Morpion

Created on Mar 3, 2022

@author: Th3-Al7ha10

"""

import random
from abc import ABCMeta, abstractmethod

class Token:
    def __init__(self,letter):
        self.tag = letter
    def __str__(self):
        return self.tag

    
class MoveToken:
     def __init__(self,i,j,token):
         self.i = i
         self.j = j
         self.token = token
        
class Board:
    def __init__(self):
        self.cases =[[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
    def __str__(self):
        row1 = ' ' + str(self.cases[0][0]) + ' | ' + str(self.cases[0][1]) + ' | ' + str(self.cases[0][2])
        row2 = ' ' + str(self.cases[1][0]) + ' | ' + str(self.cases[1][1]) + ' | ' + str(self.cases[1][2])
        row3 = ' ' + str(self.cases[2][0]) + ' | ' + str(self.cases[2][1]) + ' | ' + str(self.cases[2][2])
        return row1 + '\n' + row2 + '\n' + row3
    
    def is_case_empty(self,row,column):
        return self.cases[row][column] ==' '
    
    def cases_content(self,row,column,token):
        return self.cases[row][column] == token
    
    def show_move(self,movetoken):
        row = self.cases[movetoken.i]
        row[movetoken.j] = movetoken.token
        
    def is_full(self):
        for row in range(2):
            for column in range(2):
                if self.is_case_empty(row,column):
                    return False
        return True
    
    def if_winner(self,player):
        t = player.token
        return (
            (self.cases_content(0, 0, t) and self.cases_content(0, 1, t) and self.cases_content(0, 2, t)) or
            (self.cases_content(1, 0, t) and self.cases_content(1, 1, t) and self.cases_content(1, 2, t)) or
            (self.cases_content(2, 0, t) and self.cases_content(2, 1, t) and self.cases_content(2, 2, t)) or
            (self.cases_content(0, 0, t) and self.cases_content(1, 0, t) and self.cases_content(2, 0, t)) or
            (self.cases_content(0, 1, t) and self.cases_content(1, 1, t) and self.cases_content(2, 1, t)) or
            (self.cases_content(0, 2, t) and self.cases_content(1, 2, t) and self.cases_content(2, 2, t)) or
            (self.cases_content(0, 0, t) and self.cases_content(1, 1, t) and self.cases_content(2, 2, t)) or
            (self.cases_content(0, 2, t) and self.cases_content(1, 1, t) and self.cases_content(2, 0, t)))
        
class Player(metaclass=ABCMeta):
    def __init__(self,board):
        self.board = board
        self._token = None
        
    @property 
    def token(self): 
        """ Represents Players token - may be X or Y""" 
        return self._token 
    
    @token.setter 
    def token(self, value): 
        self._token = value 
    
    @abstractmethod 
    def make_move(self): pass 
    
    def __str__(self): 
        return self.__class__.__name__ + '[' + str(self.token) + ']' 
        
class HumanPlayer(Player):
    def __init__(self, board):
        super().__init__(board)
        
    def get_user_input(self, prompt):
        invalid_input = True
        
        while invalid_input:
            print(prompt)
            user_input = input()
            if not user_input.isdigit():
                print('Input must be a number')
            else:
                user_input_int = int(user_input)
                if user_input_int < 1 or user_input_int > 3:
                    print('input must be a number in the range 1 to 3')
                else:
                    invalid_input = False
        return user_input_int - 1
    
    def make_move(self): 
        """ Allow the human player to enter their move """ 
        while True: 
            row = self.get_user_input('Please input the row: ') 
            column = self.get_user_input('Please input the column: ')
            
            if self.board.is_case_empty(row, column): 
                return MoveToken(row, column,self.token) 
            else: 
                print('That position is not free') 
                print('Please try again') 
                
class ComputerPlayer(Player):
    def __init__(self, board):
        super().__init__(board)
        
    def randomly_select_cell(self): 
        """ Use a simplistic random selection approach to find a cell to fill. """ 
        while True:  
            row = random.randint(0, 2) 
            column = random.randint(0, 2) 
            if self.board.is_case_empty(row, column): 
                return MoveToken(row,column,self.token)
    def make_move(self): 
        """ Provide a very simple algorithm for selecting a move""" 
        if self.board.is_case_empty(1, 1): 
            return MoveToken(1, 1, self.token) 
        elif self.board.is_case_empty(0, 0): 
            return MoveToken(0, 0, self.token) 
        elif self.board.is_case_empty(2, 2): 
            return MoveToken(2, 2, self.token) 
        elif self.board.is_case_empty(0, 2): 
            return MoveToken( 0, 2, self.token) 
        elif self.board.is_case_empty(0, 2): 
            return MoveToken(2, 0, self.token) 
        else: 
            return self.randomly_select_cell() 
class Game: 
    """ Contains the Game Playing Logic """ 
    def __init__(self): 
         self.board = Board() 
         self.human = HumanPlayer(self.board) 
         self.computer = ComputerPlayer(self.board) 
         self.next_player = None 
         self.winner = None 
         
    def select_player_token(self): 
        """ Let the player select their token """ 
        token = '' 
        while not (token == 'X' or token == 'O'): 
            print('Do you want to be X or O?') 
            token = input().upper() 
            if token != 'X' and token != 'O': 
                print('Input must be X or O') 
        if token == 'X': 
            self.human.token = X 
            self.computer.token = O
        else:
            self.human.token = O
            self.computer.token = X
            
    def select_player_to_go_first(self):
        """ Randomly selects who will play first - the human or the computer."""
        if random.randint(0, 1) == 0:
            self.next_player = self.human
        else:
            self.next_player = self.computer
    
    def play(self):
        """ Main game playing loop """
        print('Welcome to TicTacToe')
        
        self.select_player_token()
        self.select_player_to_go_first()
        
        print(self.next_player, 'will play first')
        
        while self.winner is None:
        # Human players move
            if self.next_player == self.human:
               print(self.board)
               print('Your move')
               move = self.human.make_move()
               self.board.show_move(move)
               
               if self.board.if_winner(self.human):
                   self.winner = self.human
               else:
                   self.next_player = self.computer
        # Computers move
            else:
                print('Computers move')
                move = self.computer.make_move()
                self.board.show_move(move)
                
                if self.board.if_winner(self.computer):
                    self.winner = self.computer
                else:
                    self.next_player = self.human
                # Check for a winner or a draw
            if self.winner is not None:
                print('Game Over! The Winner is the ' + str(self.winner))
            elif self.board.is_full():
                print('Game is a Tie')
                break
        print(self.board)

if __name__ == "__main__":
    
    X = Token('X') 
    O = Token('O') 
    
    game = Game() 
    game.play() 
    
    
    
