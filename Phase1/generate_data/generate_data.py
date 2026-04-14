import csv
import random
from datetime import date, timedelta

random.seed(42)

# ========================
# SERVICEPROVIDER (1000)
# ========================
providers = []

cities = ["Tel Aviv", "Haifa", "Jerusalem", "Eilat", "Ashdod"]
types = ["Restaurant", "Cafe", "Hotel"]

for i in range(1, 1001):
    providers.append([
        i,
        f"Provider{i}",
        random.choice(types),
        500000000 + i,
        f"Street {i}",
        random.choice(cities)
    ])

with open("SERVICEPROVIDER.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["ProviderID","ProviderName","ServiceType","Phone","Address","City"]] + providers
    )

# ========================
# TOURIST (1000)
# ========================
countries = ["Israel","USA","France","Germany","Italy","Spain","UK"]

tourists = []

for i in range(1, 20001):
    tourists.append([
        i,
        f"First{i}",
        f"Last{i}",
        500000000 + i,
        f"user{i}@mail.com",
        random.choice(countries),
        "pass" + str(i)
    ])

with open("TOURIST.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["TouristID","FirstName","LastName","Phone","Email","Country","Password"]] + tourists
    )

# ========================
# RESERVATION (1000)
# ========================
reservations = []

start = date(2025,1,1)
status_list = ["Pending","Confirmed","Cancelled"]

for i in range(1, 20001):
    reservations.append([
        i,
        start + timedelta(days=random.randint(0, 365)),
        random.randint(1, 6),
        random.choice(status_list),
        random.randint(1, 1000),
        random.randint(1, 1000)
    ])

with open("RESERVATION.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["ReservationID","ReservationDate","NumberOfPeople","Status","ProviderID","TouristID"]] + reservations
    )

# ========================
# MENUITEM (1000)
# ========================
menu = []

item_names = ["Burger","Pizza","Salad","Coffee","Tea","Juice","Steak","Fish"]
categories = ["Food","Drink"]

for i in range(1, 1001):
    menu.append([
        i,
        random.choice(item_names),
        random.randint(10,150),
        random.choice(categories),
        random.randint(1, 1000)
    ])

with open("MENUITEM.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["ItemID","ItemName","Price","Category","ProviderID"]] + menu
    )

# ========================
# COUPON (1000)
# ========================
coupons = []

for i in range(1, 1001):
    start_d = date(2025,1,1)
    end_d = date(2025,12,31)

    coupons.append([
        i,
        f"DISC{i}",
        random.randint(5, 50),
        start_d,
        end_d,
        random.randint(1, 1000)
    ])

with open("COUPON.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["CouponID","CouponCode","DiscountPercent","StartDate","EndDate","ProviderID"]] + coupons
    )

# ========================
# TOURIST_LANGUAGE (1000)
# ========================
langs = ["Hebrew","English","French","German","Spanish","Italian"]

tourist_lang = []

for i in range(1, 1001):
    for _ in range(random.randint(1,2)):
        tourist_lang.append([
            random.choice(langs),
            random.randint(1, 1000)
        ])

with open("TOURIST_LANGUAGE.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["Language","TouristID"]] + tourist_lang
    )

print("DONE: 1000 rows generated for each table")