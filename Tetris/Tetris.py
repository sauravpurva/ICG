import random, pygame, sys
from pygame.locals import *

def generatePiece():

    pieceChoices = (PIECE_T, PIECE_L, PIECE_J, PIECE_Z, PIECE_S, PIECE_O, PIECE_I)
    pieceShape = random.choice(pieceChoices)
    
    if pieceShape == PIECE_T:
        pieceColors = {'lite': LITERED, 'dark': DARKRED}
    elif pieceShape == PIECE_L:
        pieceColors = {'lite': LITEBLUE, 'dark': DARKBLUE}
    elif pieceShape == PIECE_J:
        pieceColors = {'lite': LITEGREEN, 'dark': DARKGREEN}
    elif pieceShape == PIECE_Z:
        pieceColors = {'lite': LITEYELLOW, 'dark': DARKYELLOW}
    elif pieceShape == PIECE_S:
        pieceColors = {'lite': LITEPURPLE, 'dark': DARKPURPLE}
    elif pieceShape == PIECE_O:
        pieceColors = {'lite': LITEORANGE, 'dark': DARKORANGE}
    elif pieceShape == PIECE_I:
        pieceColors = {'lite': LITETEAL, 'dark': DARKTEAL}

    return pieceShape, pieceColors
    

def movePiece(piece, direction):

    if direction == UP:
        for i in range(len(piece)):
            piece[i]['y'] -= 1
    if direction == DOWN:
        for i in range(len(piece)):
            piece[i]['y'] += 1
    if direction == LEFT:
        for i in range(len(piece)):
            piece[i]['x'] -= 1
    if direction == RIGHT:
        for i in range(len(piece)):
            piece[i]['x'] += 1

    return piece


def rotatePiece(piece, pile):

    piv_x = piece[PIVOT]['x'] 
    piv_y = piece[PIVOT]['y']

    piece_copy = [{'x': piv_x, 'y': piv_y, 'block colors': piece[PIVOT]['block colors']}]

    for n in range(1, 4):
        
        up          =   {'x': piv_x    , 'y': piv_y - n, 'block colors': piece[PIVOT]['block colors']}
        down        =   {'x': piv_x    , 'y': piv_y + n, 'block colors': piece[PIVOT]['block colors']}
        left        =   {'x': piv_x - n, 'y': piv_y    , 'block colors': piece[PIVOT]['block colors']}
        right       =   {'x': piv_x + n, 'y': piv_y    , 'block colors': piece[PIVOT]['block colors']}
        left_up     =   {'x': piv_x - n, 'y': piv_y - n, 'block colors': piece[PIVOT]['block colors']} 
        right_up    =   {'x': piv_x + n, 'y': piv_y - n, 'block colors': piece[PIVOT]['block colors']}
        left_down   =   {'x': piv_x - n, 'y': piv_y + n, 'block colors': piece[PIVOT]['block colors']}
        right_down  =   {'x': piv_x + n, 'y': piv_y + n, 'block colors': piece[PIVOT]['block colors']}
        
        if up in piece:
            piece_copy.append(right)
        if down in piece:
            piece_copy.append(left)
        if left in piece:
            piece_copy.append(up)
        if right in piece:
            piece_copy.append(down)
        if left_up in piece:
            piece_copy.append(right_up)
        if right_up in piece:
            piece_copy.append(right_down)
        if right_down in piece:
            piece_copy.append(left_down)
        if left_down in piece:
            piece_copy.append(left_up)

    for pieceCopyBlock in piece_copy:
        if pieceCopyBlock['x'] > CELLWIDTH_TETRIS-1 or pieceCopyBlock['x'] < 0 or pieceCopyBlock['y'] > CELLHEIGHT-2: 
            return piece
        for pileBlock in pile:
            if pieceCopyBlock['x'] == pileBlock['x'] and pieceCopyBlock['y'] == pileBlock['y']:
                return piece
    
    return piece_copy



FPS = 25
WINDOWWIDTH_TOTAL = 480
WINDOWWIDTH_TETRIS = 300
WINDOWWIDTH_SIDE = WINDOWWIDTH_TOTAL-WINDOWWIDTH_TETRIS
WINDOWHEIGHT = 600
CELLSIZE = 20
assert WINDOWWIDTH_TETRIS % CELLSIZE == 0, #Window width must be a multiple of cell size.
assert WINDOWHEIGHT % CELLSIZE == 0, #Window height must be a multiple of cell size.
assert WINDOWWIDTH_TOTAL > WINDOWWIDTH_TETRIS, #Tetris window is larger than total window.
CELLWIDTH_TOTAL = int(WINDOWWIDTH_TOTAL/CELLSIZE)
CELLWIDTH_TETRIS = int(WINDOWWIDTH_TETRIS/CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT/CELLSIZE)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY  = (40, 40, 40)

LITERED = (255, 0, 0)
DARKRED = (155, 0, 0)
LITEGREEN = (0, 255, 0)
DARKGREEN = (0, 180, 0)
LITEBLUE = (0, 0, 255)
DARKBLUE = (0, 0, 155)
LITEYELLOW = (255, 255, 0)
DARKYELLOW = (200, 200, 0)
LITEPURPLE = (255, 0, 255)
DARKPURPLE = (155, 0, 155)
LITEORANGE = (255, 128, 0)
DARKORANGE = (255, 75, 0)
LITETEAL = (0, 175, 175)
DARKTEAL = (0, 128, 128)

BGCOLOR = BLACK
TEXTCOLOR = WHITE
GRIDCOLOR = GRAY

ROTATE_CW = 'rotate right'
ROTATE_CCW = 'rotate left'

PIECE_T = 't-shaped piece'
PIECE_L = 'l-shaped piece 1'
PIECE_J = 'j-shaped piece 2'
PIECE_Z = 'z-shaped piece 1'
PIECE_S = 's-shaped piece 2'
PIECE_O = 'o-shaped piece' 
PIECE_I = 'i-shaped piece'

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

PIVOT = CURRENTPIECE = 0
NEXTPIECE = 1

CURRENTPIECE_STARTX = int(CELLWIDTH_TETRIS/2)
CURRENTPIECE_STARTY = 1
NEXTPIECE_STARTX = 19 ## requires tweaking if window dimensions are changed
NEXTPIECE_STARTY = 6 ## requires tweaking if window dimensions are changed

def main():

    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH_TOTAL, WINDOWHEIGHT))
    BASICFONT = pygame.font.SysFont('Courier New', 24)
    pygame.display.set_caption('Tetris')

    while True:
        pygame.mixer.music.load('tetrissong.mid')
        pygame.mixer.music.play(-1, 0.0)
        runGame()
        pygame.mixer.music.stop()
        showGameOver()

def runGame(): #incomplete

    pieces = [[],[]]

def terminate():
        
    pygame.quit()
    sys.exit()
        
if __name__ == '__main__':
    main()
