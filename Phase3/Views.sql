-- A view of our database
המבט מאחד את שלוש הטבלאות הפיזיות של אגף המסעדות (reservation, tourist, restaurant_table)--
ומציג תצוגה אחת מרוכזת וקריאה המקשרת ישירות בין פרטי ההזמנה, השם המלא של התייר ומספר השולחן ששוריין עבורו. --
CREATE OR REPLACE VIEW public.v_restaurant_reservations AS
SELECT 
    r.reservationid AS ReservationID,
    r.reservationdate AS ReservationDate,
    r.status AS Status,
    r.numberofpeople AS NumberOfPeople,
    t.touristid AS TouristID,
    t.firstname || ' ' || t.lastname AS TouristFullName,
    t.country AS Country,
    rt.tableid AS TableID,
    rt.tablenumber AS TableNumber,
    rt.seats AS Seats
FROM public.reservation r
JOIN public.tourist t ON r.touristid = t.touristid
JOIN public.restaurant_table rt ON r.reservationid = rt.reservationid;

-- הוצאת הנתונים למבט הראשון
SELECT * FROM public.v_restaurant_reservations LIMIT 10;

-- שאילתה 1: סינון לפי מדינה, תיירים מ USA
SELECT ReservationID, ReservationDate, TouristFullName, TableNumber, Seats, NumberOfPeople
FROM public.v_restaurant_reservations
WHERE Status = 'Confirmed' AND Country = 'USA'
ORDER BY ReservationDate DESC;

-- שאילתה 2: סטטיסטיקה של סועדים מכל מדינה
SELECT 
    Country,
    COUNT(DISTINCT ReservationID) AS TotalReservations,
    SUM(NumberOfPeople) AS TotalGuests
FROM public.v_restaurant_reservations
GROUP BY Country
ORDER BY TotalReservations DESC;



-- A view at the database we received
המבט מאחד את טבלת שריון האטרקציות (reservedattraction) עם טבלת האטרקציות הכללית (attraction) --
 כדי להציג תצוגה מרוכזת וקריאה של שמות המקומות, המיקומים והמחירים עבור כל מספר הזמנה. --
CREATE OR REPLACE VIEW public.v_attraction_bookings AS
SELECT 
    ra.reservation_id AS ReservationID,
    ra.attraction_id AS AttractionID,
    a.attraction_name AS AttractionName,
    a.attraction_location AS AttractionLocation,
    a.attraction_price AS AttractionPrice
FROM public.reservedattraction ra
JOIN public.attraction a ON ra.attraction_id = a.attraction_id;

-- הוצאת הנתונים למבט השני
SELECT * FROM public.v_attraction_bookings LIMIT 10;


-- שאילתה 1 (סינון לפי מיקום): שליפת כל האטרקציות שהוזמנו ונמצאות במיקום מסוים
SELECT ReservationID, AttractionName, AttractionPrice
FROM public.v_attraction_bookings
WHERE AttractionLocation = 'North Nathan';


-- שאילתה 2 (סטטיסטיקה): ספירה כמה פעמים כל אטרקציה הוזמנה, כדי לדעת מה האטרקציה הכי מבוקשת.
SELECT 
    AttractionName,
    COUNT(ReservationID) AS TotalBookings
FROM public.v_attraction_bookings
GROUP BY AttractionName
ORDER BY TotalBookings DESC;