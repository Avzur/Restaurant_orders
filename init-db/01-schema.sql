import sqlite3

# Create / connect to database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.executescript("""

-- ========================
-- SERVICE PROVIDER
-- ========================
CREATE TABLE SERVICEPROVIDER (
  ProviderID INTEGER PRIMARY KEY,
  ProviderName VARCHAR(100) NOT NULL,
  ServiceType VARCHAR(50) NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  Address VARCHAR(150) NOT NULL,
  City VARCHAR(50) NOT NULL,
  Income NUMERIC(10,2) CHECK (Income >= 0)
);

-- ========================
-- TOURIST
-- ========================
CREATE TABLE TOURIST (
  TouristID INTEGER PRIMARY KEY,
  FirstName VARCHAR(50) NOT NULL,
  LastName VARCHAR(50) NOT NULL,
  Phone VARCHAR(20),
  Email VARCHAR(100) UNIQUE,
  Country VARCHAR(50) NOT NULL
);

-- ========================
-- RESERVATION
-- ========================
CREATE TABLE RESERVATION (
  ReservationID INTEGER PRIMARY KEY,
  ReservationDate DATE NOT NULL,
  NumberOfPeople INTEGER CHECK (NumberOfPeople > 0),
  Status VARCHAR(20) NOT NULL,
  ProviderID INTEGER NOT NULL,
  TouristID INTEGER NOT NULL,
  FOREIGN KEY (ProviderID) REFERENCES SERVICEPROVIDER(ProviderID),
  FOREIGN KEY (TouristID) REFERENCES TOURIST(TouristID)
);

-- ========================
-- MENU ITEM
-- ========================
CREATE TABLE MENUITEM (
  ItemID INTEGER,
  ProviderID INTEGER,
  ItemName VARCHAR(100) NOT NULL,
  Price NUMERIC(10,2) CHECK (Price >= 0),
  Category VARCHAR(50),
  PRIMARY KEY (ItemID, ProviderID),
  FOREIGN KEY (ProviderID) REFERENCES SERVICEPROVIDER(ProviderID)
);

-- ========================
-- COUPON
-- ========================
CREATE TABLE COUPON (
  CouponID INTEGER PRIMARY KEY,
  CouponCode VARCHAR(50) UNIQUE NOT NULL,
  DiscountPercent INTEGER CHECK (DiscountPercent BETWEEN 0 AND 100),
  StartDate DATE NOT NULL,
  EndDate DATE NOT NULL,
  ProviderID INTEGER NOT NULL,
  FOREIGN KEY (ProviderID) REFERENCES SERVICEPROVIDER(ProviderID)
);

-- ========================
-- TABLE (restaurant tables)
-- ========================
CREATE TABLE TABLER (
  TableID INTEGER,
  ProviderID INTEGER,
  TableNumber INTEGER NOT NULL,
  Seats INTEGER CHECK (Seats > 0),
  PRIMARY KEY (TableID, ProviderID),
  FOREIGN KEY (ProviderID) REFERENCES SERVICEPROVIDER(ProviderID)
);

-- ========================
-- TOURIST DISCOUNT
-- ========================
CREATE TABLE TOURISTDISCOUNT (
  DiscountID INTEGER PRIMARY KEY,
  Country VARCHAR(50) NOT NULL,
  Percent INTEGER CHECK (Percent BETWEEN 0 AND 100)
);

-- ========================
-- ASSIGN TABLE TO RESERVATION
-- ========================
CREATE TABLE AT (
  TableID INTEGER,
  ProviderID INTEGER,
  ReservationID INTEGER,
  PRIMARY KEY (TableID, ProviderID, ReservationID),
  FOREIGN KEY (TableID, ProviderID) REFERENCES TABLER(TableID, ProviderID),
  FOREIGN KEY (ReservationID) REFERENCES RESERVATION(ReservationID)
);

-- ========================
-- ORDER LINE
-- ========================
CREATE TABLE ORDERLINE (
  ItemID INTEGER,
  ProviderID INTEGER,
  ReservationID INTEGER,
  Quantity INTEGER DEFAULT 1 CHECK (Quantity > 0),
  PRIMARY KEY (ItemID, ProviderID, ReservationID),
  FOREIGN KEY (ItemID, ProviderID) REFERENCES MENUITEM(ItemID, ProviderID),
  FOREIGN KEY (ReservationID) REFERENCES RESERVATION(ReservationID)
);

-- ========================
-- COUPON INCLUDE DISCOUNT
-- ========================
CREATE TABLE INCLUDE (
  CouponID INTEGER,
  DiscountID INTEGER,
  PRIMARY KEY (CouponID, DiscountID),
  FOREIGN KEY (CouponID) REFERENCES COUPON(CouponID),
  FOREIGN KEY (DiscountID) REFERENCES TOURISTDISCOUNT(DiscountID)
);

-- ========================
-- TOURIST LANGUAGE
-- ========================
CREATE TABLE TOURIST_LANGUAGE (
  Language VARCHAR(50),
  TouristID INTEGER,
  PRIMARY KEY (Language, TouristID),
  FOREIGN KEY (TouristID) REFERENCES TOURIST(TouristID)
);

-- ========================
-- PROVIDER CULTURE
-- ========================
CREATE TABLE SERVICEPROVIDER_CULTURE (
  Culture VARCHAR(50),
  ProviderID INTEGER,
  PRIMARY KEY (Culture, ProviderID),
  FOREIGN KEY (ProviderID) REFERENCES SERVICEPROVIDER(ProviderID)
);

""")

conn.commit()
conn.close()

print("All tables created successfully!")