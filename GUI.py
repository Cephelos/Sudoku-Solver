import pygame as pg
from Solver import *

pg.init()

global num_wrong
num_wrong = 0

win_width = 675
win_height = 675

line_width = 4

pencil = pg.font.SysFont('Arial', 30)
pen = pg.font.SysFont('Arial', 70)



win = pg.display.set_mode((win_width+20, win_height+50))
pg.display.set_caption("Sudoku")




class Tile:

    def __init__(self, x, y, value=0, filled='pencil', in_box=None):
        self.x = x
        self.y = y
        self.value = value
        self.filled = filled
        self.in_box = in_box


    def draw(self):
        global num_wrong
        (mouse_x, mouse_y) = pg.mouse.get_pos()

        if mouse_x > self.x+line_width and mouse_x < self.x+win_width/9-line_width and mouse_y > self.y+line_width and mouse_y < self.y+win_height/9-line_width:
            pg.draw.rect(win, (255, 0, 0), (self.x, self.y, win_width / 9+line_width, win_height / 9+line_width))

            if keys[pg.K_1] and self.filled != "pen":
                self.value = 1
            if keys[pg.K_2] and self.filled != "pen":
                self.value = 2
            if keys[pg.K_3] and self.filled != "pen":
                self.value = 3
            if keys[pg.K_4] and self.filled != "pen":
                self.value = 4
            if keys[pg.K_5] and self.filled != "pen":
                self.value = 5
            if keys[pg.K_6] and self.filled != "pen":
                self.value = 6
            if keys[pg.K_7] and self.filled != "pen":
                self.value = 7
            if keys[pg.K_8] and self.filled != "pen":
                self.value = 8
            if keys[pg.K_9] and self.filled != "pen":
                self.value = 9

            if keys[pg.K_RETURN] and self.value is not 0 and self.filled != "pen":
                print(self.x, self.y)
                if board[int(self.y/75)][int(self.x/75)] != self.value:
                    num_wrong += 1

                    self.value = 0

                else:
                    self.filled = 'pen'

            if keys[pg.K_BACKSPACE] and self.filled != "pen":
                self.filled = 'pencil'
                self.value = 0

        if self.value == 0:
            self.in_box = ' '
        else:
            self.in_box = self.value

        pg.draw.rect(win, (255, 255, 255), (self.x+line_width, self.y+line_width, win_width/9-line_width, win_height/9-line_width))
        if self.filled == "pencil":
            val = pencil.render(str(self.in_box), True, (150, 150, 150))
            win.blit(val, (self.x+5, self.y))
        if self.filled == "pen":
            val = pen.render(str(self.in_box), True, (0, 0, 0))
            win.blit(val, (self.x+20, self.y))


run = True

tiles = []
keys = []

board = [[0, 4, 0, 8, 0, 5, 2, 0, 0],
         [0, 2, 0, 0, 4, 0, 0, 5, 0],
         [5, 0, 0, 0, 0, 0, 0, 0, 4],
         [0, 9, 0, 0, 0, 3, 1, 2, 0],
         [1, 0, 6, 0, 7, 8, 0, 0, 3],
         [3, 7, 0, 9, 0, 4, 0, 8, 0],
         [0, 0, 0, 0, 0, 6, 7, 0, 0],
         [0, 0, 8, 3, 5, 9, 0, 1, 0],
         [0, 1, 9, 0, 0, 7, 6, 0, 0]]


new_board = []

solution_board = []

for i in board:
    new_board = new_board + i

fill_board(board)

for i in range(0, win_width, int(win_width/3)+8):
    for k in range(3):
        for j in range(0, win_height, int(win_height/3)+8):

            for m in range(3):
                tiles.append(Tile(m*win_width/9+j, k*win_height/9+i, 0))


for i in range(len(tiles)):
    tiles[i].value = new_board[i]
    if tiles[i].value != 0:
        tiles[i].filled = 'pen'

timer = 0
seconds = 0
minutes = 0
hours = 0

while run:
    clock = pg.time.Clock()
    clock.tick(60)
    timer += 1
    win.fill((0, 0, 0))
    done = True

    if timer % 60 == 0:
        timer = 0
        seconds += 1
    if seconds % 60 == 0 and timer % 60 == 0:
        seconds = 0
        minutes += 1
    if minutes % 60 == 0 and seconds % 60 == 0 and timer % 60 == 0:
        minutes = 0
        hours += 1

    keys = pg.key.get_pressed()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    for i in tiles:
        i.draw()
        if i.filled == 'pencil':
            done = False
    if done == True:
        val = pencil.render("You Win!", True, (0, 255, 0))
        win.blit(val, (300, 690))
    val = pencil.render("Wrong Guesses: " + str(num_wrong), True, (255, 0, 0))
    win.blit(val, (0, 690))

    val = pencil.render("Time: " + str(hours) + ":" + str(minutes) + ":" + str(seconds), True, (255, 255, 255))
    win.blit(val, (500, 690))



    pg.display.update()



pg.quit()
