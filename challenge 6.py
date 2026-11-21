ip = list(map(int, input().split("."))) # 10.110.224.151
binary = []
base10 = []

index = 0

for n in ip:
    binary.append("")
    while n > 0:
        binary[index] = f"{str(n%2)}{binary[index]}"
        n//=2
    index+=1

print(".".join(binary))

index2 = 0

for b in binary:
    base10.append(0)
    for a in range(len(b)):
        temp = int(b[-1])
        base10[index2] += temp*(2**a)
        b = b[:-1]
    base10[index2] = str(base10[index2])
    index2+=1

print(".".join(base10))