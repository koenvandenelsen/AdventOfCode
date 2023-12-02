import re

class Game:
    name = None
    R = 0
    G = 0
    B = 0

    def __init__(self, name):
        self.name = name


def part1(path):
    f = open(path, 'r')
    sum = 0
    gamesList = []
    
    for l in f.readlines():
        g = Game(int(re.search(r'Game (\d+):', l).group(1)))
        for grab in l.strip().split(':')[1].split(';'):
            for kind in grab.split(','):
                x = kind.split(' ')
                if x[2] == 'red':
                    if g.R < int(x[1]):
                        g.R = int(x[1])
                elif x[2] == 'green':
                    if g.G < int(x[1]):
                        g.G = int(x[1])
                elif x[2] == 'blue':
                    if g.B < int(x[1]):
                        g.B = int(x[1])
        gamesList.append(g)

    for g in gamesList:
        if g.R <= 12 and g.G <=13 and g.B <= 14:
            sum += g.name
            
    print(sum)

def part2(path):
    f = open(path, 'r')
    sum = 0
    gamesList = []
    
    for l in f.readlines():
        g = Game(int(re.search(r'Game (\d+):', l).group(1)))
        
        for grab in l.strip().split(':')[1].split(';'):
            for kind in grab.split(','):
                x = kind.split(' ')
                if x[2] == 'red':
                    if g.R < int(x[1]):
                        g.R = int(x[1])
                elif x[2] == 'green':
                    if g.G < int(x[1]):
                        g.G = int(x[1])
                elif x[2] == 'blue':
                    if g.B < int(x[1]):
                        g.B = int(x[1])
        gamesList.append(g)

    for g in gamesList:
        sum += g.R*g.G*g.B
            
    print(sum)

part2('input/examples/02.txt')
part2('input/02.txt')