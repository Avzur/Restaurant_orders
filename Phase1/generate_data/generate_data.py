import csv
from random import randint, choice
from datetime import date, timedelta

# ========================
# SERVICEPROVIDER
# ========================
providers = []
for i in range(1, 6):
    providers.append([
        i,
        f"Provider{i}",
        choice(["Restaurant", "Cafe", "Hotel"]),
        500000000 + i,
        f"Street {i}",
        choice(["Tel Aviv", "Haifa", "Jerusalem", "Eilat"])
    ])

with open("SERVICEPROVIDER.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["ProviderID","ProviderName","ServiceType","Phone","Address","City"]] + providers
    )

# ========================
# TOURIST
# ========================
countries = ["Israel","USA","France","Germany","Italy","Spain","UK"]
tourists = []

for i in range(1, 11):
    tourists.append([
        i,
        f"Name{i}",
        f"Last{i}",
        500000000 + i,
        f"user{i}@mail.com",
        choice(countries),
        "pass" + str(i)
    ])

with open("TOURIST.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["TouristID","FirstName","LastName","Phone","Email","Country","Password"]] + tourists
    )

# ========================
# RESERVATION
# ========================
reservations = []
start = date(2025,1,1)

for i in range(1, 11):
    reservations.append([
        i,
        start + timedelta(days=i),
        randint(1,6),
        choice(["Pending","Confirmed","Cancelled"]),
        randint(1,5),
        randint(1,10)
    ])

with open("RESERVATION.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["ReservationID","ReservationDate","NumberOfPeople","Status","ProviderID","TouristID"]] + reservations
    )

# ========================
# MENUITEM
# ========================
menu = []
item_id = 1

for p in range(1, 6):
    for _ in range(3):
        menu.append([
            item_id,
            choice(["Burger","Pizza","Salad","Coffee","Tea","Juice"]),
            randint(10,120),
            choice(["Food","Drink"]),
            p
        ])
        item_id += 1

with open("MENUITEM.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["ItemID","ItemName","Price","Category","ProviderID"]] + menu
    )

# ========================
# COUPON
# ========================
coupons = []
for i in range(1,6):
    start_d = date(2025,1,1)
    end_d = date(2025,12,31)
    coupons.append([
        i,
        f"DISC{i*10}",
        i*5,
        start_d,
        end_d,
        randint(1,5)
    ])

with open("COUPON.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["CouponID","CouponCode","DiscountPercent","StartDate","EndDate","ProviderID"]] + coupons
    )

# ========================
# TOURIST_LANGUAGE
# ========================
langs = []
for i in range(1, 11):
    for _ in range(randint(1,2)):
        langs.append([
            choice(["Hebrew","English","French","German","Spanish","Italian"]),
            i
        ])

with open("TOURIST_LANGUAGE.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["Language","TouristID"]] + langs
    )