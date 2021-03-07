class Monster:

    def __init__(self, name, level):
        self.name = name
        self.level = level

bug = Monster("Bug", 5)
wolf = Monster("Wolf", 2)

monsters = [bug, wolf]

print("Sorting by name")
monsters.sort(key = lambda a : a.name)
for m in monsters:
    print(m.name, m.level)

print()

print("Sorting by level")
monsters.sort(key = lambda a : a.level)
for m in monsters:
    print(m.name, m.level)