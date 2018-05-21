import random
import sys
import pathlib

THINGS = [
]

if len(sys.argv) == 2:
    with open(sys.argv[1]) as f:
        for line in f:
            THINGS.append(line.strip())
    path = pathlib.Path(sys.argv[1]).stem

things = THINGS[:]

result = []

comparisons = []

def finish():
    print("\n\nResult:")
    for i, thing in enumerate(result + things):
        print("%d. %s" % (i + 1, thing))

    if path:
        f = open(path + ".out.txt", 'w')
        for i, thing in enumerate(result + things):
            f.write("%d. %s\n" % (i + 1, thing))
        f.close()
    exit()

while True:
    choice = None
    comparison = random.sample(things, 2)

    if (comparison[0], comparison[1]) in comparisons:
        choice = "1"
    elif (comparison[1], comparison[0]) in comparisons:
        choice = "2"
    else:
        print("\n\nChoose:")
        for i, thing in enumerate(comparison):
            print("%d. %s" % (i + 1, thing))
        choice = input("> ")

    if choice == "1":
        comparisons.append((comparison[0], comparison[1]))
        things.remove(comparison[1])
    elif choice == "2":
        comparisons.append((comparison[1], comparison[0]))
        things.remove(comparison[0])

    if len(things) < 2:
        result.append(things[0])
        things = list(set(THINGS[:]) - set(result))
        if len(things) < 2:
            finish()
