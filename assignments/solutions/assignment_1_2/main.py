
A = input("Enter here: ")

#Count
print(len(A))

def palindrome(A):
    for i in range(int(len(A)/2)):

        if A[i] != A[len(A)-i-1]:
            return False
        else:
            return True

if palindrome(A):
    print("is a palindrome")
else:
    print("is not a palindrome")

B = ''.join(reversed(A))

print(B)

