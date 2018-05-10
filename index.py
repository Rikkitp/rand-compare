import random

THINGS = [
  'Thing 1',
  'Thing 2',
  'Thing 3'
]

things = THINGS[:]
result = []

comparisons = []

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
            print("\n\nResult:")
            for i, thing in enumerate(result + things):
                print("%d. %s" % (i + 1, thing))
            exit()
