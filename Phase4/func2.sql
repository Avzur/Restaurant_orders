CREATE OR REPLACE FUNCTION public.fn_get_provider_coupon_count(p_provider_id INT)
RETURNS INT AS $$
DECLARE
    v_rec RECORD;          -- משתנה רשומה
    v_counter INT := 0;    -- מונה קופונים
BEGIN
    -- שימוש בלולאת FOR מעל סמן מרומז (Implicit Cursor) שמביא את קופוני הספק
    FOR v_rec IN 
        SELECT couponid 
        FROM public.coupon 
        WHERE providerid = p_provider_id
    LOOP
        -- על כל קופון שנמצא בלולאה, נקדם את המונה ב-1
        v_counter := v_counter + 1;
    END LOOP;

    -- החזרת התוצאה הסופית
    RETURN v_counter;
END;
$$ LANGUAGE plpgsql;

