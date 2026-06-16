-- א. יצירת פונקציית הטריגר
CREATE OR REPLACE FUNCTION public.fn_trg_limit_reservation_people()
RETURNS TRIGGER AS $$
BEGIN
    -- בדיקה האם כמות האנשים חורגת מהנורמה
    IF NEW.numberofpeople > 30 THEN
        RAISE EXCEPTION 'Reservation rejected. Group size (%) exceeds the maximum allowed capacity of 30 people.',
            NEW.numberofpeople;
    END IF;

    RETURN NEW; -- מאשר את ההכנסה אם הכל תקין
END;
$$ LANGUAGE plpgsql;

-- ב. הצמדת הטריגר לטבלת reservation לזמן INSERT
CREATE OR REPLACE TRIGGER trg_limit_reservation_people
BEFORE INSERT ON public.reservation
FOR EACH ROW
EXECUTE FUNCTION public.fn_trg_limit_reservation_people();

--בדיקה--
INSERT INTO public.reservation (reservationid, touristid, numberofpeople, status)
VALUES (99999, 1, 100, 'Confirmed');