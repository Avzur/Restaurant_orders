-- =========================
-- ROLLBACK EXAMPLE
-- =========================

BEGIN;

SELECT r.ReservationID, r.Status, r.NumberOfPeople
FROM RESERVATION r
JOIN SERVICEPROVIDER sp ON r.ProviderID = sp.ProviderID
WHERE sp.ProviderName = 'Provider1'
LIMIT 10;

UPDATE RESERVATION
SET Status = 'Cancelled'
WHERE ProviderID IN (
    SELECT ProviderID
    FROM SERVICEPROVIDER
    WHERE ProviderName = 'Provider1'
);

SELECT r.ReservationID, r.Status, r.NumberOfPeople
FROM RESERVATION r
JOIN SERVICEPROVIDER sp ON r.ProviderID = sp.ProviderID
WHERE sp.ProviderName = 'Provider1'
LIMIT 10;

ROLLBACK;

SELECT r.ReservationID, r.Status, r.NumberOfPeople
FROM RESERVATION r
JOIN SERVICEPROVIDER sp ON r.ProviderID = sp.ProviderID
WHERE sp.ProviderName = 'Provider1'
LIMIT 10;


-- =========================
-- COMMIT EXAMPLE
-- =========================

BEGIN;

SELECT ReservationID, NumberOfPeople, Status
FROM RESERVATION
WHERE NumberOfPeople > 10
LIMIT 10;

UPDATE RESERVATION
SET Status = 'Cancelled'
WHERE NumberOfPeople > 10
AND Status = 'Pending';

SELECT ReservationID, NumberOfPeople, Status
FROM RESERVATION
WHERE NumberOfPeople > 10
LIMIT 10;

COMMIT;

SELECT ReservationID, NumberOfPeople, Status
FROM RESERVATION
WHERE NumberOfPeople > 10
LIMIT 10;