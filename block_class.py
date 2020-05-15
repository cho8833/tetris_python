import pygame
import random
import time
import threading
from shape1 import *
board = []
board.append([4,4,4,4,4,4,4,4,4,4,4,4])
for y in range(20):
    board.append([3,0,0,0,0,0,0,0,0,0,0,2])
length = 27
bimage = pygame.image.load('nemo.png')
block_image = pygame.image.load('exist.png')
shadow_image = pygame.image.load('shadow.png')
screen = pygame.display.set_mode((500,600))
#exist = 1 right end = 2 left end = 3 bottom = 4 shadow = 5
class block(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        global board
        self.move = random.choice(shape)
        #self.move = shape[3]
        self.image = block_image
        self.state = 0
        self.xb = 3     #initial x position
        self.yb = 20    #initial y position
        self.shadow = self.move[:]
        self.shape_to_board()
        self.get_shadow()
        draw_board()
    def get_shadow(self):
        global board
        for y in range(1,20,1):
            for x in range(1,11,1):
                if board[y][x] == 5:
                    board[y][x] = 0
        save_xb = self.xb
        save_yb = self.yb
        if self.space() == 'new':
            xb = self.xb
            yb = self.yb
            for y in self.move[self.state]:
                for x in y:
                    if x== 1:
                        if board[yb][xb] == 1:
                            board[yb][xb] = 5
                    xb += 1
                xb = self.xb
                yb -= 1
        self.xb = save_xb
        self.yb = save_yb
        self.shape_to_board()                             
    def check_board(self,xb_,yb_,state):
        global board
        xb = xb_
        yb = yb_
        self.init_trace()
        for y in self.move[state]:
            for x in y :
                if x == 1:
                    if board[yb][xb] == 1:
                        return 'exist'
                    elif board[yb][xb] == 2:
                        return 'right end'
                    elif board[yb][xb] == 3:
                        return 'left end'
                    elif board[yb][xb] == 4:
                        return 'bottom'
                xb += 1
            xb = xb_
            yb -= 1
        return True
    def turn(self):
        s = self.state +1 
        if s  > 3:
            s = 0
        while True:
            check = self.check_board(self.xb,self.yb,s)
            if check == True:
                self.init_trace()
                self.state = s
                break
            elif check == 'right end':
                self.init_trace()
                self.xb -= 1
            elif check == 'left end':
                self.init_trace()
                self.xb += 1
            elif check == 'bottom':
                self.init_trace()
                self.yb += 1
            elif check == 'exist':
                self.init_trace()
                self.yb += 1
        self.shape_to_board()
        self.get_shadow()
        draw_board()
    def shape_to_board(self):       #board insert
        xb = self.xb
        yb = self.yb
        for y in self.move[self.state]:
            for x in y:
                if x== 1:
                    board[yb][xb] = 1
                xb += 1
            xb = self.xb
            yb -= 1
    def init_trace(self):
        xb = self.xb
        yb = self.yb
        for y in self.move[self.state]:
            for x in y:
                if x == 1:
                    board[yb][xb] = 0
                xb += 1
            xb = self.xb
            yb -= 1
    def down(self):
        check = self.check_board(self.xb,self.yb-1,self.state)
        if check == True:
            self.init_trace()
            self.yb -= 1
        elif check == 'exist' or 'bottom':
            self.shape_to_board()
            draw_board()
            return 'new'
        elif check == 'right end' or check == 'left end':
            return
        self.shape_to_board()
        draw_board()
    def left(self):
        check = self.check_board(self.xb-1,self.yb,self.state)
        if check == True:
            self.init_trace()
            self.xb -= 1
            self.get_shadow()
        elif check == 'exist' or 'bottom':
            return 'new'
        elif check == 'right end' or check == 'left end':
            return
        self.shape_to_board()
        draw_board()
    def right(self):
        check = self.check_board(self.xb+1,self.yb,self.state)
        if check == True:
            self.init_trace()
            self.xb += 1
            self.get_shadow()
        elif check == 'exist' or 'bottom':
            return 'new'
        elif check == 'right end' or check == 'left end':
            return
        self.shape_to_board()
        draw_board()
    def space(self):
        while True:
            if self.down() == 'new':
                return 'new'
def draw_board():      #draw board
    global board
    xb = 0
    yb = length * 20
    global screen
    for y in board:
        for x in y:
            if x == 0:
                screen.blit(bimage,(xb,yb))
            elif x == 1:
                screen.blit(block_image,(xb,yb))
            elif x == 5:
                screen.blit(shadow_image,(xb,yb))
            xb += length
        xb = 0
        yb -= length
def line_check():
    global board
    for y_ in range(1,20,1):
        if board[y_] == [3,1,1,1,1,1,1,1,1,1,1,2]:
            print('clear')
            board[y_] = [3,0,0,0,0,0,0,0,0,0,0,2]
            for yb_ in range(y_,19,1):
                board[yb_] = board[yb_+1][:]
            board[20] = [3,0,0,0,0,0,0,0,0,0,0,2]
            return
    return 'clear'
