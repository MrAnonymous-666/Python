# If-else Loop

# weight = int(input('Weight:  '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print (f" You are {converted} Kilos")
# else:
#     converted = weight /  0.45
#     print(f"you are {converted} Pounds")

# While loop

i = 1
while i <= 5:
    print('*' * i)
    i = i+1
print('Done')

# Guessing game using while loop

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count +=1
    if guess == secret_number:
        print('You won')
        break
    else :
        print('You lose')