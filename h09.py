# -*- coding: utf-8 -*-


from math import sqrt
import random
import matplotlib.pyplot as plt


class Location:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def move(self, dx, dy):
        return Location(self.x + float(dx), self.y + float(dy))

    def getCoords(self):
        return self.x, self.y

    def getDistance(self, other):
        o_x, o_y = other.getCoords()
        xDist = self.x - o_x
        yDist = self.y - o_y
        return sqrt(xDist ** 2 + yDist ** 2)


class Direction:
    possibles = ['N', 'E', 'S', 'W']

    def __init__(self, direction):
        if direction in self.possibles:
            self.direction = direction
        else:
            raise ValueError(
                "Unknown direction {} in Direction.__init__".format(direction))

    def move(self, dist):
        if self.direction == 'N':
            return (0, dist)
        elif self.direction == 'E':
            return (dist, 0)
        elif self.direction == 'S':
            return (0, -dist)
        elif self.direction == 'W':
            return (-dist, 0)
        else:
            raise ValueError("Unexpected direction in Direction.move")


class Field:
    def __init__(self, drunk, loc):
        self.drunk = drunk
        self.loc = loc

    def move(self, direction, dist):
        oldLoc = self.loc
        dx, dy = direction.move(dist)
        self.loc = oldLoc.move(dx, dy)

    def getLoc(self):
        return self.loc

    def getDrunk(self):
        return self.drunk


class Drunk:
    def __init__(self, name):
        self.name = name

    def move(self, field, direction, steps=1):
        if field.getDrunk() != self:
            raise ValueError(
                "Drunk.move called when drunk was not added to a field")
        for i in range(steps):
            field.move(direction, 1)


class UsualDrunk(Drunk):
    def move(self, field, steps=1):
        direction = Direction(random.choice(Direction.possibles))
        Drunk.move(self, field, direction, steps)


class BiasedDrunk(Drunk):
    def move(self, field, steps=1):
        # https://github.com/ianmagyar/introduction-to-python/blob/master/assignments/homeworks.md#h9
        # the drunk should move with probabilities:
        # N - 10%, E - 10%, S - 50%, W - 30%
        # step size to west should be 2

        # nie najkrajšie, ale správne riešenie - 2b
        sides = ['N','E','S','S','S','S','S','W','W','W']
        direction = Direction(random.choice(sides));
        if(direction == 'W'):
          Drunk.move(self, field, direction, 2*steps)
        else:
          Drunk.move(self, field, direction, steps)


def performTrial(steps, field):
    start = field.getLoc()
    distances = [0.0]
    for t in range(1, steps + 1):
        field.getDrunk().move(field)
        newLoc = field.getLoc()
        distance = newLoc.getDistance(start)
        distances.append(distance)
    return distances, newLoc.getCoords()


def performSim(steps, numTrials, drunkType):
    distLists = []
    endPoints = []
    for trial in range(numTrials):
        d = drunkType("Drunk" + str(trial))
        f = Field(d, Location(0, 0))
        distances, endPoint = performTrial(steps, f)
        distLists.append(distances)
        endPoints.append(endPoint)
    return distLists, endPoints


def ansQuest(steps, numTrials, drunkType, title):
    means = []
    distLists, endPoints = performSim(steps, numTrials, drunkType)
    for t in range(steps + 1):
        total = 0.0
        for distL in distLists:
            total += distL[t]
        means.append(total / len(distLists))
    plt.figure()
    plt.plot(means)
    plt.ylabel('distance')
    plt.xlabel('time')
    plt.title('Average distance vs. Time for {} ({} trials)'.format(
        title, numTrials))

    X = [p[0] for p in endPoints]
    Y = [p[1] for p in endPoints]
    plt.figure()
    plt.scatter(X, Y)
    plt.xlabel('x distance')
    plt.ylabel('y distance')
    plt.title('End points for {}'.format(title))

    plt.figure()
    plt.hist(X)
    plt.xlabel('X distance')
    plt.ylabel('Number of trials')
    plt.title(title + ' Distribution of X distances')


ansQuest(500, 300, BiasedDrunk, 'BiasedDrunk')
plt.show()

#ansQuest(500, 300, ColdDrunk, 'ColdDrunk')
#plt.show()

#ansQuest(500, 300, EWDrunk, 'EWDrunk')
#plt.show()
