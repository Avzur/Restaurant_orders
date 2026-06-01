SELECT MAX(reservationid) FROM public.reservation1;

BEGIN;

-- 1. מחיקת האילוץ הישן אם הוא קיים
ALTER TABLE public.reservedattraction 
DROP CONSTRAINT IF EXISTS reservedattraction_reservation_id_fkey;

-- 2. העתקת הנתונים עם תרגום הסטטוס Approved -> Confirmed
INSERT INTO public.reservation1 (reservationid, reservationdate, numberofpeople, status, providerid, touristid)
SELECT 
    reservation_id,       
    reservation_date,     
    1,                    
    CASE 
        WHEN reservation_status = 'Approved' THEN 'Confirmed'
        ELSE reservation_status 
    END,                  -- מתרגם Approved ל-Confirmed כדי לעבור את ה-Check Constraint
    1,                    
    1                     
FROM public.reservation
ON CONFLICT (reservationid) DO NOTHING;

-- 3. קישור האילוץ מחדש לטבלה המאוחדת reservation1
ALTER TABLE public.reservedattraction
ADD CONSTRAINT reservedattraction_reservation1_id_fkey 
FOREIGN KEY (reservation_id) REFERENCES public.reservation1(reservationid);

COMMIT;


BEGIN;
SELECT setval(pg_get_serial_sequence('public.reservation1', 'reservationid'), COALESCE(MAX(reservationid), 1)) 
FROM public.reservation1;

DROP TABLE public.reservation;
COMMIT;


ALTER TABLE public.reservation1 
RENAME TO reservation;




