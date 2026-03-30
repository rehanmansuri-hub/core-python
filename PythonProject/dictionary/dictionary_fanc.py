d = {'name': 'rehan','surname': 'mansuri','age': 19}
print(d)

# 1. clear()

list = d.copy()
list.clear()
print(list)


# 2.get()

print(d.get('name'))
print(d.get('age'))

# 3.keys()

print(d.keys())

# 4.values()
print(d.values())

# 5.items()
print(d.items())

# 6.copy()
print(d.copy())

# 7.pop()
d.pop('age')
print(d)

# 8.poptime()
d.popitem()
print(d)

# 9.update()
d.update({'age': 20,'country': 'india'})
print(d)

# 10.setdefault()
d.setdefault('marks',90)
print(d)

# 11.len()
print(len(d))