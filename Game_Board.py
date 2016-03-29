__author__ = 'mfmer'

import sys
import my_class_objects
import pygame
from pygame.locals import *

#Board is a 2d list that holds our warrior objects and is used by the class member funcitons
Board = [["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
         ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
         ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
         ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
         ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
         ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
         ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
         ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]]

#creates a pawn and places it in the Board
#white pawns
wPawn1 = my_class_objects.wPawn(0,1)
Board[0][1] = wPawn1
wPawn2 = my_class_objects.wPawn(1,1)
Board[1][1] = wPawn2
wPawn3 = my_class_objects.wPawn(2,1)
Board[2][1] = wPawn3
wPawn4 = my_class_objects.wPawn(3,1)
Board[3][1] = wPawn4
wPawn5 = my_class_objects.wPawn(4,1)
Board[4][1] = wPawn5
wPawn6 = my_class_objects.wPawn(5,1)
Board[5][1] = wPawn6
wPawn7 = my_class_objects.wPawn(6,1)
Board[6][1] = wPawn7
wPawn8 = my_class_objects.wPawn(7,1)
Board[7][1] = wPawn8
#white rooks
wRook1 = my_class_objects.wRook(0, 0)
Board[0][0] = wRook1
wRook2 = my_class_objects.wRook(7, 0)
Board[7][0] = wRook2
#white Knights
wKnight1 = my_class_objects.wKnight(1, 0)
Board[1][0] = wKnight1
wKnight2 = my_class_objects.wKnight(6, 0)
Board[6][0] = wKnight2
#white bishops
wBishop1 = my_class_objects.wBishop(2, 0)
Board[2][0] = wBishop1
wBishop2 = my_class_objects.wBishop(5, 0)
Board[5][0] = wBishop2
#white queen
wQueen1 = my_class_objects.wQueen(3, 0)
Board[3][0] = wQueen1
#white king
wKing1 = my_class_objects.wKing(4, 0)
Board[4][0] = wKing1

#red pieces
#red pawns
rPawn1 = my_class_objects.rPawn(0,6)
Board[0][6] = rPawn1
rPawn2 = my_class_objects.rPawn(1,6)
Board[1][6] = rPawn2
rPawn3 = my_class_objects.rPawn(2,6)
Board[2][6] = rPawn3
rPawn4 = my_class_objects.rPawn(3,6)
Board[3][6] = rPawn4
rPawn5 = my_class_objects.rPawn(4,6)
Board[4][6] = rPawn5
rPawn6 = my_class_objects.rPawn(5,6)
Board[5][6] = rPawn6
rPawn7 = my_class_objects.rPawn(6,6)
Board[6][6] = rPawn7
rPawn8 = my_class_objects.rPawn(7,6)
Board[7][6] = rPawn8
#red rooks
rRook1 = my_class_objects.rRook(0, 7)
Board[0][7] = rRook1
rRook2 = my_class_objects.rRook(7, 7)
Board[7][7] = rRook2
#red knights
rKnight1 = my_class_objects.rKnight(1, 7)
Board[1][7] = rKnight1
rKnight2 = my_class_objects.rKnight(6, 7)
Board[6][7] = rKnight2
#red Bishops
rBishop1 = my_class_objects.rBishop(2, 7)
Board[2][7] = rBishop1
rBishop2 = my_class_objects.rBishop(5, 7)
Board[5][7] = rBishop2
#red queen
rQueen1 = my_class_objects.rQueen(3, 7)
Board[3][7] = rQueen1
#red king
rKing1 = my_class_objects.rKing(4, 7)
Board[4][7] = rKing1

#here is a list of all wariros. This list we will loop through later to retrieve captured pieces for printing.
warriors = []
#add white pieces
warriors.append(wPawn1)
warriors.append(wPawn2)
warriors.append(wPawn3)
warriors.append(wPawn4)
warriors.append(wPawn5)
warriors.append(wPawn6)
warriors.append(wPawn7)
warriors.append(wPawn8)
warriors.append(wRook1)
warriors.append(wRook2)
warriors.append(wKnight1)
warriors.append(wKnight2)
warriors.append(wBishop1)
warriors.append(wBishop2)
warriors.append(wQueen1)
warriors.append(wKing1)
#add red pieces
warriors.append(rPawn1)
warriors.append(rPawn2)
warriors.append(rPawn3)
warriors.append(rPawn4)
warriors.append(rPawn5)
warriors.append(rPawn6)
warriors.append(rPawn7)
warriors.append(rPawn8)
warriors.append(rRook1)
warriors.append(rRook2)
warriors.append(rKnight1)
warriors.append(rKnight2)
warriors.append(rBishop1)
warriors.append(rBishop2)
warriors.append(rQueen1)
warriors.append(rKing1)

#this can be uncommented to show a full captured screen for red
#p3 = my_class_objects.rPawn(-1,-1)
#p4 = my_class_objects.rPawn(-1,-1)
#p5 = my_class_objects.rPawn(-1,-1)
#p6 = my_class_objects.rPawn(-1,-1)
#p7 = my_class_objects.rPawn(-1,-1)
#p8 = my_class_objects.rPawn(-1,-1)
#p8 = my_class_objects.rPawn(-1,-1)
#p9 = my_class_objects.rPawn(-1,-1)
#p10 = my_class_objects.rPawn(-1,-1)
#p11 = my_class_objects.rPawn(-1,-1)
#p12 = my_class_objects.rPawn(-1,-1)
#p13 = my_class_objects.rPawn(-1,-1)
#p14 = my_class_objects.rPawn(-1,-1)
#p15 = my_class_objects.rPawn(-1,-1)
#p16 = my_class_objects.rPawn(-1,-1)
#p17 = my_class_objects.rPawn(-1,-1)
#p18 = my_class_objects.rPawn(-1,-1)
#warriors.append(p3)
#warriors.append(p4)
#warriors.append(p5)
#warriors.append(p6)
#warriors.append(p7)
#warriors.append(p8)
#warriors.append(p9)
#warriors.append(p10)
#warriors.append(p11)
#warriors.append(p12)
#warriors.append(p13)
#warriors.append(p14)
#warriors.append(p15)
#warriors.append(p16)
#warriors.append(p17)
#warriors.append(p18)

#this can be uncommented to test for a full capture of white
#w1 = my_class_objects.wPawn(-1,-1)
#w2 = my_class_objects.wPawn(-1,-1)
#w3 = my_class_objects.wPawn(-1,-1)
#w4 = my_class_objects.wPawn(-1,-1)
#w5 = my_class_objects.wPawn(-1,-1)
#w6 = my_class_objects.wPawn(-1,-1)
#w7 = my_class_objects.wPawn(-1,-1)
#w8 = my_class_objects.wPawn(-1,-1)
#w9 = my_class_objects.wPawn(-1,-1)
#w10 = my_class_objects.wPawn(-1, -1)
#w11 = my_class_objects.wPawn(-1,-1)
#w12 = my_class_objects.wPawn(-1,-1)
#w13 = my_class_objects.wPawn(-1,-1)
#w14 = my_class_objects.wPawn(-1,-1)
#w15 = my_class_objects.wPawn(-1,-1)
#w16 = my_class_objects.wPawn(-1,-1)
#warriors.append(w1)
#warriors.append(w2)
#warriors.append(w3)
#warriors.append(w4)
#warriors.append(w5)
#warriors.append(w6)
#warriors.append(w7)
#warriors.append(w8)
#warriors.append(w9)
#warriors.append(w10)
#warriors.append(w11)
#warriors.append(w12)
#warriors.append(w13)
#warriors.append(w14)
#warriors.append(w15)
#warriors.append(w16)

#beginning of pygame
pygame.init()

#window initialization
screen = pygame.display.set_mode((640,450))
pygame.display.set_caption('Chess')

# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 15)

#bool for when something is clicked, might remove this in final code
clicked = False

#Loads white pawn image
wPawnImg = pygame.image.load('wPawn.png')
wPawnImg = pygame.transform.scale(wPawnImg, (50,50))
#Loads red pawn image
rPawnImg = pygame.image.load('rPawn.png')
rPawnImg = pygame.transform.scale(rPawnImg, (50, 50))
#loads white rook image
wRookImg = pygame.image.load('wRook.png')
wRookImg = pygame.transform.scale(wRookImg, (50, 50))
#loads red rook image
rRookImg = pygame.image.load('rRook.png')
rRookImg = pygame.transform.scale(rRookImg, (50, 50))
#loads white knight image
wKnightImg = pygame.image.load('wKnight.png')
wKnightImg = pygame.transform.scale(wKnightImg, (50,50))
#loads red knight image
rKnightImg = pygame.image.load('rKnight.png')
rKnightImg = pygame.transform.scale(rKnightImg, (50, 50))
#loads white bishop image
wBishopImg = pygame.image.load('wBishop.png')
wBishopImg = pygame.transform.scale(wBishopImg, (50, 50))
#loads red bishop image
rBishopImg = pygame.image.load('rBishop.png')
rBishopImg = pygame.transform.scale(rBishopImg, (50, 50))
#loads white queen image
wQueenImg = pygame.image.load('wQueen.png')
wQueenImg = pygame.transform.scale(wQueenImg, (50, 50))
#loads red queen image
rQueenImg = pygame.image.load('rQueen.png')
rQueenImg = pygame.transform.scale(rQueenImg, (50, 50))
#loads white king image
wKingImg = pygame.image.load('wKing.png')
wKingImg = pygame.transform.scale(wKingImg, (50, 50))
#loads red king image
rKingImg = pygame.image.load('rKing.png')
rKingImg = pygame.transform.scale(rKingImg, (50, 50))

#clickCount is a variable that determines a select or
clickCount = 0

#bools for players turn
whitePlayerTurn = True
redPlayerTurn = False

#loop for updating the window
while True:
    #handles the event of closing the window
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #handles the mouse click event
        if event.type == pygame.MOUSEBUTTONUP:
            #clicked and posClicked can be removed later, these are for testing purposes
            #clicked = True
            #collects position for output to the console
            posClicked = str(pygame.mouse.get_pos())
            #gets the coords of the mouse click to covert to numbers that the backend can use
            coordsToConvert = pygame.mouse.get_pos()

            if clickCount % 2 == 0:
                #handles first click of a person's turn (i.e. selecting a piece to move)
                initCoords = (int(coordsToConvert[0]/50), ((int(coordsToConvert[1]/50) - 7) * -1))
                #console output for test
                print "first click in box: ", initCoords

                #if a empty box is clicked
                if Board[initCoords[0]][initCoords[1]] == "empty":
                    #console output for test
                    print "This square is empty"

                #handles red player's turn
                elif redPlayerTurn:
                    if Board[initCoords[0]][initCoords[1]].color == "white":
                        #console output for testing
                        print "This piece does not belong to you"
                    else:
                        #console output for testing
                        print "This square contains a " + Board[initCoords[0]][initCoords[1]].reportRank()
                        #increments the count to move to the next step
                        clickCount = clickCount + 1

                #handles white player's turn
                elif whitePlayerTurn:
                    if Board[initCoords[0]][initCoords[1]].color == "red":
                        #console output for testing
                        print "this piece does not belong to you"
                    else:
                        #console output for testing
                        print "This square contains a " + Board[initCoords[0]][initCoords[1]].reportRank()
                        #increments the count to move to the next step
                        clickCount = clickCount + 1

            else:
                #handles second click of a person's turn (i.e. where the piece will move)
                moveCoords = (int(coordsToConvert[0]/50), ((int(coordsToConvert[1]/50) - 7) * -1))

                #console output for testing
                print "second click in box: ", moveCoords

                #stores true is the move was valid
                validMove = Board[initCoords[0]][initCoords[1]].move(moveCoords[0],moveCoords[1], Board)

                #switches turn if a valid move was preformed
                if validMove:
                    if redPlayerTurn:
                        redPlayerTurn = False
                        whitePlayerTurn = True
                    elif whitePlayerTurn:
                        redPlayerTurn = True
                        whitePlayerTurn = False

                #if not a valid move, current player is set back to step one
                else:
                    print "try again"

                #increments the count to return to step one
                clickCount = clickCount + 1

    #initial filling of the screen, required so images dont double print
    screen.fill((255, 255, 255))

    #following code draws red and white squares of the chess board
    count = 0
    for row in xrange(0, 400, 50):
        count = count + 1
        for col in xrange(0, 400, 50):
            if count % 2 == 0:
                pygame.draw.rect(screen, (255, 255, 255), (col, row, 50, 50))
            else:
                pygame.draw.rect(screen, (175, 7, 7), (col, row, 50, 50))
            count = count + 1

    #draws the outside boarder of the chess board
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 400, 400), 1)

    #draw a green square when you select a piece
    if clickCount % 2 != 0:
        pygame.draw.rect(screen, (0, 255, 128), (initCoords[0] * 50, 350 - (initCoords[1] * 50), 50, 50))

    #this code was for testing
    #keeps a current location of mouse, this can be removed for the final game
    #label = myfont.render(str(pygame.mouse.get_pos()), 1, (0, 0,0))
    #screen.blit(label, (500, 100))

    #this code is for testing purposes only
    #this keeps a current location of which square you are currently in
    #mouseCoords = pygame.mouse.get_pos()
    #xSquare = int(mouseCoords[0]/50)
    #ySquare = (int(mouseCoords[1]/50) - 7) * (-1)
    #label2 = myfont.render(str(xSquare) + " " + str(ySquare),1, (0, 0, 0))
    #screen.blit(label2, (500, 120))

    #this was code for testing
    #this checks if a mouse click has been detected and prints the location of the mouse at the time of the click
    #if clicked:
    #    label3 = myfont.render("Mouse clicked at " + posClicked, 1, (0,0,0))
    #    screen.blit(label3, (400, 140))

    #prints the chess board
    for x in range(0, 8):
        for y in range(0, 8):
            if Board[x][y] != "empty":
                #draws white pawn
                if Board[x][y].value == "wpawn":
                    screen.blit(wPawnImg, (x * 50, 350 - (y * 50)))
                #draws red pwn
                if Board[x][y].value == "rpawn":
                    screen.blit(rPawnImg, (x * 50, 350 - (y * 50)))
                #draws white rook
                if Board[x][y].value == "wrook":
                    screen.blit(wRookImg, (x * 50, 350 - (y * 50)))
                #draws red rook
                if Board[x][y].value == "rrook":
                    screen.blit(rRookImg, (x * 50, 350 - (y * 50)))
                #draws white knight
                if Board[x][y].value == "wknight":
                    screen.blit(wKnightImg, (x * 50, 350 - (y * 50)))
                #draws red knight
                if Board[x][y].value == "rknight":
                    screen.blit(rKnightImg, (x * 50, 350 - (y * 50)))
                #draws white bishop
                if Board[x][y].value == "wbishop":
                    screen.blit(wBishopImg, (x * 50, 350 - (y * 50)))
                #draws red bishop
                if Board[x][y].value == "rbishop":
                    screen.blit(rBishopImg, (x * 50, 350 - (y * 50)))
                #draws white queen
                if Board[x][y].value == "wqueen":
                    screen.blit(wQueenImg, (x * 50, 350 - (y * 50)))
                #draws red queen
                if Board[x][y].value == "rqueen":
                    screen.blit(rQueenImg, (x * 50, 350 - (y * 50)))
                #draws white king
                if Board[x][y].value == "wking":
                    screen.blit(wKingImg, (x * 50, 350 - (y * 50)))
                #draws red king
                if Board[x][y].value == "rking":
                    screen.blit(rKingImg, (x * 50, 350 - (y * 50)))


    #check for win conditions
    redWins = False
    if (wKing1.xCoord == -1) and (wKing1.yCoord == -1):
        winLabel = myfont.render("Red player wins!", 1, (175, 7, 7))
        screen.blit(winLabel, (100, 425))
        redWins = True

    #check for win conditions
    whiteWins = False
    if (rKing1.xCoord == -1) and (rKing1.yCoord == -1):
        winLabel = myfont.render("White player wins!", 1, (145, 145, 145))
        screen.blit(winLabel, (100, 425))
        whiteWins = True

    #prints which player's turn it is
    if redPlayerTurn:
        currentTurnName = "Red"
    else:
        currentTurnName = "White"
    if (redWins == False) and (whiteWins == False):
        label4 = myfont.render(currentTurnName + " player's turn" , 1, (0, 0, 0))
        screen.blit(label4, (100, 425))

    #prints capture label for red
    capturedLabel = myfont.render("Red's Captured pieces: ", 1, (175, 7, 7))
    screen.blit(capturedLabel, (410, 10))

    #prints capture label for white
    capturedLabel2 = myfont.render("White's Captured pieces: ", 1, (145, 145, 145))
    screen.blit(capturedLabel2, (410, 230))

    #counter for each red capturee
    rCapCount = 0
    #counter for each white capturee
    wCapCount = 0

    #looks through warriors for captured units
    for i in xrange(0, len(warriors)):
        #first finds a warrior thats coords are -1, -1. This only happens once kill has been called for that object
        if (warriors[i].xCoord == -1) and (warriors[i].yCoord == -1):
            #case for capture white pawns
            if warriors[i].color == "white" and warriors[i].value == "wpawn":
                #print image at location determind by counter
                if wCapCount < 4:
                    screen.blit(wPawnImg, (410 + (wCapCount * 50), 240))
                if (wCapCount < 8) and (wCapCount > 3):
                    screen.blit(wPawnImg, (410 + ((wCapCount - 4) * 50), 290))
                if (wCapCount < 12) and (wCapCount > 7):
                    screen.blit(wPawnImg, (410 + ((wCapCount - 8) * 50), 340))
                if (wCapCount < 16) and (wCapCount > 11):
                    screen.blit(wPawnImg, (410 + ((wCapCount - 12) * 50), 390))
                wCapCount = wCapCount + 1
            #case for captured red pawns
            if warriors[i].color == "red" and warriors[i].value == "rpawn":
                #print image at location determind by counter
                if rCapCount < 4:
                    screen.blit(rPawnImg, (410 + (rCapCount * 50), 20))
                if (rCapCount < 8) and (rCapCount > 3):
                    screen.blit(rPawnImg, (410 + ((rCapCount - 4) * 50), 70))
                if (rCapCount < 12) and (rCapCount > 7):
                    screen.blit(rPawnImg, (410 + ((rCapCount - 8) * 50), 120))
                if (rCapCount < 16) and (rCapCount > 11):
                    screen.blit(rPawnImg, (410 + ((rCapCount - 12) * 50), 170))
                rCapCount = rCapCount + 1
            #case for capture white rooks
            if warriors[i].color == "white" and warriors[i].value == "wrook":
                #print image at location determind by counter
                if wCapCount < 4:
                    screen.blit(wRookImg, (410 + (wCapCount * 50), 240))
                if (wCapCount < 8) and (wCapCount > 3):
                    screen.blit(wRookImg, (410 + ((wCapCount - 4) * 50), 290))
                if (wCapCount < 12) and (wCapCount > 7):
                    screen.blit(wRookImg, (410 + ((wCapCount - 8) * 50), 340))
                if (wCapCount < 16) and (wCapCount > 11):
                    screen.blit(wRookImg, (410 + ((wCapCount - 12) * 50), 390))
                wCapCount = wCapCount + 1
            #case for captured red rooks
            if warriors[i].color == "red" and warriors[i].value == "rrook":
                #print image at location determind by counter
                if rCapCount < 4:
                    screen.blit(rRookImg, (410 + (rCapCount * 50), 20))
                if (rCapCount < 8) and (rCapCount > 3):
                    screen.blit(rRookImg, (410 + ((rCapCount - 4) * 50), 70))
                if (rCapCount < 12) and (rCapCount > 7):
                    screen.blit(rRookImg, (410 + ((rCapCount - 8) * 50), 120))
                if (rCapCount < 16) and (rCapCount > 11):
                    screen.blit(rRookImg, (410 + ((rCapCount - 12) * 50), 170))
                rCapCount = rCapCount + 1
            #case for capture white knights
            if warriors[i].color == "white" and warriors[i].value == "wknight":
                #print image at location determind by counter
                if wCapCount < 4:
                    screen.blit(wKnightImg, (410 + (wCapCount * 50), 240))
                if (wCapCount < 8) and (wCapCount > 3):
                    screen.blit(wKnightImg, (410 + ((wCapCount - 4) * 50), 290))
                if (wCapCount < 12) and (wCapCount > 7):
                    screen.blit(wKnightImg, (410 + ((wCapCount - 8) * 50), 340))
                if (wCapCount < 16) and (wCapCount > 11):
                    screen.blit(wKnightImg, (410 + ((wCapCount - 12) * 50), 390))
                wCapCount = wCapCount + 1
            #case for captured red knight
            if warriors[i].color == "red" and warriors[i].value == "rknight":
                #print image at location determind by counter
                if rCapCount < 4:
                    screen.blit(rKnightImg, (410 + (rCapCount * 50), 20))
                if (rCapCount < 8) and (rCapCount > 3):
                    screen.blit(rKnightImg, (410 + ((rCapCount - 4) * 50), 70))
                if (rCapCount < 12) and (rCapCount > 7):
                    screen.blit(rKnightImg, (410 + ((rCapCount - 8) * 50), 120))
                if (rCapCount < 16) and (rCapCount > 11):
                    screen.blit(rKnightImg, (410 + ((rCapCount - 12) * 50), 170))
                rCapCount = rCapCount + 1
            #case for capture white bishop
            if warriors[i].color == "white" and warriors[i].value == "wbishop":
                #print image at location determind by counter
                if wCapCount < 4:
                    screen.blit(wBishopImg, (410 + (wCapCount * 50), 240))
                if (wCapCount < 8) and (wCapCount > 3):
                    screen.blit(wBishopImg, (410 + ((wCapCount - 4) * 50), 290))
                if (wCapCount < 12) and (wCapCount > 7):
                    screen.blit(wBishopImg, (410 + ((wCapCount - 8) * 50), 340))
                if (wCapCount < 16) and (wCapCount > 11):
                    screen.blit(wBishopImg, (410 + ((wCapCount - 12) * 50), 390))
                wCapCount = wCapCount + 1
            #case for captured red bishop
            if warriors[i].color == "red" and warriors[i].value == "rbishop":
                #print image at location determind by counter
                if rCapCount < 4:
                    screen.blit(rBishopImg, (410 + (rCapCount * 50), 20))
                if (rCapCount < 8) and (rCapCount > 3):
                    screen.blit(rBishopImg, (410 + ((rCapCount - 4) * 50), 70))
                if (rCapCount < 12) and (rCapCount > 7):
                    screen.blit(rBishopImg, (410 + ((rCapCount - 8) * 50), 120))
                if (rCapCount < 16) and (rCapCount > 11):
                    screen.blit(rBishopImg, (410 + ((rCapCount - 12) * 50), 170))
                rCapCount = rCapCount + 1
            #case for capture white queen
            if warriors[i].color == "white" and warriors[i].value == "wqueen":
                #print image at location determind by counter
                if wCapCount < 4:
                    screen.blit(wQueenImg, (410 + (wCapCount * 50), 240))
                if (wCapCount < 8) and (wCapCount > 3):
                    screen.blit(wQueenImg, (410 + ((wCapCount - 4) * 50), 290))
                if (wCapCount < 12) and (wCapCount > 7):
                    screen.blit(wQueenImg, (410 + ((wCapCount - 8) * 50), 340))
                if (wCapCount < 16) and (wCapCount > 11):
                    screen.blit(wQueenImg, (410 + ((wCapCount - 12) * 50), 390))
                wCapCount = wCapCount + 1
            #case for captured red queen
            if warriors[i].color == "red" and warriors[i].value == "rqueen":
                #print image at location determind by counter
                if rCapCount < 4:
                    screen.blit(rQueenImg, (410 + (rCapCount * 50), 20))
                if (rCapCount < 8) and (rCapCount > 3):
                    screen.blit(rQueenImg, (410 + ((rCapCount - 4) * 50), 70))
                if (rCapCount < 12) and (rCapCount > 7):
                    screen.blit(rQueenImg, (410 + ((rCapCount - 8) * 50), 120))
                if (rCapCount < 16) and (rCapCount > 11):
                    screen.blit(rQueenImg, (410 + ((rCapCount - 12) * 50), 170))
                rCapCount = rCapCount + 1
            #case for capture white king
            if warriors[i].color == "white" and warriors[i].value == "wking":
                #print image at location determind by counter
                if wCapCount < 4:
                    screen.blit(wKingImg, (410 + (wCapCount * 50), 240))
                if (wCapCount < 8) and (wCapCount > 3):
                    screen.blit(wKingImg, (410 + ((wCapCount - 4) * 50), 290))
                if (wCapCount < 12) and (wCapCount > 7):
                    screen.blit(wKingImg, (410 + ((wCapCount - 8) * 50), 340))
                if (wCapCount < 16) and (wCapCount > 11):
                    screen.blit(wKingImg, (410 + ((wCapCount - 12) * 50), 390))
                wCapCount = wCapCount + 1
            #case for captured red king
            if warriors[i].color == "red" and warriors[i].value == "rking":
                #print image at location determind by counter
                if rCapCount < 4:
                    screen.blit(rKingImg, (410 + (rCapCount * 50), 20))
                if (rCapCount < 8) and (rCapCount > 3):
                    screen.blit(rKingImg, (410 + ((rCapCount - 4) * 50), 70))
                if (rCapCount < 12) and (rCapCount > 7):
                    screen.blit(rKingImg, (410 + ((rCapCount - 8) * 50), 120))
                if (rCapCount < 16) and (rCapCount > 11):
                    screen.blit(rKingImg, (410 + ((rCapCount - 12) * 50), 170))
                rCapCount = rCapCount + 1

    #gameupdate
    pygame.display.update()

#function for printing the board in the console
def printBoard():
    for y in range(7, -1, -1):
        for x in xrange(0,8):
            if Board[x][y] == "empty":
                print Board[x][y],
            else:
                print Board[x][y].reportRank(),
        print "\n"










