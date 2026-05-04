-- =========================================
-- CONSTRAINTS
-- =========================================

--1
--האילוץ קובע שאי אפשר להכניס להזמנה יותר מ-20 אנשים, והוא חוסם אוטומטית כל רישום של מספר גבוה יותר
ALTER TABLE RESERVATION
ADD CONSTRAINT max_people_check
CHECK (NumberOfPeople <= 20);

--2
האילוץ מוודא שמספרי הטלפון בטבלה יהיו באורך תקין, והוא חוסם הכנסה של מספרים קצרים מדי (כמו 050995)
ALTER TABLE SERVICEPROVIDER
ADD CONSTRAINT phone_length_check
CHECK (Phone >= 100000000);

--3
--האילוץ על עמודת תאריך הסיום הופך אותה לשדה חובה, והוא מונע מצב שבו מכניסים קופון למערכת בלי לציין מתי הוא מסתיים
ALTER TABLE COUPON
ALTER COLUMN EndDate SET NOT NULL;


-- =========================================
-- בדיקות (לדו"ח)
-- =========================================

--1
INSERT INTO RESERVATION VALUES (99999, '2025-01-01', 25, 'Pending', 1, 1);

--2
INSERT INTO SERVICEPROVIDER VALUES (9999, 'Test', 'Cafe', 123, 'Addr', 'Tel Aviv');

--3
INSERT INTO COUPON VALUES (9999, 'TEST999', 10, '2025-01-01', NULL, 1);