CREATE OR REPLACE PROCEDURE public.pr_optimize_reservation_people() AS $$
DECLARE
    v_res_rec RECORD; -- שימוש ברשומה (Record) כפי שנדרש
BEGIN
    -- לולאה שעוברת על כל ההזמנות שבהן יש רק אדם אחד
    FOR v_res_rec IN 
        SELECT reservationid 
        FROM public.reservation 
        WHERE numberofpeople = 1
    LOOP
        -- ביצוע עדכון DML עבור כל שורה שנמצאה
        UPDATE public.reservation
        SET numberofpeople = 2
        WHERE reservationid = v_res_rec.reservationid;
    END LOOP;
    
    -- הדפסת הודעת הצלחה בחלון ה-Messages
    RAISE NOTICE 'Reservation optimization completed successfully.';
END;
$$ LANGUAGE plpgsql;