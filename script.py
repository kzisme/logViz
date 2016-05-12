import json
import fileinput

# Descriptive names are better than type names. On Python 2 you'd have overwritten the `file` global (builtin) class.
# We avoid "with" usage here because the file is long-lived; no need to indent absolutely every other line just to
# have an open file.  Using "with" for that is optimized for small snippets of code that open files, i.e. just to
# write an existing variable out, then close.
usernames = open('usernames.txt', 'a')

# If a name is still pretty generic, comments are good to add. Many editors will show comments and docstrings in
# completion listss or help tooltips and such.  (Pymode in Vim does. ;)
count = {}  # Track the number of occurances of each unique username.

for line in fileinput.input():
    # Exit early if this line is missing a username.  Again, saves indenting every other line.
    if '<' not in line or '>' not in line:
        continue
    
    # Separate the username from the rest of the line.
    prefix, sep, username = line.partition('<')
    username, sep, suffix = username.partition('>')

    strippedUsername = username.strip('~!@+%&$_').lstrip()

    # Track occurances.
    count.setdefault(strippedUsername, 0)
    count[strippedUsername] += 1
    
    # Record the occurance.
    usernames.write(strippedUsername + "\n")

#print(json.dumps(count))
with open('data.json', 'w') as outfile:
    #json.dump(count, outfile,indent = 4)
    #print(json.dumps(list(count.items())))
    print json.dump([dict(val=val, name=name) for (name, val) in count.items()],outfile)
