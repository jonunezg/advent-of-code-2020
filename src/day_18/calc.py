from os import path

def insert(q, n):
    if not q or q[-1] == '(':
        q.append(n)
    else:
        op = q.pop()
        m = q.pop()
        q.append(n + m if op == '+' else n * m)

def evaluate(tokens):
    q = []
    for token in tokens:
        if token in ('+', '*', '('):
            q.append(token)
        elif token == ')':
            n = q.pop()
            q.pop()
            insert(q, n)
        else:
            insert(q, int(token))
    return sum(q)

with open(path.dirname(__file__) + '/input.txt') as f:
    print('Print sum of evaluating expressions, + and * have the same precedence, evaluate left to right')
    result = 0
    for line in f.readlines():
        tokens = line.strip('\n').replace('(', '( ').replace(')', ' )').split(' ')
        result += evaluate(tokens)
    print(result)