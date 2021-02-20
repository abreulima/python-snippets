names = ["Carmen Sandiego", "Harry Potter", "Saint Paul"]
lasts = []

for n in names:
    last = n.split(" ")[-1]
    lasts.append(last)

print(lasts)

elements = ['a', 'b', '2', 'k', '🍕']
cap = []

for e in elements:
    if e.isalpha():
        cap.append(e.upper())

print(cap)