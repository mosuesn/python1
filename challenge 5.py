# num = int(input())
# digits = 1
# while num >= 1:
#     if num / 10 >= 1:
#         digits += 1
#     num /= 10

# num *= 10**digits
# num = int(num)

# reverse_num = 0

# for i in range(1, digits+1):
#     temp = num % (10**(digits-i))
#     temp = (num-temp)/(10**(digits-i))
#     reverse_num += temp*(10**(i-1))
#     num -= temp * (10**(digits-i))
# print(int(reverse_num))

num = int(input())
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print(reversed_num)