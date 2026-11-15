member = input("""Select membership:
1) VIP
2) Regular
3) Non-member
-> """)

price = int(input("Price:"))

if member == "1":
    print("20% discount" if price > 5000 else "15% discount")
    print(f"Price: {price - (price * 20/100)}" if price > 5000 \
          else f"Price: {price - (price * 15/100)}")
elif member == "2":
    print("10% discount" if price > 5000 else "5% discount")
    print(f"Price: {price - (price * 10/100)}" if price > 5000 \
          else f"Price: {price - (price * 5/100)}")
else:
    print("No discount")
    print(f"Price: {price}")