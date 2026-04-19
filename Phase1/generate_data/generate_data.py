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

for i in range(1, 1001):
    tourists.append([
        i,
        f"First{i}",
        f"Last{i}",
        500000000 + i,
        f"user{i}@mail.com",  # UNIQUE
        random.choice(countries),
        "pass" + str(random.randint(1000,9999))  # length >= 4
    ])

with open("TOURIST.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["TouristID","FirstName","LastName","Phone","Email","Country","Password"]] + tourists
    )

# ========================
# RESERVATION (20000)
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
    provider_id = random.randint(1, 1000)
    menu.append([
        i,
        random.choice(item_names),
        random.randint(10,150),
        random.choice(categories),
        provider_id
    ])

with open("MENUITEM.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["ItemID","ItemName","Price","Category","ProviderID"]] + menu
    )

# 👉 חשוב: מפתחות קיימים ל-FK מורכב
menu_keys = [(row[0], row[4]) for row in menu]

# ========================
# COUPON (500)
# ========================
coupons = []

for i in range(1, 501):
    start_d = date(2025,1,1)
    end_d = date(2025,12,31)

    coupons.append([
        i,
        f"DISC{i}",  # UNIQUE
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
# TOURISTDISCOUNT (500)
# ========================
tourist_discounts = []
discount_countries = ["Israel","USA","France","Germany","Italy","Spain","UK"]

for i in range(1, 501):
    tourist_discounts.append([
        random.choice(discount_countries),
        random.randint(5, 50),
        i
    ])

with open("TOURISTDISCOUNT.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["Country","Percent","DiscountID"]] + tourist_discounts
    )

# ========================
# RESTAURANT_TABLE (1000)
# ========================
tables = []

for i in range(1, 1001):
    tables.append([
        random.randint(1, 20),
        random.randint(2, 10),
        i,
        random.randint(1, 1000),
        random.randint(1, 20000)
    ])

with open("RESTAURANT_TABLE.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["TableNumber","Seats","TableID","ProviderID","ReservationID"]] + tables
    )

# ========================
# ORDERLINE (FIXED ✅)
# ========================
orderlines = set()
orderline_rows = []

for res_id in range(1, 20001):
    for _ in range(random.randint(1, 2)):
        item_id, provider_id = random.choice(menu_keys)

        key = (item_id, provider_id, res_id)
        if key not in orderlines:
            orderlines.add(key)
            orderline_rows.append([item_id, provider_id, res_id])

with open("ORDERLINE.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["ItemID","ProviderID","ReservationID"]] + orderline_rows
    )

# ========================
# INCLUDE (500)
# ========================
includes = set()
include_rows = []

while len(include_rows) < 500:
    cid = random.randint(1, 500)
    did = random.randint(1, 500)

    if (cid, did) not in includes:
        includes.add((cid, did))
        include_rows.append([cid, did])

with open("INCLUDE.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["CouponID","DiscountID"]] + include_rows
    )

# ========================
# TOURIST_LANGUAGE (>=500)
# ========================
langs = ["Hebrew","English","French","German","Spanish","Italian"]
tourist_lang = set()
lang_rows = []

for i in range(1, 1001):
    for _ in range(random.randint(1, 2)):
        key = (random.choice(langs), i)
        if key not in tourist_lang:
            tourist_lang.add(key)
            lang_rows.append([key[0], key[1]])

with open("TOURIST_LANGUAGE.csv", "w", newline="") as f:
    csv.writer(f).writerows(
        [["Language","TouristID"]] + lang_rows
    )

print("DONE ✅ הכל תקין בלי שגיאות FK")