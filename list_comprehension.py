names = ["Carmen Sandiego", "Harry Potter", "Saint Paul"]

# [ <action> for <object> in <list> ]
last = [n.split(" ")[-1] for n in names]

print(last)

elements = ['a', 'b', '2', 'k', '🍕']

# [ <action> for <object> in <list> if <condition> ]
cap = [e.upper() for e in elements if e.isalpha()]

print(cap)