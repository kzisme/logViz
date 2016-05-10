import fileinput


for line in fileinput.input():
    if '<' in line:
        prefix, sep, inner = line.partition('<');
        inner, sep, suffix = inner.rpartition('>')
        if line.partition(">")[1] == '>':
            prefix, sep, inner = line.partition('<');
            inner, sep, suffix = inner.rpartition('>')
        print inner.partition('>')[0]


