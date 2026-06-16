CREATE OR REPLACE FUNCTION public.fn_get_tourist_spending(p_tourist_id INT)
RETURNS NUMERIC AS $$
DECLARE
    -- 1. הגדרת סמן מפורש (Explicit Cursor)
    cur_attractions CURSOR FOR 
        SELECT a.attraction_price 
        FROM public.reservation r
        JOIN public.reservedattraction ra ON r.reservationid = ra.reservation_id
        JOIN public.attraction a ON ra.attraction_id = a.attraction_id
        WHERE r.touristid = p_tourist_id;
        
    v_price NUMERIC;
    v_total_spending NUMERIC := 0;
    v_tourist_exists INT;
BEGIN
    -- 2. בדיקה האם התייר קיים במערכת
    SELECT COUNT(*) INTO v_tourist_exists FROM public.tourist WHERE touristid = p_tourist_id;
    
    -- אם התייר לא קיים, נזרוק שגיאה רשמית (זה ייצר חריגה מסוג USER_RAISED_EXCEPTION)
    IF v_tourist_exists = 0 THEN
        RAISE EXCEPTION 'Tourist with ID % does not exist in the system.', p_tourist_id;
    END IF;

    -- 3. שימוש בלולאה מעל הסמן המפורש
    OPEN cur_attractions;
    LOOP
        FETCH cur_attractions INTO v_price;
        EXIT WHEN NOT FOUND;
        v_total_spending := v_total_spending + COALESCE(v_price, 0);
    END LOOP;
    CLOSE cur_attractions;

    RETURN v_total_spending;

EXCEPTION
    -- תופס רק שגיאות לא צפויות אחרות, אבל נותן לשגיאה שלנו לפרוץ החוצה למסך!
    WHEN OTHERS THEN
        IF SQLSTATE = 'P0001' THEN 
            RAISE; -- זורק את השגיאה המתוכנתת החוצה כדי שהמשתמש יראה אותה
        END IF;
        RETURN 0;
END;
$$ LANGUAGE plpgsql;