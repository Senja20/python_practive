
A = input("First string:")
B = input("Second string:")

if A == B:
    print("are equal")
else:
    print("are not equal")

if A in B:
    print("is a substring")
elif B in A:
    print("is a substring")
else:
    print("is not a substring")