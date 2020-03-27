year = int(input("Δώστε έτος (-9090 για έξοδο): "))
while not year == -9090:
    disekto = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    if disekto:
        print("Το έτος", year, "ΕΙΝΑΙ δίσεκτο.")
    else:
        print("Το έτος", year, "ΔΕΝ ΕΙΝΑΙ δίσεκτο.")
    year = int(input("Δώστε έτος (-9090 για έξοδο): "))
