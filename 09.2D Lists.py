matrices = [[1, 2, 3],
             [4, 5, 7]]
matrices [1][2] = 6
print(matrices[1][2])
for row in matrices:
    for item in row:
        print(item)

"""
# List's Methods & Functions

append()
insert(index,  )
remove()
clear()
pop()
(List_name.index())
count()
sort()
reverse()
copy()

"""

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)