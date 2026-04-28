-- =========================
-- ROLLBACK EXAMPLE
-- =========================

BEGIN;

-- בדיקה לפני
SELECT *
FROM MENUITEM
WHERE Category = 'Drink'
LIMIT 5;

-- עדכון
UPDATE MENUITEM
SET Price = Price + 5
WHERE Category = 'Drink';

-- בדיקה אחרי עדכון
SELECT *
FROM MENUITEM
WHERE Category = 'Drink'
LIMIT 5;

-- ביטול
ROLLBACK;

-- בדיקה אחרי rollback (אמור לחזור למצב קודם)
SELECT *
FROM MENUITEM
WHERE Category = 'Drink'
LIMIT 5;

-- =========================
-- COMMIT EXAMPLE
-- =========================

BEGIN;

-- בדיקה לפני
SELECT *
FROM RESERVATION
WHERE NumberOfPeople > 5
LIMIT 5;

-- עדכון
UPDATE RESERVATION
SET Status = 'Cancelled'
WHERE NumberOfPeople > 5;

-- בדיקה אחרי עדכון
SELECT *
FROM RESERVATION
WHERE NumberOfPeople > 5
LIMIT 5;

-- שמירה
COMMIT;

-- בדיקה אחרי commit (השינוי נשאר)
SELECT *
FROM RESERVATION
WHERE NumberOfPeople > 5
LIMIT 5;