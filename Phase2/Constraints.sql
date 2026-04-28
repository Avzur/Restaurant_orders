-- =========================================
-- CONSTRAINTS
-- =========================================

ALTER TABLE RESERVATION
ADD CONSTRAINT max_people_check
CHECK (NumberOfPeople <= 20);


ALTER TABLE SERVICEPROVIDER
ADD CONSTRAINT phone_length_check
CHECK (Phone >= 100000000);


ALTER TABLE COUPON
ALTER COLUMN EndDate SET NOT NULL;


-- =========================================
-- בדיקות (לדו"ח)
-- =========================================

INSERT INTO RESERVATION VALUES (99999, '2025-01-01', 25, 'Pending', 1, 1);


INSERT INTO SERVICEPROVIDER VALUES (9999, 'Test', 'Cafe', 123, 'Addr', 'Tel Aviv');


INSERT INTO COUPON VALUES (9999, 'TEST999', 10, '2025-01-01', NULL, 1);