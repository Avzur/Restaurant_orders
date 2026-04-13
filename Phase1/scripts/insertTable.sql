-- ========================
-- SERVICEPROVIDER
-- ========================
INSERT INTO SERVICEPROVIDER VALUES
(1,'Provider1','Restaurant',501111111,'Street 1','Tel Aviv'),
(2,'Provider2','Cafe',502222222,'Street 2','Haifa'),
(3,'Provider3','Hotel',503333333,'Street 3','Jerusalem'),
(4,'Provider4','Restaurant',504444444,'Street 4','Eilat'),
(5,'Provider5','Cafe',505555555,'Street 5','Ashdod');

-- ========================
-- TOURIST
-- ========================
INSERT INTO TOURIST VALUES
(1,'Noa','Levi',501234567,'noa1@mail.com','Israel','pass1'),
(2,'Dana','Cohen',502345678,'dana2@mail.com','Israel','pass2'),
(3,'Yael','Mizrahi',503456789,'yael3@mail.com','USA','pass3'),
(4,'Omer','Katz',504567890,'omer4@mail.com','France','pass4'),
(5,'Lior','David',505678901,'lior5@mail.com','Germany','pass5'),
(6,'Eden','Bar',506111111,'eden6@mail.com','Israel','pass6'),
(7,'Tal','Sharon',507222222,'tal7@mail.com','Italy','pass7'),
(8,'Gal','Mor',508333333,'gal8@mail.com','Spain','pass8'),
(9,'Niv','Harel',509444444,'niv9@mail.com','Israel','pass9'),
(10,'Ron','Ziv',501555555,'ron10@mail.com','UK','pass10');

-- ========================
-- RESERVATION
-- ========================
INSERT INTO RESERVATION VALUES
(1,'2025-01-01',2,'Confirmed',1,1),
(2,'2025-01-02',4,'Pending',2,2),
(3,'2025-01-03',3,'Cancelled',3,3),
(4,'2025-01-04',5,'Confirmed',4,4),
(5,'2025-01-05',2,'Confirmed',5,5),
(6,'2025-01-06',6,'Pending',1,6),
(7,'2025-01-07',3,'Confirmed',2,7),
(8,'2025-01-08',4,'Cancelled',3,8),
(9,'2025-01-09',2,'Confirmed',4,9),
(10,'2025-01-10',5,'Pending',5,10);

-- ========================
-- MENUITEM
-- ========================
INSERT INTO MENUITEM VALUES
(1,'Burger',50,'Food',1),
(2,'Pizza',60,'Food',1),
(3,'Salad',40,'Food',1),
(4,'Coffee',15,'Drink',2),
(5,'Tea',10,'Drink',2),
(6,'Juice',12,'Drink',2),
(7,'Steak',120,'Food',3),
(8,'Fish',100,'Food',3);

-- ========================
-- ORDERLINE
-- ========================
INSERT INTO ORDERLINE VALUES
(1,1,1),
(2,1,1),
(4,2,2),
(5,2,2),
(7,3,3),
(8,3,3);

-- ========================
-- COUPON
-- ========================
INSERT INTO COUPON VALUES
(1,'DISC10',10,'2025-01-01','2025-12-31',1),
(2,'DISC20',20,'2025-01-01','2025-06-30',2),
(3,'DISC15',15,'2025-02-01','2025-07-01',3);

-- ========================
-- TOURISTDISCOUNT
-- ========================
INSERT INTO TOURISTDISCOUNT VALUES
('Israel',5,1),
('USA',10,2),
('France',7,3);

-- ========================
-- INCLUDE
-- ========================
INSERT INTO INCLUDE VALUES
(1,1),
(2,2),
(3,3);

-- ========================
-- RESTAURANT_TABLE
-- ========================
INSERT INTO RESTAURANT_TABLE VALUES
(1,4,1,1,1),
(2,2,2,2,2),
(3,6,3,3,3),
(4,4,4,4,4),
(5,2,5,5,5);

-- ========================
-- TOURIST_LANGUAGE
-- ========================
INSERT INTO TOURIST_LANGUAGE VALUES
('Hebrew',1),
('English',1),
('English',2),
('French',3),
('German',4),
('Hebrew',5);