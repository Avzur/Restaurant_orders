-- =========================================
-- INDEXES
-- =========================================

-- =========================================
-- בדיקת זמן ריצה לפני אינדקס
-- =========================================

EXPLAIN ANALYZE
SELECT *
FROM RESERVATION
WHERE TouristID = 100;


-- =========================================
-- INDEX 1: על TouristID בטבלת RESERVATION
-- =========================================

CREATE INDEX idx_reservation_tourist
ON RESERVATION(TouristID);


-- בדיקה אחרי
EXPLAIN ANALYZE
SELECT *
FROM RESERVATION
WHERE TouristID = 100;


-- =========================================
-- INDEX 2: על ProviderID בטבלת RESERVATION
-- =========================================

CREATE INDEX idx_reservation_provider
ON RESERVATION(ProviderID);


-- בדיקה
EXPLAIN ANALYZE
SELECT *
FROM RESERVATION
WHERE ProviderID = 50;


-- =========================================
-- INDEX 3: אינדקס מורכב על ORDERLINE
-- =========================================

CREATE INDEX idx_orderline_item_provider
ON ORDERLINE(ItemID, ProviderID);


-- בדיקה
EXPLAIN ANALYZE
SELECT *
FROM ORDERLINE
WHERE ItemID = 10 AND ProviderID = 20;