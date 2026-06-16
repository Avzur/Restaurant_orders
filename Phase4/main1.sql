DO $$
DECLARE
    v_total_spending NUMERIC;
BEGIN
    -- קריאה לפונקציה
    v_total_spending := public.fn_get_tourist_spending(1);

    RAISE NOTICE 'Total tourist spending: %', v_total_spending;

    -- קריאה לפרוצדורה
    CALL public.pr_optimize_reservation_people();

    RAISE NOTICE 'Main Program 1 completed successfully.';

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Error in Main Program 1: %', SQLERRM;
END;
$$;