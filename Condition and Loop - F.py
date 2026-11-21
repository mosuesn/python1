start, end = int(input()), int(input())
start += 1 if start%2 == 1 else 0
for i in range(start, end+1, 2):
    print(i)