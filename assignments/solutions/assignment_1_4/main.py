
A = input("Enter: ")

B = [0] * (ord('z') - ord('a') + 1)

for char in A:
    B[ord(char) - ord('a')] += 1

for index, count in enumerate(B):

    C = chr(index + ord('a'))

    if count != 0:
        print(f'\'{C}\' : {count}')