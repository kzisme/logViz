import fileinput


with open('usernames.txt', 'a') as file:
    for line in fileinput.input():
        if '<' in line:
            prefix, sep, inner = line.partition('<');
            inner, sep, suffix = inner.rpartition('>')
            if line.partition(">")[1] == '>':
                prefix, sep, inner = line.partition('<');
                inner, sep, suffix = inner.rpartition('>')
            usernames = inner.partition('>')[0];
            for user in usernames:
                file.write("%s\n" %usernames);

count = {}
for w in open('usernames.txt').read().split():
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
for word, times in count.items():
    print "%s was found %d times" % (word, times)
