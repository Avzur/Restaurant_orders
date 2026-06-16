CREATE OR REPLACE PROCEDURE public.pr_update_provider_coupon_status(
    p_provider_id INT,
    p_new_status CHARACTER(1)
) AS $$
BEGIN
    -- בדיקת תקינות הקלט (הסתעפות ותנאי)
    IF p_new_status NOT IN ('A', 'U', 'E') THEN
        RAISE EXCEPTION 'Invalid status: %. Status must be A (Active), U (Used), or E (Expired).', p_new_status;
    END IF;

    -- פקודת עדכון DML מרוכזת
    UPDATE public.coupon
    SET status = p_new_status
    WHERE providerid = p_provider_id;

    RAISE NOTICE 'Successfully updated coupons for provider % to status %.', p_provider_id, p_new_status;

EXCEPTION
    -- תפיסת חריגות וטיפול בשגיאות
    WHEN OTHERS THEN
        RAISE NOTICE 'An error occurred in pr_update_provider_coupon_status: %', SQLERRM;
        RAISE; -- זריקת השגיאה החוצה למסך כדי שהמשתמש יראה אותה
END;
$$ LANGUAGE plpgsql;

--בדיקה--
CALL public.pr_update_provider_coupon_status(403, 'A');

-- בדיקת חריגה--
CALL public.pr_update_provider_coupon_status(403, 'Z');