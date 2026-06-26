names = ['John','Bob', 'Mosh', 'Sarah', 'Mary']
names[0] ='Johnny' # modifying the item in list
print(names[2:4]) # number+1 to number-1 but does no include number
print(names)

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)