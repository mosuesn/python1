time = int(input("Parking time (min): "))
hr = time // 60 + (1 if time % 60 > 0 else 0)

if hr <= 2:
    print("Free parking")
elif hr <= 7:
    print(f"Parking fee: {50 * (hr - 2)}")
elif hr <= 10:
    print(f"Parking fee: {(50 * 5) + \
        (20 * (hr - 7))}")
else:
    print(f"Parking fee: {1000*(hr//24 + \
        (1 if hr % 24 > 0 else 0))}")   