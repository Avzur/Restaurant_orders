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



----------------------------------

SELECT MAX(couponid) FROM public.coupon1;


-- 1. הסרת אילוצי מפתח זר הישנים מהטבלאות המקושרות כדי שנוכל לשנות את ה-IDs
ALTER TABLE public.customercoupon
DROP CONSTRAINT IF EXISTS customercoupon_coupon_id_fkey;

ALTER TABLE public.attractioncoupon
DROP CONSTRAINT IF EXISTS attractioncoupon_coupon_id_fkey;



-- 2. עדכון המפתחות הזרים בטבלאות המקושרות (הוספת 10000 למניעת התנגשות)
UPDATE public.customercoupon
SET coupon_id = coupon_id + 500;

UPDATE public.attractioncoupon
SET coupon_id = coupon_id + 500;



INSERT INTO public.coupon1 (couponid, couponcode, discountpercent, startdate, enddate, providerid, status)
SELECT
    coupon_id + 500,                            -- מפתח ראשי חדש ורץ ללא התנגשויות
    coupon_code,                                  -- קוד הקופון
    coupon_discount_percent,                      -- אחוז ההנחה
    '2026-01-01'::date,                           -- ברירת מחדל לתאריך התחלה (כי אין בטבלת המקור)
    coupon_expiry_date,                           -- תאריך תוקף
    158,                                          -- providerid ברירת מחדל זמנית להתאמה למבנה
    CASE
        WHEN coupon_status = 'Active' THEN 'A'    -- התאמה לתו בודד (character 1) בטבלת היעד
        WHEN coupon_status = 'Used' THEN 'U'
        ELSE 'E'
    END
FROM public.coupon
ON CONFLICT (couponid) DO NOTHING;


ALTER TABLE public.customercoupon
ADD CONSTRAINT customercoupon_coupon1_id_fkey
FOREIGN KEY (coupon_id) REFERENCES public.coupon1(couponid);

ALTER TABLE public.attractioncoupon
ADD CONSTRAINT attractioncoupon_coupon1_id_fkey
FOREIGN KEY (coupon_id) REFERENCES public.coupon1(couponid);

DROP TABLE public.coupon;

-- 3. שינוי שם הטבלה המאוחדת לשם הנקי והסופי
ALTER TABLE public.coupon1
RENAME TO coupon;






