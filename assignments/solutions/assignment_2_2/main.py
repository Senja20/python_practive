A = []  # define list A
B = 0

while True:
    B = input('Enter: ')
    if B != 'stop':
        A.append(B)
    else:
        break  # if input is "stop", while loop will break

print(f'Unique : {len(set(A))}')  # set() makes new list with all times without repeating

print(f'Total : {len(A)}')  # print length of the list

for i in set(A):
    print(f'{i} : {A.count(i)}')  # print each element and the number entered in the list A
