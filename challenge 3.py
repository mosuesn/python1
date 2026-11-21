import sys
a, b, c, d = map(int, input("input: ").split())

#  swap sort
if a > b: a, b = b, a
if b > c: b, c = c, b
if c > d: c, d = d, c

if a > b: a, b = b, a
if b > c: b, c = c, b

if a > b: a, b = b, a

# selection sort
if a < b and a < c and a < d:
    a = a
elif b < a and b < c and b < d:
    a, b = b, a
elif c < a and c < b and c < d:
    a, c = c, a
elif d < a and d < b and d < c:
    a, d = d, a
else:
    # print("4 same")
    print(f"{((str(a) + " ") * 4).strip()}")
    sys.exit()

if b < c and b < d:
    b = b
elif c < b and c < d:
    b, c = c, b
elif d < b and d < c:
    b, d = d, b
else:
    # print("3 same")
    print(f"{a} {((str(b) + " ") * 3).strip()}")
    sys.exit()

if c < d:
    c = c
elif d < c:
    c, d = d, c
else:
    # print("2 same")
    print(f"{a} {b} {((str(c) + " ") * 2).strip()}")
    sys.exit()

print(f"{a} {b} {c} {d}")