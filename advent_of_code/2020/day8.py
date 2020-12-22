import re

def parse_input(raw):
    return [
        (i, int(n))
        for i, n in
        re.findall(
            r'(.+) (.+)\n',
            raw
        )
    ]

with open('inputs/input8.txt') as file:
    input8 = parse_input(file.read())

def get_acc_once(instructions):
    executeds = list()
    accumulator = 0
    i = 0
    while True:
        if i in executeds:
            return accumulator, executeds
        try:
            operation, argument = instructions[i]
        except IndexError:
            return accumulator, []
        executeds.append(i)
        i += argument if operation == 'jmp' else 1
        accumulator += argument if operation == 'acc' else 0

def get_acc_changed_op(instructions):
    _, executeds = get_acc_once(instructions)
    for i in executeds:
        changed_ops = list(instructions)
        op, arg = changed_ops[i]
        if op == 'jmp':
            op = 'nop'
        elif op == 'nop':
            op = 'jmp'
        changed_ops[i] = [op, arg]

        accumulator, l = get_acc_once(changed_ops)
        if not l:
            return accumulator


answer1, _ = get_acc_once(input8)
answer2 = get_acc_changed_op(input8)

def test():
    raw = (
        'nop +0\n'
        'acc +1\n'
        'jmp +4\n'
        'acc +3\n'
        'jmp -3\n'
        'acc -99\n'
        'acc +1\n'
        'jmp -4\n'
        'acc +6\n'
    )
    sample = parse_input(raw)
    assert get_acc_once(sample)[0] == 5
    assert get_acc_changed_op(sample) == 8
