from os import path

def parse(rules, index, data):
    matched = []
    for rule in rules[index]:
        if rule[0][0] == '"' and rule[0][2] == '"': # Check for terminal character
            return [data[1:]] if data and data[0] == rule[0][1] else []
        else:
            next = [data]
            for p in rule:  # Parse sequentially each member of the rule
                parsed = []
                for n in next:
                    parsed += parse(rules, p, n)
                next = parsed # The new options are the successfully parsed remaining strings in each step
            matched += next
    return matched

with open(path.dirname(__file__) + '/input.txt') as f:
    print('Evaluate each expression with the production rules, count the number of valid expressions')
    rules = {}
    rules_text, expressions = f.read().split('\n\n')
    for line in rules_text.split('\n'):
        rules[line.split(': ')[0]] = [rule.split(' ') for rule in line.split(': ')[1].split(' | ')]
    print(sum([1 if [True for match in parse(rules, '0', exp + '$') if match == '$'] else 0 for exp in expressions.split('\n')]))