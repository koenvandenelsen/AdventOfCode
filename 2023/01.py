import re

nd = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def part1(path):
    sum = 0

    f = open(path, 'r')
    
    for l in f.readlines():
        parseLine = re.findall(r'\d', l)
        sum += int(f'{parseLine[0]}{parseLine[-1]}')

    print(sum)

def part2(path):
    sum = 0

    f = open(path, 'r')
    
    for l in f.readlines():
        parseLine = re.findall(rf'(?=(\d|{"|".join(nd)}))', l)

        component1 = nd[parseLine[0]] if parseLine[0] in nd else parseLine[0]
        component2 = nd[parseLine[-1]] if parseLine[-1] in nd else parseLine[-1]
            
        sum += int(f'{component1}{component2}')

    print(sum)

part1('./input/01.txt')
part2('./input/01.txt')