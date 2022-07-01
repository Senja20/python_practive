#Numbers 1 to 10
for x in range(10):
    x = x + 1
    print(x, end=' ')

print('\n')
#Numbers 1 to 20, only even numbers
count2 = -1
while count2 < 19:
    count2 = count2 + 2
    print(count2, end=' ')

print('\n')
#Numbers 1 to 20, only odd numbers
count3 = 0
for a in range(10):
    count3 = count3 + 2
    print(count3, end=' ')

print('\n')
#Numbers 1 to 50, every 3rd number
count5 = -2
while count5 < 48:
    count5 = count5 + 3
    print(count5, end=' ')

print('\n')
#Numbers 1 to 40, reverse order, every 4th number
count4 = 44
while count4 > 4:
    count4 = count4 - 4
    print(count4, end=' ')

print('\n')

for count6 in range(100):
    if count6 > 1:
        for a in range(2, count6):
            if (count6 % a) == 0:
                break
        else:
            print(count6, end=' ')