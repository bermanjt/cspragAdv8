#!/usr/bin/env python3

import readline
from sty import fg, bg, ef, rs, RgbFg
import operator

operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow, 
}


def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:    
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1,arg2)
            stack.append(result)
        print(stack)
        
    if len(stack) != 1:
        raise TypeError('malformed input')
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        if int(result) < 0:
            print(fg.red + str(result) + fg.rs)
        else:
            print(fg.blue + str(result) + fg.rs)


if __name__ == '__main__':
    main()

 
