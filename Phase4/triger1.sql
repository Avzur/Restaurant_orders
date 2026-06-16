-- א. יצירת פונקציית הטריגר
CREATE OR REPLACE FUNCTION public.fn_trg_check_coupon_expiry()
RETURNS TRIGGER AS $$
BEGIN
    -- בדיקה האם הסטטוס משתנה ל-'A' והאם התאריך הנוכחי עבר את תאריך התפוגה
    IF NEW.status = 'A' AND NEW.enddate < CURRENT_DATE THEN
        RAISE EXCEPTION 'Cannot activate coupon %. The expiration date (%) has already passed.',
            NEW.couponid, NEW.enddate;
    END IF;

    RETURN NEW; -- מאשר את העדכון אם הכל תקין
END;
$$ LANGUAGE plpgsql;

-- ב. הצמדת הטריגר לטבלת coupon לזמן UPDATE
CREATE OR REPLACE TRIGGER trg_check_coupon_expiry
BEFORE UPDATE ON public.coupon
FOR EACH ROW
EXECUTE FUNCTION public.fn_trg_check_coupon_expiry();

--בדיקה--
UPDATE public.coupon
SET status = 'A', enddate = '2020-01-01'
WHERE couponid = 1;