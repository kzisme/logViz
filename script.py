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

         
