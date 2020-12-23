from os import path

def insert(q, n):
    if not q or q[-1] in ('(', '*'): #
        q.append(n)
    else:
        q.pop()
        m = q.pop()
        q.append(n + m) #

def mult(q):
    while len(q) > 1:
        n = q.pop()
        op = q.pop()
        if op == '(':
            insert(q, n)
            break
        else:
            m = q.pop()
            q.append(n * m) #

def evaluate(tokens):
    q = []
    for token in tokens:
        if token in ('+', '*', '('):
            q.append(token)
        elif token == ')':
            mult(q)
        else:
            insert(q, int(token))
    mult(q)
    return sum(q)

with open(path.dirname(__file__) + '/input.txt') as f:
    print('Print sum of evaluating expressions, + has precence over *, evaluate left to right')
    print(sum([evaluate(line.strip('\n').replace('(', '( ').replace(')', ' )').split(' ')) for line in f.readlines()]))
