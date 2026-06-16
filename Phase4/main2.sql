DO $$
DECLARE
    v_coupon_count INT;
BEGIN
    -- קריאה לפונקציה
    v_coupon_count := public.fn_get_provider_coupon_count(403);

    RAISE NOTICE 'Provider 403 currently has % coupons.', v_coupon_count;

    -- קריאה לפרוצדורה
    CALL public.pr_update_provider_coupon_status(403, 'A');

    RAISE NOTICE 'Main Program 2 completed successfully.';

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Error in Main Program 2: %', SQLERRM;
END;
$$;