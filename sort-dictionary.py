monsters = [
    {
        "Name" : "Slime",
        "Level" : 1
    },
    {
        "Name" : "Spider",
        "Level" : 5
    },
    {
        "Name" : "Bug",
        "Level" : 2
    },
    {
        "Name" : "Troll",
        "Level" : 8
    }
]

print("Sorting by name")
monsters.sort(key = lambda a : a["Name"])
print(monsters)

print("Sorting by level")
monsters.sort(key = lambda a : a["Level"])
print(monsters)