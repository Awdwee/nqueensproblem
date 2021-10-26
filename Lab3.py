import time
import random
import numpy as np
import math
from tkinter import *
import threading

import Chess


class Queens(object):
    """An N-queens candidate solution."""

    def __init__(self, N):
        """A random N-queens instance. There is a queen in every column. The
queen in column i is in row board[i]"""
        self.board = dict()
        for col in range(N):
            row = random.choice(range(N))
            self.board[col] = row

    def copy(self, q):
        """Copy a candidate solution (prevent aliasing)"""
        self.board = q.board.copy()

    def actions(self):
        """Return a list of possible actions given the current placements."""
        ####################
        # YOU FILL THIS IN #
        ####################
        action_list = []
        for col in range(len(self.board)):
            for row in range(len(self.board)):
                if self.board[col] != row:
                    action_list.append((col, row))

        return action_list

    def cost(self):
        """Compute the cost of this solution."""
        ####################
        # YOU FILL THIS IN #
        ####################
        cost = 0
        for i in range(len(self.board)):
            for j in range(i + 1, len(self.board)):
                if (self.board[i] == self.board[j]) or (abs(i - j) == abs(self.board[i] - self.board[j])):
                    print(self.board[i], self.board[j])
                    cost += 1
        print("Cost of move: " + str(cost))
        return cost

    def neighbor(self, action):
        xCopy = Queens(8)
        xCopy.copy(self)
        xCopy.board[action[0]] = action[1]
        return xCopy


class QueensSearch(object):

    def __init__(self, root, N):
        self.root = root
        self.N = N

    def run(self):
        env = Chess.ChessEnvironment(self.root, self.N)
        x = Queens(self.N)
        steps = 1
        maxsteps = 5
        counter = 0
        while x.cost() > 0 and steps < maxsteps:
            ####################
            # YOU FILL THIS IN #
            ####################
            y = x.neighbor(random.choice(x.actions()))
            steps = 1
            if (y.cost() < x.cost()):
                x = y
            else:
                c = y.cost() - x.cost()
                p = math.e ** (((-c) / (steps * .001)))

                if (p > random.uniform(0, 1)):
                    x = y
            env.display(x)
            steps += steps + 1
            counter += 1
            env.display(x)
            steps += 1
        print("Solved after {} steps.\n".format(steps))


if __name__ == '__main__':
    ## Initialize environemnt
    root = Tk()
    root.title("N-Queens")
    root.geometry("600x500")
    search = QueensSearch(root, 8)
    search.run()
    root.mainloop()
