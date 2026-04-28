-- =========================================
-- CONSTRAINTS
-- =========================================

-- 1. מספר אנשים מקסימלי להזמנה
ALTER TABLE RESERVATION
ADD CONSTRAINT max_people_check
CHECK (NumberOfPeople <= 20);


-- =========================================

-- 2. מספר טלפון חייב להיות 9 ספרות לפחות
ALTER TABLE SERVICEPROVIDER
ADD CONSTRAINT phone_length_check
CHECK (Phone >= 100000000);


-- =========================================

-- 3. תאריך סיום קופון לא יכול להיות NULL
ALTER TABLE COUPON
ALTER COLUMN EndDate SET NOT NULL;


-- =========================================
-- בדיקות (לדו"ח)
-- =========================================

-- ❌ אמור להיכשל (יותר מדי אנשים)
INSERT INTO RESERVATION VALUES (99999, '2025-01-01', 25, 'Pending', 1, 1);


-- ❌ אמור להיכשל (טלפון קצר מדי)
INSERT INTO SERVICEPROVIDER VALUES (9999, 'Test', 'Cafe', 123, 'Addr', 'Tel Aviv');


-- ❌ אמור להיכשל (EndDate NULL)
INSERT INTO COUPON VALUES (9999, 'TEST999', 10, '2025-01-01', NULL, 1);