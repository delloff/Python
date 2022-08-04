# Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.
# If you need to modify the sequence you are iterating over while inside the loop (for example to duplicate selected items),
# it is recommended that you first make a copy. Iterating over a sequence does not implicitly make a copy.


# remove items from one list and put them to another

names = ['foo', 'bar']
new_names = []

# option 1 (preferred)
for i in names[:]:
    new_names.append(i)
    names.remove(i)

#-----------------------

#option 2
for i in range(len(names)):
    new_names.append(names[0])
    names.remove(names[0])

#-----------------------

print(names, new_names)
