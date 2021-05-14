#!/usr/bin/python3

from os import path as ospath, get_terminal_size
from math import floor
from typing import List
import readline, glob

example = [
    'Plants absorb metal compounds, in this case containing copper(II)',
    'Plants are harvested and combusted',
    'Acid added to ash producing dissolved metal solution',
    'Copper extracted from solution'
]

def complete(text, state):
    return (glob.glob(ospath.expanduser(text)+'*')+[None])[state]

def getInput() -> str:
    readline.set_completer_delims(' \t\n;')
    readline.parse_and_bind('tab: complete')
    readline.set_completer(complete)
    return input('Flowchart filepath [Leave empty for demo]> ')

def box(text: str, width: int) -> str:
    msg = '##' + '#' * width + '##\n## '
    for line in text.split('\n'):
        i = 0
        j = 1
        while i < len(line):
            if i != 0 and (i / (width - 1)).is_integer():
                msg += ' ' * (width - (i - j * width) - 2 - width) + '##\n## '
                j+=1
            msg += line[i]
            if i == len(line) - 1:
                msg += ' ' * ((width * j) - i - j - 1) + '##'
            i+=1
            
    msg += '\n' + '#' * (width + 2) + '##'
    
    return msg

def loadData(path: str) -> List[str]:
    ret = []
    with open(path, 'r') as file:
        ret = file.readlines()
    return ret

def showBoxes(text: List[str]):
    width = floor(get_terminal_size().columns / 2)
    boxes = [box(item, width) for item in text]
    for i in range(0, len(boxes)):
        print(boxes[i])
        if i < len(boxes) - 1: print(' ' * floor(len(boxes[i].split('\n')[0])/2) + 'v')

if __name__ == '__main__':
    path = getInput()
    if path == '':
        print('\n== Process of Phytomining ==\n')
        showBoxes(example)
    else:
        showBoxes(loadData(path))
