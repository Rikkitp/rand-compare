import pathlib
import random
import sys
from typing import Optional, List

THINGS = []


def save(result: List[str], things: List[str], all_things: bool = False):
    things0: List[str] = list(result + things) if all_things else list(result)

    print("\n\nResult:")

    if path:
        with open(path + ".out.txt", 'w') as f:
            for i, thing in enumerate(things0):
                print(" %d. %s" % (i + 1, thing))
                f.write("%d. %s\n" % (i + 1, thing))


def main(things) -> None:
    things = THINGS[:]
    result = []
    comparisons = []

    while True:
        choice: Optional[str] = None
        comparison = random.sample(things, 2)
        if (comparison[0], comparison[1]) in comparisons:
            choice = "1"
        elif (comparison[1], comparison[0]) in comparisons:
            choice = "2"
        else:
            print("\n\nChoose (%d left to #%d):" % (len(things), len(result) + 1))
            for i, thing in enumerate(comparison):
                print("%d. %s" % (i + 1, thing))
            choice = input("> ")

        if choice in ("1", "2"):
            a1i = int(choice) - 1
            a2i = 1 ^ a1i
            comparisons.append((comparison[a1i], comparison[a2i]))
            things.remove(comparison[a2i])
        elif "-" in choice:
            ai = int(choice[1]) - 1
            things.remove(comparison[ai])
            THINGS.remove(comparison[ai])

        if len(things) < 2:
            result.append(things[0])
            things = list(set(THINGS[:]) - set(result))
            save(result, things)
            if len(things) < 2:
                save(result, things, True)
                exit()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            for line in f:
                THINGS.append(line.strip())
        path = pathlib.Path(sys.argv[1]).stem

    main(THINGS)
