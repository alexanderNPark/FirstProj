# -----------------------------------------------------------------------------
# Name:       tictac
# Purpose:    Implement a game of Tic Tac Toe
#
# Author:Alexander park
# -----------------------------------------------------------------------------
'''
Contains the Tic tac toe game object which starts a game of tic tac toe
against the computer upon running the module
'''
import tkinter
import random


class Game(object):
    '''
    Implements the tic tac toe game of a 3x3 grid with a restart button and
    status checking of win or loss
    square_size - default tile size
    tiles - grid of the game (3x3)
    user_value - the input of the user's move
    computer - the input of the computer's move
    you_win, computer_win,tie - game states depending on the outcome of the
    game
    '''

    # Add your class variables if needed here - square size, etc...)
    square_size = 80
    tiles=[[1,1,1],[1,1,1],[1,1,1]]
    user_value = 7
    computer = 100 # relatively prime numbers have no possible intersection
    # of linear combinations when summating the numbers to get a single
    # modulo of 0, for example 2 and 5 have intersections of 3 in a row like
    #  5*2 is mod 6 ==0 because 2*3 the sum of 3 in a row of me has to have
    # more weight to create a modulo class that is not intersecting

    you_win = False
    computer_win = False
    tie = False


    def __init__(self, parent):
        self.root = parent
        parent.title('Tic Tac Toe')
        # Create the restart button widget
        button = tkinter.Button(parent,text="Restart",command=self.restart)
        button.grid()
        self.canvas = tkinter.Canvas(self.root, width=240,
                                height=240, background="white")
        self.canvas.bind("<Button-1>", self.play)
        self.draw()
        self.canvas.grid()
        # Create a label widget for the win/lose message
        self.status = tkinter.Label(parent)

        self.status.grid()
        # Create any additional instance variable you need for the game


    def draw(self):
        """
        Part of initializing the canvas and restarting the canvas where it
        draws a white box and adds grid lines
        :return: None
        """

        self.canvas.create_rectangle(0,0,240,240,fill="white")
        """
        for i in range(len(self.tiles)):

            for j in range(len(self.tiles)):
                canvas.create_rectangle(1+i*(self.square_size),
                                        1+j*(self.square_size),
                                        self.square_size,self.square_size,
                                        fill="red")
                print(1+i*self.square_size,",",1+j*self.square_size)
        """
        for i in range(len(self.tiles)):
            self.canvas.create_line(0,i*self.square_size,240,
                                    i*self.square_size,
                               fill="black"
                               )
            self.canvas.create_line(i*self.square_size,0,i*self.square_size,
                                    240,
                               fill="black")









    def check_status(self):
        """
        checks status of the game of whether it should end or not
        ending in either win, lose or tie (if all the tiles are filled but
        no win nor loss occurred)
        :return: boolean state of game
        """
        def is_full():
            for i in range(len(self.tiles)):
                for j in range(len(self.tiles[0])):
                    if (self.tiles[i][j] == 1):
                        return False

            return True

        def won(player):
            """
            Measures 3 in a row sum based on players values. 300 inverse mod
            7 has a prime inverse of 43 which is impossible to obtain with
            multiples or linear combinations of 3, so I picked 7 and 100 to
            be my choices
            :param player: the player value 7 or 100
            :return: boolean of win or loss of the player in question
            computer or user
            """
            win_val = player*3
            for i in range(len(self.tiles)):
                sum=0
                for j in range(len(self.tiles)):
                    sum+=self.tiles[i][j]

                if(sum%win_val==0):
                    return True

            for i in range(len(self.tiles)):
                sum=0
                for j in range(len(self.tiles)):
                    sum+=self.tiles[j][i]

                if(sum%win_val==0):
                    return True

            diagonal_one = self.tiles[0][0]+self.tiles[1][1]+self.tiles[2][2]
            diagonal_two = self.tiles[0][2]+self.tiles[1][1]+self.tiles[2][0]
            if(diagonal_one%win_val==0 or diagonal_two%win_val==0):
                return True

            return False

        if(won(self.user_value)):
            self.status.configure(text="YOU WIN!")
            self.you_win=True
            return True
        elif(won(self.computer)):
            self.status.configure(text="YOU LOSE!")
            self.computer_win=True
            return True
        elif(is_full()):
            self.status.configure(text="TIE!")
            self.tie=True
            return True
        else:
            return False


    def restart(self):
        """
        restarts the game and all of its states
        :return: None
        """
        # This method is invoked when the user clicks on the RESTART button.

        self.draw()
        self.you_win=False
        self.computer_win=False
        self.tie=False
        self.status.configure(text="")
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles)):
                self.tiles[i][j]=1



    def play(self, event):
        """
        callback method that measures which tiles are matchable with the
        mouse press. If the tile is chosen, nothing happens, also performs
        computer move
        :param event: the callback event
        :return: None
        """
        if(self.you_win or self.computer_win or self.tie):
            return
        pos_x = event.x
        pos_y = event.y
        # This method is invoked when the user clicks on a square.
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles)):
                if(pos_x>=self.square_size*i and pos_x<self.square_size*(
                            i+1) and pos_y>=self.square_size*j and
                           pos_y<self.square_size*(j+1)):
                    if(self.tiles[i][j]==1):
                        self.fill_square(i,j,self.user_value)
                    else:
                        return
        #checks status again because your move changes state
        if(not self.check_status()):
            while(True):
                comp_x = random.randint(0,2)
                comp_y = random.randint(0,2)
                if(self.tiles[comp_x][comp_y]==1):
                    self.fill_square(comp_x,comp_y,self.computer)
                    break

        #check before leaving since the computer move changes state
        self.check_status()


    def fill_square(self,i,j,turn):
        """
        fills square based on parameter
        :param i: x location
        :param j: y location
        :param turn: int representing the value of the player
        :return: None
        """
        if(turn==self.computer):
            color = "blue"
        else:
            color='red'
        self.canvas.create_rectangle(i*self.square_size,j*self.square_size,
                                     (i+1)*self.square_size,
                                     (j+1)*self.square_size,
                                     fill=color)
        self.tiles[i][j] = turn




def main():
    root = tkinter.Tk()
    g = Game(root)
    root.mainloop()
    # Instantiate a root window
    # Instantiate a Game object
    # Enter the main event loop



if __name__ == '__main__':
    main()