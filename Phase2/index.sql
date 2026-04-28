

EXPLAIN ANALYZE
SELECT *
FROM RESERVATION
WHERE TouristID = 100;


-- =========================================
-- INDEX 1:
-- =========================================

CREATE INDEX idx_reservation_tourist
ON RESERVATION(TouristID);



EXPLAIN ANALYZE
SELECT *
FROM RESERVATION
WHERE TouristID = 100;


-- =========================================
-- INDEX 2:
-- =========================================

CREATE INDEX idx_reservation_provider
ON RESERVATION(ProviderID);


EXPLAIN ANALYZE
SELECT *
FROM RESERVATION
WHERE ProviderID = 50;


-- =========================================
-- INDEX 3:
-- =========================================

CREATE INDEX idx_orderline_item_provider
ON ORDERLINE(ItemID, ProviderID);


EXPLAIN ANALYZE
SELECT *
FROM ORDERLINE
WHERE ItemID = 10 AND ProviderID = 20;