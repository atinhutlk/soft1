seasons = ("winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter")
month = int(input("Enter the month : "))
if month in range(1, 13):
    print(f"Month {month} is in {seasons[month - 1]}")
else:
    print("invalid number.")