-- =========================
-- ROLLBACK EXAMPLE
-- =========================

BEGIN;

-- בדיקה לפני שינוי: הזמנות למסעדת Provider1
SELECT r.ReservationID, r.Status, r.NumberOfPeople
FROM RESERVATION r
JOIN SERVICEPROVIDER sp ON r.ProviderID = sp.ProviderID
WHERE sp.ProviderName = 'Provider1'
LIMIT 10;

-- עדכון זמני: סימון הזמנות למסעדה כ-Confirmed → Cancelled
UPDATE RESERVATION
SET Status = 'Cancelled'
WHERE ProviderID IN (
    SELECT ProviderID
    FROM SERVICEPROVIDER
    WHERE ProviderName = 'Provider1'
);

-- בדיקה אחרי עדכון
SELECT r.ReservationID, r.Status, r.NumberOfPeople
FROM RESERVATION r
JOIN SERVICEPROVIDER sp ON r.ProviderID = sp.ProviderID
WHERE sp.ProviderName = 'Provider1'
LIMIT 10;

-- ביטול כל השינויים
ROLLBACK;

-- בדיקה אחרי rollback (אמור לחזור למצב המקורי)
SELECT r.ReservationID, r.Status, r.NumberOfPeople
FROM RESERVATION r
JOIN SERVICEPROVIDER sp ON r.ProviderID = sp.ProviderID
WHERE sp.ProviderName = 'Provider1'
LIMIT 10;


-- =========================
-- COMMIT EXAMPLE
-- =========================

BEGIN;

-- בדיקה לפני שינוי: הזמנות גדולות במיוחד
SELECT ReservationID, NumberOfPeople, Status
FROM RESERVATION
WHERE NumberOfPeople > 10
LIMIT 10;

-- עדכון קבוע: ביטול הזמנות גדולות מדי (עסקי)
UPDATE RESERVATION
SET Status = 'Cancelled'
WHERE NumberOfPeople > 10
AND Status = 'Pending';

-- בדיקה אחרי עדכון
SELECT ReservationID, NumberOfPeople, Status
FROM RESERVATION
WHERE NumberOfPeople > 10
LIMIT 10;

-- שמירת השינויים
COMMIT;

-- בדיקה אחרי commit (השינוי נשאר קבוע)
SELECT ReservationID, NumberOfPeople, Status
FROM RESERVATION
WHERE NumberOfPeople > 10
LIMIT 10;