-- =========================================
-- SELECT
-- =========================================

-- 1. (שתי דרכים)
-- המנה שנקנתה הכי הרבה פעמים במסעדה מסוימת

-- דרך 1: עם GROUP BY + ORDER BY
SELECT sp.ProviderName, m.ItemName,
       COUNT(*) AS order_count,
       COUNT(*) * m.Price AS total_price
FROM ORDERLINE o
JOIN MENUITEM m ON o.ItemID = m.ItemID AND o.ProviderID = m.ProviderID
JOIN SERVICEPROVIDER sp ON sp.ProviderID = m.ProviderID
WHERE sp.ProviderName = 'Restaurant1'
GROUP BY sp.ProviderName, m.ItemName, m.Price
ORDER BY order_count DESC
LIMIT 1;


-- דרך 2: עם תת-שאילתה
SELECT sp.ProviderName, m.ItemName,
       COUNT(*) AS order_count,
       COUNT(*) * m.Price AS total_price
FROM ORDERLINE o
JOIN MENUITEM m ON o.ItemID = m.ItemID AND o.ProviderID = m.ProviderID
JOIN SERVICEPROVIDER sp ON sp.ProviderID = m.ProviderID
WHERE sp.ProviderName = 'Restaurant1'
GROUP BY sp.ProviderName, m.ItemName, m.Price
HAVING COUNT(*) = (
    SELECT MAX(cnt)
    FROM (
        SELECT COUNT(*) AS cnt
        FROM ORDERLINE o2
        JOIN MENUITEM m2 ON o2.ItemID = m2.ItemID AND o2.ProviderID = m2.ProviderID
        WHERE m2.ProviderID = sp.ProviderID
        GROUP BY m2.ItemID, m2.ProviderID
    ) sub
);


-- =========================================

-- 2. קופונים למסעדה "סטייקהאוס" ולתיירים מצרפת
SELECT c.CouponCode, c.DiscountPercent, c.EndDate
FROM COUPON c
JOIN SERVICEPROVIDER sp ON c.ProviderID = sp.ProviderID
JOIN INCLUDE i ON c.CouponID = i.CouponID
JOIN TOURISTDISCOUNT td ON i.DiscountID = td.DiscountID
WHERE sp.ProviderName = 'סטייקהאוס'
  AND td.Country = 'France';


-- =========================================

-- 3. הזמנות למסעדת "סושי" ברבעון האחרון של 2025
SELECT r.ReservationID,
       t.FirstName || ' ' || t.LastName AS TouristName,
       r.ReservationDate
FROM RESERVATION r
JOIN TOURIST t ON r.TouristID = t.TouristID
JOIN SERVICEPROVIDER sp ON r.ProviderID = sp.ProviderID
WHERE sp.ProviderName = 'סושי'
  AND r.ReservationDate BETWEEN '2025-10-01' AND '2025-12-31';


-- =========================================

-- 4. (שתי דרכים)
-- מנות שלא הוזמנו אף פעם

-- דרך 1: NOT EXISTS
SELECT sp.ProviderName, m.ItemName, m.Price
FROM MENUITEM m
JOIN SERVICEPROVIDER sp ON m.ProviderID = sp.ProviderID
WHERE NOT EXISTS (
    SELECT 1
    FROM ORDERLINE o
    WHERE o.ItemID = m.ItemID
      AND o.ProviderID = m.ProviderID
);


-- דרך 2: LEFT JOIN
SELECT sp.ProviderName, m.ItemName, m.Price
FROM MENUITEM m
JOIN SERVICEPROVIDER sp ON m.ProviderID = sp.ProviderID
LEFT JOIN ORDERLINE o
    ON m.ItemID = o.ItemID AND m.ProviderID = o.ProviderID
WHERE o.ItemID IS NULL;


-- =========================================
-- UPDATE
-- =========================================

-- 1. העלאת מחיר ב-10% למנות קינוחים בירושלים
UPDATE MENUITEM
SET Price = Price * 1.10
WHERE Category = 'קינוחים'
  AND ProviderID IN (
    SELECT ProviderID
    FROM SERVICEPROVIDER
    WHERE City = 'ירושלים'
);


-- =========================================

-- 2. עדכון תאריך סיום קופונים ליוון
UPDATE COUPON
SET EndDate = EndDate + INTERVAL '30 days'
WHERE CouponID IN (
    SELECT c.CouponID
    FROM COUPON c
    JOIN INCLUDE i ON c.CouponID = i.CouponID
    JOIN TOURISTDISCOUNT td ON i.DiscountID = td.DiscountID
    WHERE td.Country = 'Greece'
);


-- =========================================

-- 3. ביטול הזמנות
UPDATE RESERVATION
SET Status = 'Cancelled'
WHERE NumberOfPeople > 15
  AND ProviderID IN (
    SELECT ProviderID
    FROM SERVICEPROVIDER
    WHERE ServiceType = 'Cafe'
);


-- =========================================
-- DELETE
-- =========================================

-- 1. מחיקת שפות של תיירים שלא הזמינו
DELETE FROM TOURIST_LANGUAGE tl
WHERE NOT EXISTS (
    SELECT 1
    FROM RESERVATION r
    WHERE r.TouristID = tl.TouristID
);


-- =========================================

-- 2. מחיקת קופונים שפג תוקפם
DELETE FROM COUPON
WHERE EndDate < CURRENT_DATE;


-- =========================================

-- 3. מחיקת מנות זולות מחיפה
DELETE FROM MENUITEM
WHERE Price < 15
  AND ProviderID IN (
    SELECT ProviderID
    FROM SERVICEPROVIDER
    WHERE City = 'Haifa'
);