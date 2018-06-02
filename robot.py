# -----------------------------------------------------------------------------
# Name:       robot
# Purpose:    class definition for robots
#
# Author: Alexander Park
# Date:11/13/17
# -----------------------------------------------------------------------------

"""
Module to describe and control robot objects in a maze.
"""
import tkinter


class Robot(object):
    """
    This is a Robot that is represented by a rectangle along a maze that it
    defines as its environment of boundaries that have obstacles within it.
    The robot cannot land on a obstacle, nor can it leave its boundaries,
    and cannot move if it loses battery fully, but can recharge. Each move
    removes a unit from its batter which starts full upon instantiation.

    Arguments:
    str - name, str - color, int - row=0, int - column=0

    Attributes:
    class: unit_size,maze,maze_size,full
    instance: name, color, column, row, battery

    """

    # class variable used by the show method
    unit_size = 60

    # Class variable describing the maze
    # False represents an obstacle, True represents open space
    maze = [[True, True, False, True, True, True, False, True, True, True],
            [True, True, False, True, True, True, False, True, True, True],
            [True, False, True, True, True, True, False, True, True, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, False, False, False, False, True, True, True, True, True],
            [True, True, False, True, True, True, True, True, False, True],
            [True, False, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True]]

    maze_size = len(maze)
    # class variable to represent a full charge
    # A robot with a fully charged battery can take up to 20 steps
    full = 20

    def __init__(self,  name, color, row=0, column=0):
        self.battery = self.full
        self.color = color
        self.name = name
        self.row = row
        self.column = column

    def __str__(self):
        return "{0} is a {1} robot lost in the maze".format(self.name,
                                                           self.color)

    def __gt__(self, other):
        return self.battery>other.battery

    def recharge(self):
        """
        Recharges battery to full for the robot
        :returns self itself
        """
        self.battery=self.full
        return self

    def one_step_forward(self):
        """
        Makes the robot go one step forward if it has energy and within its
        space and not colliding with any other obstacles
        :argument None
        :returns boolean flag - true or false of successful step
        """
        if(self.row+1>=len(self.maze)):
            return False
        elif(self.battery==0):
            return False
        elif(self.maze[self.row+1][self.column]==False):
            return False
        else:
            self.row+=1
            self.battery-=1
            return True

    def one_step_back(self):
        """
        Makes the robot go one step back if it has energy and within its space
        and not colliding with any other obstacles
        :argument None
        :returns boolean flag - true or false of successful step
        """
        if (self.row -1<0):
            return False
        elif (self.battery == 0):
            return False
        elif (self.maze[self.row - 1][self.column] == False):
            return False
        else:
            self.row -= 1
            self.battery -= 1
            return True
    def one_step_right(self):
        """
        Makes the robot go one step right if it has energy and within its space
        and not colliding with any other obstacles
        :argument None
        :returns boolean flag - true or false of successful step
        """
        if (self.column+ 1 >=len(self.maze[0])):
            return False
        elif (self.battery == 0):
            return False
        elif (self.maze[self.row][self.column+1] == False):
            return False
        else:
            self.column += 1
            self.battery -= 1
            return True

    def one_step_left(self):
        """
        Makes the robot go one step left if it has energy and within its space
        and not colliding with any other obstacles
        :argument None
        :returns boolean flag - true or false of successful step
        """
        if (self.column-1 <0):
            return False
        elif (self.battery == 0):
            return False
        elif (self.maze[self.row][self.column-1] == False):
            return False
        else:
            self.column-=1
            self.battery -= 1
            return True

    def forward(self, steps):
        """
        :argument steps - the number of steps to take in forward direction
        :returns None
        """

        for i in range(0,steps):
            if(not self.one_step_forward()):
                break


    def backward(self, steps):
        """
        :argument steps - the number of steps to take in backward direction
        :returns None
        """
        for i in range(0,steps):
            if(not self.one_step_back()):
                break


    def right(self, steps):
        """
        :argument steps - the number of steps to take in right direction
        :returns None
        """
        for i in range(0,steps):
            if(not self.one_step_right()):
                break

    def left(self, steps):
        """
        :argument steps - the number of steps to take in left direction
        :returns None
        """
        for i in range(0,steps):
            if(not self.one_step_left()):
                break

    # The method below has been written for you
    # You can use it when testing your class

    def show(self):
        """
        Draw a graphical representation of the robot in the maze.

        The robot's position and color are shown.
        The color is assumed to be one of the colors recognized by tkinter
        (https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm)
        If the robot's battery is empty, the robot is shown in a
        horizontal position. Otherwise the robot is shown in an upright
        position.
        The obstacles in the maze are shown in red.

        Parameter: None
        Return: None
        """
        root = tkinter.Tk()
        root.title(self.name + ' in the Maze')
        canvas = tkinter.Canvas(root, background='light green',
                                width=self.unit_size * self.maze_size,
                                height=self.unit_size * self.maze_size)
        canvas.grid()

        # draw a representation of the robot in the maze
        if self.battery:
            upper_x = self.column * self.unit_size + self.unit_size / 4
            upper_y = self.row * self.unit_size
            lower_x = upper_x + self.unit_size / 2
            lower_y = upper_y + self.unit_size
            eye_x = lower_x - 3 * self.unit_size / 20
            eye_y = upper_y + self.unit_size / 10

        else: # the robot ran out of battery
            upper_x = self.column * self.unit_size
            upper_y = self.row * self.unit_size + self.unit_size / 2
            lower_x = upper_x + self.unit_size
            lower_y = upper_y + self.unit_size / 2
            eye_x = lower_x - 9 * self.unit_size / 10
            eye_y = lower_y - 3 * self.unit_size / 20

        rectangle = canvas.create_rectangle(upper_x,
                                            upper_y,
                                            lower_x,
                                            lower_y,
                                            fill=self.color)
        # draw the robot's eyes
        canvas.create_oval(upper_x + self.unit_size / 10,
                           upper_y + self.unit_size / 10,
                           upper_x + 3 * self.unit_size / 20,
                           upper_y + 3 * self.unit_size / 20,
                           fill='black')
        canvas.create_oval(eye_x,
                           eye_y,
                           eye_x + self.unit_size / 20,
                           eye_y + self.unit_size / 20,
                           fill='black')
        # draw the obstacles in the maze
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                if not self.maze[row][col]:
                    canvas.create_rectangle(col * self.unit_size,
                                            row * self.unit_size,
                                            (col + 1) * self.unit_size,
                                            (row + 1) * self.unit_size,
                                            fill='red')
        for row in range(self.maze_size):
            canvas.create_line(0,
                               row * self.unit_size,
                               self.maze_size * self.unit_size,
                               row * self.unit_size)
        for col in range(self.maze_size):
            canvas.create_line(col * self.unit_size,
                               0,
                               col * self.unit_size,
                               self.maze_size * self.unit_size)
        root.mainloop()


# Enter you UnderwaterRobot Class definition below
class UnderwaterRobot(Robot):
    """
    Subclass of Robot which has virtually all the characteristics as Robot
    except that it has dive(distance)
    """
    def __init__(self,  name, color, depth, row=0, column=0):
        super().__init__(name,color,row,column)
        self.depth = depth

    def __str__(self):
        return "{0} is a {1} robot diving underwater".format(self.name,
                                                             self.color)

    def dive(self,distance):
        """

        :param distance: int depth
        :return: None
        """
        self.depth+=distance