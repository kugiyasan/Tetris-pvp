import pygame
import random
import sys, os

class Tetrisapp:
    sqSize = 30
    pieceColor =   [[0  , 0  , 0  ],
                    [0  , 255, 255],
                    [255, 255, 0  ],
                    [255, 0  , 255],
                    [255, 0  , 0  ],
                    [0  , 255, 0  ],
                    [255, 127, 0  ],
                    [0  , 0  , 255]]

    pieceShapeDef = [[[0]],

            [[1, 1, 1, 1]],

            [[2, 2],
             [2, 2]],

            [[3, 3, 3],
             [0, 3, 0]],

            [[4, 4, 0],
             [0, 4, 4]],

            [[0, 5, 5],
             [5, 5, 0]],

            [[6, 6, 6],
             [6, 0, 0]],

            [[7, 7, 7],
             [0, 0, 7]]]

    

    def __init__(self):
        self.timeSinceLastUpdate = 0
        self.newPiece()

        self.grid = [None] * 10
        for i in range(len(self.grid)):
            self.grid[i] = [0] * 20

        path = os.path.dirname(sys.argv[0])
        
        pygame.mixer.music.load(path + '/tetris-99-main-theme.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        
    def update(self):
        if pygame.time.get_ticks() > self.timeSinceLastUpdate + 500:
            self.timeSinceLastUpdate = pygame.time.get_ticks()
            self.thisPieceY += 1
            if self.colliding():
                self.thisPieceY -= 1
                for x in range(len(self.thisPieceShape)):
                    for y in range(len(self.thisPieceShape[x])):
                        if (self.thisPieceShape[x][y] != 0):
                            self.grid[x + self.thisPieceX][y + self.thisPieceY] = self.thisPieceShapeNumber
                self.deleteLine()
                self.newPiece()

    def colliding(self):
        if self.thisPieceY + len(self.thisPieceShape[0]) > 20:
            return True
        else:
            for x in range(len(self.thisPieceShape)):
                for y in range(len(self.thisPieceShape[x])):
                    if self.grid[self.thisPieceX + x][self.thisPieceY + y] != 0 and self.thisPieceShape[x][y] != 0:
                        return True
        return False

    def deleteLine(self):
        zipGrid = list(zip(*self.grid))
        for x in range(20):
            if not 0 in zipGrid[x]:
                del zipGrid[x]
                zipGrid.insert(0, [0] * 10)
        self.grid = zip(*zipGrid)
        self.grid = list(map(list, self.grid))

    def newPiece(self):
        self.thisPieceShapeNumber = random.randint(1, 7)
        self.thisPieceShape = self.pieceShapeDef[self.thisPieceShapeNumber]
        self.thisPieceColor = self.pieceColor[self.thisPieceShapeNumber]
        # self.thisPieceX = len(self.grid) // 2 - len(self.thisPieceShape[0])//2
        self.thisPieceX = 4
        self.thisPieceY = 0

    def rotatePiece(self):
        # newPieceShape = []
        # for x in range(len(self.thisPieceShape)):
        #     for y in range(len(self.thisPieceShape[x])):
        #         newPieceShape[y][x] = self.thisPieceShape[x][y]
        # https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
        self.thisPieceShape = list(zip(*self.thisPieceShape[::-1]))
        if self.thisPieceX + len(self.thisPieceShape) > 10:
                    self.thisPieceX = 10 - len(self.thisPieceShape)
        

    def show(self, DISPLAY, offsetX, offsetY):
        # print("grid = ") # Grid in the console
        # for y in range(len(self.grid[0])):
        #     row = []
        #     for x in range(len(self.grid)):
        #         row.append(self.grid[x][y])
        #     print(row)
        pygame.draw.rect(DISPLAY, (0, 0, 50), (offsetX, offsetY, self.sqSize*len(self.grid), self.sqSize*len(self.grid[0])))
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if (self.grid[x][y] != 0):
                    pygame.draw.rect(DISPLAY, self.pieceColor[self.grid[x][y]], (x*self.sqSize + offsetX, y*self.sqSize + offsetY, self.sqSize, self.sqSize))
        
        for x in range(len(self.thisPieceShape)):
            for y in range(len(self.thisPieceShape[x])):
                if (self.thisPieceShape[x][y] != 0):
                    rectInfo = pygame.Rect(self.sqSize * (self.thisPieceX + x) + offsetX, self.sqSize * (self.thisPieceY + y) + offsetY, self.sqSize, self.sqSize)
                    pygame.draw.rect(DISPLAY, self.thisPieceColor, rectInfo)