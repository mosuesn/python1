# ======= hello world =======
print("hello world")

# ======= data types=======
str("hello") # str
int("3") # int
float("3.14") # float  
bool("True") # bool

print(type("hello")) # <class 'str'>
print(type(3)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type(True)) # <class 'bool'>

# ======= variables =======
width = 6767
height = 1212
print(f"area = {width * height}") # area = 8176404
print(f"perimeter = {2 * (width + height)}") # perimeter = 15958

# ======= operators =======
print(5 + 3) # 8
print(5 - 3) # 2
print(5 * 3) # 15
print(5 / 3) # 1.67
print(5 // 3) # 1
print(5 % 3) # 2
print(5 ** 3) # 125

# ======= comparison operators =======
print(5 == 3) # False
print(5 != 3) # True
print(5 > 3) # True
print(5 < 3) # False
print(5 >= 3) # True
print(5 <= 3) # False


# ======= conditional statements =======
food = 35
if food > 30:
    print("You have enough food") # You have enough food
print("done")

followers = 456789
if followers >= 1000000:
    print("You are a celebrity")
elif followers >= 100000:
    print("You are a famous person")
elif followers >= 10000:
    print("You are a popular person")

age = 15
student = True
if age < 12 and student:
    print("Free entry")
elif age < 18 or student:
    print("Discounted entry")
else:
    print("Full price entry")

score = 70
if score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
else:
    print("Grade: F")

# ======= loops =======
for i in range (3, 9, 2):
    print(i)

num = 0
while num < 5:
    print(num)
    num+=1

for num in range(10):
    if num % 3 == 0:
        print('AAA')
        print('---')
    print('BBB')
print('CCC')

for num in range(5):
    print('Counting', num)
    print('---------------')
    for current_number in range(1, num):
        print(current_number)
    print('--End of Loop--')