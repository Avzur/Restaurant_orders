--SELECT Query--

-- 1. (שתי דרכים) תציג את שם התייר, שם המשפחה, מדינת המוצא שלו – עבור תיירים שעשו הזמנה בחודש ינואר בשנת 2026
select FirstName, LastName, Country
from TOURIST
where TouristID in (
	select TouristID
	from RESERVATION
	WHERE EXTRACT(YEAR FROM ReservationDate) = 2026
    AND EXTRACT(MONTH FROM ReservationDate) = 1
	)


SELECT DISTINCT t.FirstName, t.LastName, t.Country
FROM TOURIST t
JOIN RESERVATION r ON t.TouristID = r.TouristID
WHERE EXTRACT(YEAR FROM r.ReservationDate) = 2026
AND EXTRACT(MONTH FROM r.ReservationDate) = 1


--2. (שתי דרכים) תציג את שם התייר, כתובת המסעדה, עיר המסעדה ושם המסעדה שעבורה תייר בשם "First80" ביצע הזמנה
SELECT FirstName, ProviderName, Address, City
FROM TOURIST t
JOIN RESERVATION r ON t.TouristID = r.TouristID
JOIN SERVICEPROVIDER sp ON r.ProviderID = sp.ProviderID
WHERE t.FirstName = 'First80'


SELECT FirstName, ProviderName, Address, City
FROM TOURIST t, RESERVATION r, SERVICEPROVIDER sp
WHERE t.TouristID = r.TouristID
AND r.ProviderID = sp.ProviderID
AND t.FirstName = 'First80'


--3. תציג לי את שמות ומחירי התפריטים של מסעדות שסוג השירות שלהם הוא "קפה" בסדר עולה של השמות
SELECT ItemName, Price
FROM MENUITEM m, SERVICEPROVIDER sp
WHERE m.ProviderID = sp.ProviderID
AND ServiceType = 'Cafe'
ORDER BY (ItemName)


--4. (שתי דרכים) תציג את שם המסעדה, שם המנה, כמות הפעמים שהיא הוזמנה, והמחיר הכולל שלה עבור המנה שנקנתה הכי הרבה פעמים במסעדה מסויימת
SELECT
    sp.ProviderName,
    m.ItemName,
    COUNT(ol.ReservationID) AS TotalOrders,
    SUM(m.Price) AS TotalPrice
FROM SERVICEPROVIDER sp
JOIN MENUITEM m ON sp.ProviderID = m.ProviderID
JOIN ORDERLINE ol ON m.ItemID = ol.ItemID AND m.ProviderID = ol.ProviderID
WHERE sp.ProviderName = 'Provider1'
GROUP BY sp.ProviderName, m.ItemName
ORDER BY TotalOrders DESC
LIMIT 1;


SELECT
    sp.ProviderName,
    m.ItemName,
    COUNT(ol.ReservationID) AS TotalOrders,
    SUM(m.Price) AS TotalPrice
FROM SERVICEPROVIDER sp
JOIN MENUITEM m ON sp.ProviderID = m.ProviderID
JOIN ORDERLINE ol ON m.ItemID = ol.ItemID AND m.ProviderID = ol.ProviderID
WHERE sp.ProviderName = 'Provider1'
GROUP BY sp.ProviderName, m.ItemName, sp.ProviderID
HAVING COUNT(ol.ReservationID) >= ALL (
    SELECT COUNT(ol2.ReservationID)
    FROM ORDERLINE ol2
    JOIN SERVICEPROVIDER sp2 ON ol2.ProviderID = sp2.ProviderID
    WHERE sp2.ProviderName = 'Provider1'
    GROUP BY ol2.ItemID
);


--5. תציגי את שם התייר, מדינת המוצא ומספר השפות שהוא דובר, רק עבור תיירים שמדברים לפחות 2 שפות ושיש להם הזמנות במערכת
SELECT FirstName, Country, COUNT(tl.Language) AS NumberOfLanguages
FROM TOURIST t
JOIN TOURIST_LANGUAGE tl ON t.TouristID = tl.TouristID
WHERE t.TouristID IN (SELECT r.TouristID FROM RESERVATION r)
GROUP BY t.TouristID, t.FirstName, t.Country
HAVING COUNT(tl.Language) >= 2


--6. תציג את קודי הקופונים, אחוז ההנחה ותאריך הסיום ששייכים למסעדה "Provider2" ולתיירים מארץ "France"
SELECT c.CouponCode, c.DiscountPercent, c.EndDate, sp.ProviderName, td.Country
FROM COUPON c
JOIN SERVICEPROVIDER sp ON c.ProviderID = sp.ProviderID
JOIN INCLUDE i ON c.CouponID = i.CouponID
JOIN TOURISTDISCOUNT td ON i.DiscountID = td.DiscountID
WHERE sp.ProviderName = 'Provider2'
AND td.Country = 'France'


--7. תציג את מספר ההזמנה, שם התייר המזמין, תאריך ההזמנה המלא למסעדת "Provider1", עבור הזמנות שבוצעו ברבעון האחרון של שנת 2025
SELECT ReservationID, ReservationDate, FirstName, ProviderName
FROM RESERVATION r
JOIN TOURIST t ON r.TouristID = t.TouristID
JOIN SERVICEPROVIDER sp ON r.ProviderID = sp.ProviderID
WHERE ProviderName= 'Provider1'
AND EXTRACT(YEAR FROM ReservationDate) = 2025
AND EXTRACT(MONTH FROM ReservationDate) IN (10, 11, 12)


--8. (שתי דרכים) תציג את שם המסעדה, שם המנה והמחיר שלה, עבור מנות שלא מופיעות באף הזמנה
SELECT ProviderName, ItemName, Price
FROM SERVICEPROVIDER sp
JOIN MENUITEM m ON sp.ProviderID=m.ProviderID
WHERE NOT EXISTS (
    SELECT 1
    FROM ORDERLINE ol
    WHERE ol.ItemID = m.ItemID
    AND ol.ProviderID = m.ProviderID)


SELECT sp.ProviderName, m.ItemName, m.Price, m.Category
FROM SERVICEPROVIDER sp
JOIN MENUITEM m ON sp.ProviderID = m.ProviderID
LEFT JOIN ORDERLINE ol ON m.ItemID = ol.ItemID AND m.ProviderID = ol.ProviderID
WHERE ol.ItemID IS NULL;


--UPDATE Query--

--1. העלאת המחיר של כל המנות (ב-10%) השייכות לקטגוריה "Drink", אבל רק במסעדות שנמצאות בעיר ספציפית "Jerusalem"
UPDATE MENUITEM
SET Price = Price * 1.10
WHERE Category = 'Drink'
AND ProviderID IN (
    SELECT ProviderID
    FROM SERVICEPROVIDER
    WHERE City = 'Jerusalem')


SELECT sp.ProviderName, sp.City, m.ItemName, m.Category, m.Price AS PriceAfterUpdate
FROM MENUITEM m
JOIN SERVICEPROVIDER sp ON m.ProviderID = sp.ProviderID
WHERE m.Category = 'Drink'
AND sp.City = 'Jerusalem'
ORDER BY sp.ProviderName ASC;


--2.  עדכון תאריך הסיום של הקופונים ששייכים לתיירים מארץ "USA"
UPDATE COUPON c
SET EndDate = '2026-3-31'
WHERE EXISTS (
    SELECT 1
    FROM ORDERLINE ol
    JOIN RESERVATION r ON ol.ReservationID = r.ReservationID
    JOIN TOURIST t ON r.TouristID = t.TouristID
    WHERE t.Country = 'USA'
      AND ol.ProviderID = c.ProviderID
)


SELECT DISTINCT c.CouponID, c.CouponCode, c.EndDate, t.Country
FROM COUPON c
JOIN ORDERLINE ol ON c.ProviderID = ol.ProviderID
JOIN RESERVATION r ON ol.ReservationID = r.ReservationID
JOIN TOURIST t ON r.TouristID = t.TouristID
WHERE t.Country = 'USA'
ORDER BY c.CouponID ASC;


--3. עדכון "סטטוס" ההזמנה ל-"Cancelled" עבור הזמנות שבהן מספר האנשים גדול מ-5, וההזמנה שייכת (ServiceType) למסעדה מסוג "Hotel"
UPDATE RESERVATION r
SET Status = 'Cancelled'
WHERE r.NumberOfPeople > 5
  AND r.ProviderID IN (
      SELECT sp.ProviderID
      FROM SERVICEPROVIDER sp
      WHERE sp.ServiceType = 'Hotel'
  )


SELECT r.ReservationID, r.NumberOfPeople, r.Status, sp.ServiceType
FROM RESERVATION r
JOIN SERVICEPROVIDER sp ON r.ProviderID = sp.ProviderID
WHERE r.NumberOfPeople > 5
  AND sp.ServiceType = 'Hotel'
ORDER BY reservationid ASC


--DELETE Query--

--1. מחיקת רשומות מטבלת "TOURIST" עבור תיירים שמעולם לא ביצעו הזמנה במערכת
DELETE FROM TOURIST t
WHERE NOT EXISTS (
    SELECT 1
    FROM RESERVATION r
    WHERE r.TouristID = t.TouristID
)


SELECT *
FROM TOURIST t
WHERE NOT EXISTS (
    SELECT 1
    FROM RESERVATION r
    WHERE r.TouristID = t.TouristID
)


--2. מחיקת קופונים מטבלת COUPON שתאריך הסיום שלהם קטן מתאריך ושעת המערכת הנוכחיים
DELETE FROM include
WHERE couponid IN (SELECT couponid FROM coupon WHERE EndDate < CURRENT_DATE);

DELETE FROM coupon
WHERE EndDate < CURRENT_DATE;


SELECT * FROM COUPON
WHERE EndDate < CURRENT_DATE;


--3. מחיקת כל מנות מהתפריט שהמחיר שלהם קטן מ-15, ושייכים למסעדות שנמצאות בחיפה
DELETE FROM orderline
WHERE (itemid, providerid) IN (
    SELECT itemid, providerid
    FROM MENUITEM
    WHERE Price < 15
      AND ProviderID IN (SELECT ProviderID FROM SERVICEPROVIDER WHERE City = 'Haifa')
);

DELETE FROM MENUITEM
WHERE Price < 15
  AND ProviderID IN (
    SELECT ProviderID
    FROM SERVICEPROVIDER
    WHERE City = 'Haifa'
);


SELECT * FROM MENUITEM
WHERE Price < 15
  AND ProviderID IN (
    SELECT ProviderID
    FROM SERVICEPROVIDER
    WHERE City = 'Haifa'
  );
