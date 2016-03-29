__author__ = 'mfmer'

#----------PAWNS----------#

class wPawn:

    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y
        self.color = "white"
        self.value = "wpawn"
        self.firstmove = True

    def checkForEnemy(self, x, y, z):
        if z[x][y] != "empty":
            if z[x][y].color == "red":
                return True
        else:
            return False

    def kill(self):
        self.xCoord = -1
        self.yCoord = -1

    def move(self, x, y, z):
        #move up
        if (x == self.xCoord) and (y == self.yCoord + 1) and (z[x][y] == "empty"):
            self.yCoord = y
            z[x][y] = self
            z[x][y-1] = "empty"
            self.firstmove = False
            return True
        #attack up left
        elif (x == self.xCoord - 1) and (y == self.yCoord + 1) and (self.checkForEnemy(x, y, z)):
            self.yCoord = y
            self.xCoord = x
            z[x][y].kill()
            z[x][y] = self
            z[x+1][y-1] = "empty"
            self.firstmove = False
            return True
        #attack up right
        elif (x == self.xCoord + 1) and (y == self.yCoord + 1) and (self.checkForEnemy(x, y, z)):
            self.yCoord = y
            self.xCoord = x
            z[x][y].kill()
            z[x][y] = self
            z[x-1][y-1] = "empty"
            self.firstmove = False
            return True
        #move up two if first move
        elif (self.firstmove) and (x == self.xCoord) and (y == self.yCoord + 2) and (z[x][y] == "empty") :
            z[self.xCoord][self.yCoord] = "empty"
            z[x][y] = self
            self.xCoord = x
            self.yCoord = y
            self.firstmove = False
            return True
        else:
            print("This is not a valid move")
            return False

    def reportRank(self):
        return "white pawn"

class rPawn:

    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y
        self.color = "red"
        self.value = "rpawn"
        self.firstmove = True

    def checkForEnemy(self, x, y, z):
        if z[x][y] != "empty":
            if z[x][y].color == "white":
                return True
        else:
            return False

    def kill(self):
        self.xCoord = -1
        self.yCoord = -1

    #move down(red player forward)
    def move(self, x, y, z):
        if (x == self.xCoord) and (y == self.yCoord - 1) and (z[x][y] == "empty"):
            self.yCoord = y
            z[x][y] = self
            z[x][y+1] = "empty"
            self.firstmove = False
            return True
        #move down left
        elif (x == self.xCoord - 1) and (y == self.yCoord - 1) and (self.checkForEnemy(x, y, z)):
            self.yCoord = y
            self.xCoord = x
            z[x][y].kill()
            z[x][y] = self
            z[x+1][y+1] = "empty"
            self.firstmove = False
            return True
        #move down right
        elif (x == self.xCoord + 1) and (y == self.yCoord - 1) and (self.checkForEnemy(x, y, z)):
            self.yCoord = y
            self.xCoord = x
            z[x][y].kill()
            z[x][y] = self
            z[x-1][y+1] = "empty"
            self.firstmove = False
            return True
        #move down two if first move
        elif (self.firstmove) and (x == self.xCoord) and (y == self.yCoord - 2) and (z[x][y] == "empty") :
            z[self.xCoord][self.yCoord] = "empty"
            z[x][y] = self
            self.xCoord = x
            self.yCoord = y
            self.firstmove = False
            return True
        else:
            print("This is not a valid move")
            return False

    def reportRank(self):
        return "red pawn"

#----------ROOKS----------#

class wRook:

    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y
        self.color = "white"
        self.value = "wrook"

    def checkForEnemy(self, x, y, z):
        if z[x][y] != "empty":
            if z[x][y].color == "red":
                return True
        else:
            return False

    def kill(self):
        self.xCoord = -1
        self.yCoord = -1

    def move(self, x, y, z):
        if (x == self.xCoord) and (y != self.yCoord) and (y > -1 and y < 8) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checeks for pieces between rook and final position
            dy = y - self.yCoord
            #move is upwards
            if dy > 1:
                for space in xrange(1, dy):
                    if z[self.xCoord][self.yCoord + space] != "empty":
                        print "Rook cannot move over pieces"
                        return False
            #move is downwards
            if dy < -1:
                for space in xrange(-1, dy, -1):
                    if z[self.xCoord][self.yCoord + space] != "empty":
                        print "Rook cannot move over pieces"
                        return False
            #checks for enemy and calls kill if found
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets previous space to empty
            z[self.xCoord][self.yCoord] = "empty"
            #updates location
            self.yCoord = y
            #place piece on new location in board
            z[x][y] = self
            return True
        elif (x != self.xCoord) and (x < 8 and x > -1) and (y == self.yCoord) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checeks for pieces between rook and final position
            dx = x - self.xCoord
            #move is right
            if dx > 1:
                for space in xrange(1, dx):
                    if z[self.xCoord + space][self.yCoord] != "empty":
                        print "Rook cannot move over pieces"
                        return False
            #move is left
            if dx < (-1):
                for space in xrange(-1, dx, -1):
                    if z[self.xCoord + space][self.yCoord] != "empty":
                        print "Rook cannot move over pieces"
                        return False
            #if enemy exists, calls kill
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #set previous location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #sets new location
            self.xCoord = x
            #sets piece in new location on board
            z[x][y] = self
            return True
        else:
            print("This is not a valid move")
            return False

    def reportRank(self):
        return "white rook"

class rRook:

    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y
        self.color = "red"
        self.value = "rrook"

    def checkForEnemy(self, x, y, z):
        if z[x][y] != "empty":
            if z[x][y].color == "white":
                return True
        else:
            return False

    def kill(self):
        self.xCoord = -1
        self.yCoord = -1

    def move(self, x, y, z):
        if (x == self.xCoord) and (y != self.yCoord) and (y > -1 and y < 8) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checeks for pieces between rook and final position
            dy = y - self.yCoord
            #move is upwards
            if dy > 1:
                for space in xrange(1, dy):
                    if z[self.xCoord][self.yCoord + space] != "empty":
                        print "Rook cannot move over pieces"
                        return False
            #move is downwards
            if dy < -1:
                for space in xrange(-1, dy, -1):
                    if z[self.xCoord][self.yCoord + space] != "empty":
                        print "Rook cannot move over pieces"
                        return False
            #checks for enemy and calls kill if found
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets previous space to empty
            z[self.xCoord][self.yCoord] = "empty"
            #updates location
            self.yCoord = y
            #place piece on new location in board
            z[x][y] = self
            return True
        elif (x != self.xCoord) and (x < 8 and x > -1) and (y == self.yCoord) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checeks for pieces between rook and final position
            dx = x - self.xCoord
            #move is right
            if dx > 1:
                for space in xrange(1, dx):
                    if z[self.xCoord + space][self.yCoord] != "empty":
                        print "Rook cannot move over pieces"
                        return False
            #move is left
            if dx < -1:
                for space in xrange(-1, dx, -1):
                    if z[self.xCoord + space][self.yCoord] != "empty":
                        print "Rook cannot move over pieces"
                        return False
            #if enemy exists, calls kill
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #set previous location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #sets new location
            self.xCoord = x
            #sets piece in new location on board
            z[x][y] = self
            return True
        else:
            print("This is not a valid move")
            return False

    def reportRank(self):
        return "red rook"

#----------Knights----------#

class wKnight:

    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y
        self.color = "white"
        self.value = "wknight"

    def checkForEnemy(self, x, y, z):
        if z[x][y] != "empty":
            if z[x][y].color == "red":
                return True
        else:
            return False

    def kill(self):
        self.xCoord = -1
        self.yCoord = -1

    def move(self, x, y, z):
        if (x == self.xCoord + 1) and (y == self.yCoord + 2) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks for enemy
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets old location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #places in new location
            z[x][y] = self
            #update self
            self.xCoord = x
            self.yCoord = y
            return True
        elif (x == self.xCoord + 2) and (y == self.yCoord + 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks for enemy
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets old location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #places in new location
            z[x][y] = self
            #update self
            self.xCoord = x
            self.yCoord = y
            return True
        elif (x == self.xCoord + 2) and (y == self.yCoord - 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks for enemy
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets old location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #places in new location
            z[x][y] = self
            #update self
            self.xCoord = x
            self.yCoord = y
            return True
        elif (x == self.xCoord + 1) and (y == self.yCoord - 2) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks for enemy
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets old location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #places in new location
            z[x][y] = self
            #update self
            self.xCoord = x
            self.yCoord = y
            return True
        elif (x == self.xCoord - 1) and (y == self.yCoord - 2) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks for enemy
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets old location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #places in new location
            z[x][y] = self
            #update self
            self.xCoord = x
            self.yCoord = y
            return True
        elif (x == self.xCoord - 2) and (y == self.yCoord - 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks for enemy
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets old location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #places in new location
            z[x][y] = self
            #update self
            self.xCoord = x
            self.yCoord = y
            return True
        elif (x == self.xCoord - 2) and (y == self.yCoord + 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks for enemy
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets old location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #places in new location
            z[x][y] = self
            #update self
            self.xCoord = x
            self.yCoord = y
            return True
        elif (x == self.xCoord - 1) and (y == self.yCoord + 2) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks for enemy
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets old location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #places in new location
            z[x][y] = self
            #update self
            self.xCoord = x
            self.yCoord = y
            return True
        else:
            print("This is not a valid move")
            return False

    def reportRank(self):
        return "white knight"

class rKnight:

    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y
        self.color = "red"
        self.value = "rknight"

    def checkForEnemy(self, x, y, z):
        if z[x][y] != "empty":
            if z[x][y].color == "white":
                return True
        else:
            return False

    def kill(self):
        self.xCoord = -1
        self.yCoord = -1

    def move(self, x, y, z):
        if (x == self.xCoord + 1) and (y == self.yCoord + 2) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks for enemy
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets old location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #places in new location
            z[x][y] = self
            #update self
            self.xCoord = x
            self.yCoord = y
            return True
        elif (x == self.xCoord + 2) and (y == self.yCoord + 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks for enemy
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets old location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #places in new location
            z[x][y] = self
            #update self
            self.xCoord = x
            self.yCoord = y
            return True
        elif (x == self.xCoord + 2) and (y == self.yCoord - 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks for enemy
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets old location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #places in new location
            z[x][y] = self
            #update self
            self.xCoord = x
            self.yCoord = y
            return True
        elif (x == self.xCoord + 1) and (y == self.yCoord - 2) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks for enemy
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets old location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #places in new location
            z[x][y] = self
            #update self
            self.xCoord = x
            self.yCoord = y
            return True
        elif (x == self.xCoord - 1) and (y == self.yCoord - 2) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks for enemy
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets old location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #places in new location
            z[x][y] = self
            #update self
            self.xCoord = x
            self.yCoord = y
            return True
        elif (x == self.xCoord - 2) and (y == self.yCoord - 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks for enemy
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets old location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #places in new location
            z[x][y] = self
            #update self
            self.xCoord = x
            self.yCoord = y
            return True
        elif (x == self.xCoord - 2) and (y == self.yCoord + 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks for enemy
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets old location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #places in new location
            z[x][y] = self
            #update self
            self.xCoord = x
            self.yCoord = y
            return True
        elif (x == self.xCoord - 1) and (y == self.yCoord + 2) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks for enemy
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets old location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #places in new location
            z[x][y] = self
            #update self
            self.xCoord = x
            self.yCoord = y
            return True
        else:
            print("This is not a valid move")
            return False

    def reportRank(self):
        return "red knight"

#----------Bishops----------#

class wBishop:

    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y
        self.color = "white"
        self.value = "wbishop"

    def checkForEnemy(self, x, y, z):
        if z[x][y] != "empty":
            if z[x][y].color == "red":
                return True
        else:
            return False

    def kill(self):
        self.xCoord = -1
        self.yCoord = -1

    def move(self, x, y, z):
        dx = x - self.xCoord
        dy = y - self.yCoord
        if (x != self.xCoord and y != self.yCoord) and (abs(dx) == abs(dy)) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks direction and for pieces between
            #up right
            if (dx > 1) and (dy > 1):
                for space in xrange(1, dx):
                    if z[self.xCoord + space][self.yCoord + space] != "empty":
                        print "Bishop cannot move over pieces"
                        return False
            #up left
            if (dx < (-1)) and (dy > 1):
                for space in xrange(1, dy):
                    if z[self.xCoord - space][self.yCoord + space] != "empty":
                        print "Bishop cannot move over pieces"
                        return False
            #down right
            if (dx > 1) and (dy < (-1)):
                for space in xrange (1, dx):
                    if z[self.xCoord + space][self.yCoord - space] != "empty":
                        print "Bishop cannot move over pieces"
                        return False
            #down left
            if (dx < (-1)) and (dy < (-1)):
                for space in xrange(-1, dx, -1):
                    if z[self.xCoord + space][self.yCoord + space] != "empty":
                        print "Bishop cannot move over pieces"
                        return False
            #set old loaction to empty
            z[self.xCoord][self.yCoord] = "empty"
            #deals with enemy if found
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets piece at location
            z[x][y] = self
            #updates self
            self.xCoord = x
            self.yCoord = y
            return True
        else:
            print("This is not a valid move")
            return False

    def reportRank(self):
        return "white bishop"

class rBishop:

    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y
        self.color = "red"
        self.value = "rbishop"

    def checkForEnemy(self, x, y, z):
        if z[x][y] != "empty":
            if z[x][y].color == "white":
                return True
        else:
            return False

    def kill(self):
        self.xCoord = -1
        self.yCoord = -1

    def move(self, x, y, z):
        dx = x - self.xCoord
        dy = y - self.yCoord
        if (x != self.xCoord and y != self.yCoord) and (abs(dx) == abs(dy)) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks direction and for pieces between
            #up right
            if (dx > 1) and (dy > 1):
                for space in xrange(1, dx):
                    if z[self.xCoord + space][self.yCoord + space] != "empty":
                        print "Bishop cannot move over pieces"
                        return False
            #up left
            if (dx < (-1)) and (dy > 1):
                for space in xrange(1, dy):
                    if z[self.xCoord - space][self.yCoord + space] != "empty":
                        print "Bishop cannot move over pieces"
                        return False
            #down right
            if (dx > 1) and (dy < (-1)):
                for space in xrange (1, dx):
                    if z[self.xCoord + space][self.yCoord - space] != "empty":
                        print "Bishop cannot move over pieces"
                        return False
            #down left
            if (dx < (-1)) and (dy < (-1)):
                for space in xrange(-1, dx, -1):
                    if z[self.xCoord + space][self.yCoord + space] != "empty":
                        print "Bishop cannot move over pieces"
                        return False
            #set old loaction to empty
            z[self.xCoord][self.yCoord] = "empty"
            #deals with enemy if found
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets piece at location
            z[x][y] = self
            #updates self
            self.xCoord = x
            self.yCoord = y
            return True
        else:
            print("This is not a valid move")
            return False

    def reportRank(self):
        return "red bishop"

#----------Queens----------#

class wQueen:

    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y
        self.color = "white"
        self.value = "wqueen"

    def checkForEnemy(self, x, y, z):
        if z[x][y] != "empty":
            if z[x][y].color == "red":
                return True
        else:
            return False

    def kill(self):
        self.xCoord = -1
        self.yCoord = -1

    def move(self, x, y, z):
        #diagnoal moves
        dx = x - self.xCoord
        dy = y - self.yCoord
        if (x != self.xCoord and y != self.yCoord) and (abs(dx) == abs(dy)) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks direction and for pieces between
            #up right
            if (dx > 1) and (dy > 1):
                for space in xrange(1, dx):
                    if z[self.xCoord + space][self.yCoord + space] != "empty":
                        print "Queen cannot move over pieces"
                        return False
            #up left
            if (dx < (-1)) and (dy > 1):
                for space in xrange(1, dy):
                    if z[self.xCoord - space][self.yCoord + space] != "empty":
                        print "Queen cannot move over pieces"
                        return False
            #down right
            if (dx > 1) and (dy < (-1)):
                for space in xrange (1, dx):
                    if z[self.xCoord + space][self.yCoord - space] != "empty":
                        print "Queen cannot move over pieces"
                        return False
            #down left
            if (dx < (-1)) and (dy < (-1)):
                for space in xrange(-1, dx, -1):
                    if z[self.xCoord + space][self.yCoord + space] != "empty":
                        print "Queen cannot move over pieces"
                        return False
            #set old loaction to empty
            z[self.xCoord][self.yCoord] = "empty"
            #deals with enemy if found
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets piece at location
            z[x][y] = self
            #updates self
            self.xCoord = x
            self.yCoord = y
            return True
        #horizontal/vertical movements
        elif (x == self.xCoord) and (y != self.yCoord) and (y > -1 and y < 8) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #move is upwards
            if dy > 1:
                for space in xrange(1, dy):
                    if z[self.xCoord][self.yCoord + space] != "empty":
                        print "Queen cannot move over pieces"
                        return False
            #move is downwards
            if dy < -1:
                for space in xrange(-1, dy, -1):
                    if z[self.xCoord][self.yCoord + space] != "empty":
                        print "Queen cannot move over pieces"
                        return False
            #checks for enemy and calls kill if found
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets previous space to empty
            z[self.xCoord][self.yCoord] = "empty"
            #updates location
            self.yCoord = y
            #place piece on new location in board
            z[x][y] = self
            return True
        elif (x != self.xCoord) and (x < 8 and x > -1) and (y == self.yCoord) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #move is right
            if dx > 1:
                for space in xrange(1, dx):
                    if z[self.xCoord + space][self.yCoord] != "empty":
                        print "Queen cannot move over pieces"
                        return False
            #move is left
            if dx < - 1:
                for space in xrange(-1, dx, -1):
                    if z[self.xCoord + space][self.yCoord] != "empty":
                        print "Queen cannot move over pieces"
                        return False
            #if enemy exists, calls kill
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #set previous location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #sets new location
            self.xCoord = x
            #sets piece in new location on board
            z[x][y] = self
            return True
        else:
            print("This is not a valid move")
            return False

    def reportRank(self):
        return "white queen"

class rQueen:

    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y
        self.color = "red"
        self.value = "rqueen"

    def checkForEnemy(self, x, y, z):
        if z[x][y] != "empty":
            if z[x][y].color == "white":
                return True
        else:
            return False

    def kill(self):
        self.xCoord = -1
        self.yCoord = -1

    def move(self, x, y, z):
        #diagnoal moves
        dx = x - self.xCoord
        dy = y - self.yCoord
        if (x != self.xCoord and y != self.yCoord) and (abs(dx) == abs(dy)) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #checks direction and for pieces between
            #up right
            if (dx > 1) and (dy > 1):
                for space in xrange(1, dx):
                    if z[self.xCoord + space][self.yCoord + space] != "empty":
                        print "Queen cannot move over pieces"
                        return False
            #up left
            if (dx < (-1)) and (dy > 1):
                for space in xrange(1, dy):
                    if z[self.xCoord - space][self.yCoord + space] != "empty":
                        print "Queen cannot move over pieces"
                        return False
            #down right
            if (dx > 1) and (dy < (-1)):
                for space in xrange (1, dx):
                    if z[self.xCoord + space][self.yCoord - space] != "empty":
                        print "Queen cannot move over pieces"
                        return False
            #down left
            if (dx < (-1)) and (dy < (-1)):
                for space in xrange(-1, dx, -1):
                    if z[self.xCoord + space][self.yCoord + space] != "empty":
                        print "Queen cannot move over pieces"
                        return False
            #set old loaction to empty
            z[self.xCoord][self.yCoord] = "empty"
            #deals with enemy if found
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets piece at location
            z[x][y] = self
            #updates self
            self.xCoord = x
            self.yCoord = y
            return True
        #horizontal/vertical movements
        elif (x == self.xCoord) and (y != self.yCoord) and (y > -1 and y < 8) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #move is upwards
            if dy > 1:
                for space in xrange(1, dy):
                    if z[self.xCoord][self.yCoord + space] != "empty":
                        print "Queen cannot move over pieces"
                        return False
            #move is downwards
            if dy < -1:
                for space in xrange(-1, dy, -1):
                    if z[self.xCoord][self.yCoord + space] != "empty":
                        print "Queen cannot move over pieces"
                        return False
            #checks for enemy and calls kill if found
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets previous space to empty
            z[self.xCoord][self.yCoord] = "empty"
            #updates location
            self.yCoord = y
            #place piece on new location in board
            z[x][y] = self
            return True
        elif (x != self.xCoord) and (x < 8 and x > -1) and (y == self.yCoord) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #move is right
            if dx > 1:
                for space in xrange(1, dx):
                    if z[self.xCoord + space][self.yCoord] != "empty":
                        print "Queen cannot move over pieces"
                        return False
            #move is left
            if dx < - 1:
                for space in xrange(-1, dx, -1):
                    if z[self.xCoord + space][self.yCoord] != "empty":
                        print "Queen cannot move over pieces"
                        return False
            #if enemy exists, calls kill
            if(self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #set previous location to empty
            z[self.xCoord][self.yCoord] = "empty"
            #sets new location
            self.xCoord = x
            #sets piece in new location on board
            z[x][y] = self
            return True
        else:
            print("This is not a valid move")
            return False

    def reportRank(self):
        return "red queen"

#----------Kings----------#

class wKing:

    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y
        self.color = "white"
        self.value = "wking"

    def checkForEnemy(self, x, y, z):
        if z[x][y] != "empty":
            if z[x][y].color == "red":
                return True
        else:
            return False

    def kill(self):
        self.xCoord = -1
        self.yCoord = -1

    def move(self, x, y, z):
        #Kings cannot capture kings
        if z[x][y] != "empty":
            if z[x][y].value == "rking":
                print "Kings cannot capture kings"
                return False
        #move up
        if (x == self.xCoord) and (y == self.yCoord + 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            self.yCoord = y
            z[x][y] = self
            z[x][y-1] = "empty"
            return True
        #move up left
        elif (x == self.xCoord - 1) and (y == self.yCoord + 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            self.yCoord = y
            self.xCoord = x
            z[x][y] = self
            z[x+1][y-1] = "empty"
            return True
        #move up right
        elif (x == self.xCoord + 1) and (y == self.yCoord + 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            self.yCoord = y
            self.xCoord = x
            z[x][y] = self
            z[x-1][y-1] = "empty"
            return True
        #move right
        elif (x == self.xCoord + 1) and (y == self.yCoord) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #deals with enemy
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets previous postion to empty
            z[self.xCoord][self.yCoord] = "empty"
            #sets piece in new position
            z[x][y] = self
            #updates self
            self.xCoord = x
            self.yCoord = y
            return True
        #move left
        elif (x == self.xCoord - 1) and (y == self.yCoord) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #deals with enemy
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #empty previous postion
            z[self.xCoord][self.yCoord] = "empty"
            #moves piece to new postion
            z[x][y] = self
            #updates self
            self.xCoord = x
            self.yCoord = y
            return True
        #move down
        elif (x == self.xCoord) and (y == self.yCoord - 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #deals with enemy
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #empty previous postion
            z[self.xCoord][self.yCoord] = "empty"
            #moves piece to new postion
            z[x][y] = self
            #updates self
            self.xCoord = x
            self.yCoord = y
            return True
        #move down right
        elif (x == self.xCoord + 1) and (y == self.yCoord - 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #deals with enemy
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #empty previous postion
            z[self.xCoord][self.yCoord] = "empty"
            #moves piece to new postion
            z[x][y] = self
            #updates self
            self.xCoord = x
            self.yCoord = y
            return True
        #move down left
        elif (x == self.xCoord - 1) and (y == self.yCoord - 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #deals with enemy
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #empty previous postion
            z[self.xCoord][self.yCoord] = "empty"
            #moves piece to new postion
            z[x][y] = self
            #updates self
            self.xCoord = x
            self.yCoord = y
            return True
        else:
            print("This is not a valid move")
            return False

    def reportRank(self):
        return "white king"

class rKing:

    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y
        self.color = "red"
        self.value = "rking"

    def checkForEnemy(self, x, y, z):
        if z[x][y] != "empty":
            if z[x][y].color == "white":
                return True
        else:
            return False

    def kill(self):
        self.xCoord = -1
        self.yCoord = -1

    def move(self, x, y, z):
        #Kings cannot capture kings
        if z[x][y] != "empty":
            if z[x][y].value == "wking":
                print "Kings cannot capture kings"
                return False
        #move up
        if (x == self.xCoord) and (y == self.yCoord + 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            self.yCoord = y
            z[x][y] = self
            z[x][y-1] = "empty"
            return True
        #move up left
        elif (x == self.xCoord - 1) and (y == self.yCoord + 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            self.yCoord = y
            self.xCoord = x
            z[x][y] = self
            z[x+1][y-1] = "empty"
            return True
        #move up right
        elif (x == self.xCoord + 1) and (y == self.yCoord + 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            self.yCoord = y
            self.xCoord = x
            z[x][y] = self
            z[x-1][y-1] = "empty"
            return True
        #move right
        elif (x == self.xCoord + 1) and (y == self.yCoord) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #deals with enemy
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #sets previous postion to empty
            z[self.xCoord][self.yCoord] = "empty"
            #sets piece in new position
            z[x][y] = self
            #updates self
            self.xCoord = x
            self.yCoord = y
            return True
        #move left
        elif (x == self.xCoord - 1) and (y == self.yCoord) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #deals with enemy
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #empty previous postion
            z[self.xCoord][self.yCoord] = "empty"
            #moves piece to new postion
            z[x][y] = self
            #updates self
            self.xCoord = x
            self.yCoord = y
            return True
        #move down
        elif (x == self.xCoord) and (y == self.yCoord - 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #deals with enemy
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #empty previous postion
            z[self.xCoord][self.yCoord] = "empty"
            #moves piece to new postion
            z[x][y] = self
            #updates self
            self.xCoord = x
            self.yCoord = y
            return True
        #move down right
        elif (x == self.xCoord + 1) and (y == self.yCoord - 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #deals with enemy
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #empty previous postion
            z[self.xCoord][self.yCoord] = "empty"
            #moves piece to new postion
            z[x][y] = self
            #updates self
            self.xCoord = x
            self.yCoord = y
            return True
        #move down left
        elif (x == self.xCoord - 1) and (y == self.yCoord - 1) and (z[x][y] == "empty" or self.checkForEnemy(x, y, z)):
            #deals with enemy
            if (self.checkForEnemy(x, y, z)):
                z[x][y].kill()
            #empty previous postion
            z[self.xCoord][self.yCoord] = "empty"
            #moves piece to new postion
            z[x][y] = self
            #updates self
            self.xCoord = x
            self.yCoord = y
            return True
        else:
            print("This is not a valid move")
            return False

    def reportRank(self):
        return "red king"