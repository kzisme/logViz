import fileinput


for line in fileinput.input():
    if '<' in line:
        prefix, sep, inner = line.partition('<'); 
        if '>' in line:
            inner, sep, suffix = inner.rpartition('>')
        print(inner)


