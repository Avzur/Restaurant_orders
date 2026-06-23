# Restaurant_orders
Avishag Ben Zur and Ayala Ovadya
<br><br>
Selected system: Tourist services - restaurant reservations
## Table of Contents
* [Phase 1: Design and Build the Database](#phase-1-design-and-build-the-database)
  * [Introduction - Screenshots](#introduction---screenshots)
  * [ERD (Entity-Relationship Diagram)](#erd-entity-relationship-diagram)
  * [DSD (Data Structure Diagram)](#dsd-data-structure-diagram)
  * [SQL Scripts](#sql-scripts)
  * [Data](#data)
  * [Python code](#Python-code)
  * [Backup1](#backup1)
* [Phase 2: Queries and constraints](#Phase-2-Queries-and-constraints)
  * [select queries](#select-queries)
  * [update queries](#update-queries)
  * [delete queries](#delete-queries)
  * [Constraints](#Constraints)
  * [RollbackCommit](#RollbackCommit)
  * [Index](#Index)
  * [backup2](#backup2)
* [Phase 3: Integration and Views](#Phase-3-Integration-and-Views)
  * [The new ERD](#The-new-ERD)
  * [The new DSD](#The-new-DSD)
  * [Integration Steps Summary](#Integration-Steps-Summary)
  * [ERD of the integration](#ERD-of-the-integration)
  * [DSD after integration](#DSD-after-integration)
  * [reverse engineering](#reverse-engineering)
  * [Alter and create table commands in the integration file](#Alter-and-create-table-commands-in-the-integration-file)
  * [Commands for creating views and queries on views in the Views file](#Commands-for-creating-views-and-queries-on-views-in-the-Views-file)
  * [backup3](#backup3)
* [Phase 4: PL/pgSQL programs](#Phase-4-PL-pgSQL-programs)
  * [Functions](#Functions)
  * [Procedures](#Procedures)
  * [Triggers](#Triggers)
  * [Main programs](#Main-programs)
* [Phase 5: Graphical interface](#Graphical-interface)
## Phase 1: Design and Build the Database

### Introduction - Screenshots
**DineReserve** system is designed to bridge the gap between tourists and local restaurants. The system allows for dynamic management of table availability, consideration of tourists' culinary preferences, and order history management.

**Main data stored in the system:**
* **Tourists:** Contact details, preferred language and cultural preferences.
* **Restaurants:** Location, type of cuisine, operating hours.
* **Tables:** Capacity and availability status.
* **Reservations:** Link between a tourist, a table in a restaurant and a specific time.

**Main functionality:**
* Making a reservation in real time with immediate confirmation.
* Table inventory management for the restaurant owner.
* Obtaining statistics on tourists for the restaurant owner

**Website link:**
https://ai.studio/apps/b2cd3651-0d95-4ace-9c3d-26c037da6b7d

#### System registration side
<img width="1795" height="942" alt="הרשמה" src="https://github.com/user-attachments/assets/4fe0ed70-f6b3-4c7d-aee2-4744103a5963" />
<br><br>

#### Restaurant owner's side
<img width="1892" height="897" alt="צד מנהל1" src="https://github.com/user-attachments/assets/8ee455eb-958d-4ec9-8770-eb3707c5180a" />
<br><br>
<img width="1887" height="918" alt="צד מנהל2" src="https://github.com/user-attachments/assets/1365e704-30fd-4511-bea6-ef8ffb35e169" />
<br><br>
<img width="1886" height="927" alt="צד מנהל3" src="https://github.com/user-attachments/assets/24802d85-200d-4123-83de-65e6a288e8d1" />
<br><br>
<img width="1882" height="921" alt="צד מנהל4" src="https://github.com/user-attachments/assets/dcc009ca-cceb-4a2e-ab5a-4a440978f61d" />
<br><br>

#### Tourist side
<img width="1888" height="921" alt="צד תייר1" src="https://github.com/user-attachments/assets/28806395-35c3-4c36-9956-67f0777545c8" />
<br><br>
<img width="1878" height="910" alt="צד תייר3" src="https://github.com/user-attachments/assets/64ffa33a-ef3e-4250-86f7-c0e5af62f01e" />
<br><br>
<img width="1905" height="917" alt="צד תייר2" src="https://github.com/user-attachments/assets/e31bb39e-04f6-4d67-a69c-d77907bd1d68" />
<br><br>

### ERD (Entity-Relationship Diagram)]
<img width="4512" height="2085" alt="ERD" src="https://github.com/user-attachments/assets/ce5cf7b5-ec12-465f-8601-41c1780b8389" />
<br><br>

### DSD (Data Structure Diagram)]
<img width="4512" height="2085" alt="DSD1" src="https://github.com/user-attachments/assets/97371415-8765-480d-89e0-43860298848c" />
<br><br>
<img width="1257" height="931" alt="DSD2" src="https://github.com/user-attachments/assets/b3ccce7d-bb23-4a06-8490-18be018c3579" />
<br><br>

### SQL Scripts

* **Create Tables Script** - The SQL script for creating the database tables is available in the repository:

  📜 [View `create_tables.sql`](Phase1/scripts/createtables.sql)

* **Insert Data Script** - The SQL script for insert data to the database tables is available in the repository:

  📜 [View `insertTable.sql`](Phase1/scripts/insertTable.sql)

* **Drop Tables Script** - The SQL script for droping all tables is available in the repository:

  📜 [View `dropTables.sql`](Phase1/scripts/dropTables.sql)

* **Select All Data Script** - The SQL script for selectAll tables is available in the repository:

  📜 [View `selectAll.sql`](Phase1/scripts/selectAll.sql)

### Data

using [mockaro](https://www.mockaroo.com/) to create csv files

Entering a data to RESERVATION table

* 📜 [View `RESERVATION_MOCK_DATA.csv`](Phase1/mockData/RESERVATION_MOCK_DATA.csv)

Entering a data to SERVICEPROVIDER table

* 📜 [View `SERVICEPROVIDER_MOCK_DATA.csv`](Phase1/mockData/SERVICEPROVIDER_MOCK_DATA.csv)

Entering a data to TOURISTDISCOUNT table

* 📜 [View `TOURISTDISCOUNT_MOCK_DATA.csv`](Phase1/mockData/TOURISTDISCOUNT_MOCK_DATA.csv)

Example of entering data in the SERVICEPROVIDER table:
<img width="1862" height="718" alt="SERVICEPROVIDER" src="https://github.com/user-attachments/assets/8cca9da7-0c48-4fdd-88ff-367b0dbda230" />
<br><br>
<img width="870" height="687" alt="צילום מסך 2026-04-14 121427" src="https://github.com/user-attachments/assets/538756a5-4d6f-48a2-9f95-43f294ac7e47" />
<br><br>
<img width="873" height="502" alt="צילום מסך 2026-04-14 122340" src="https://github.com/user-attachments/assets/e3f73d15-55cd-4b0a-888c-cb56cfb2c5c4" />
<br><br>
<img width="500" height="468" alt="צילום מסך 2026-04-20 025323" src="https://github.com/user-attachments/assets/7ef40bf2-25ba-4ad1-95ce-15d2564680ed" />
<br><br>

### Python code

* 📜 [View `/generate_data.py`](Phase1/generate_data/generate_data.py)
<img width="1014" height="912" alt="image (1)" src="https://github.com/user-attachments/assets/a9564bce-b0c0-40a1-83ed-fe5b34cec478" />
<br><br>
<img width="1073" height="1010" alt="image (3)" src="https://github.com/user-attachments/assets/ed9fc3d3-b1ee-4093-904d-32dca9eea477" />
<br><br>
<img width="951" height="1253" alt="image (4)" src="https://github.com/user-attachments/assets/fd07ee1d-1049-4488-aa29-ef3f2b365cd9" />
<br><br>

### backup1

backups files are kept with the date and hour of the backup:
* 📜 [View `backup.backup-19_4_26`](Phase1/backup/backup.backup-19_4_26)
<img width="1691" height="748" alt="image" src="https://github.com/user-attachments/assets/97bf4be2-4b1f-41fb-881e-8d4747fbff0b" />
<br><br>
<img width="606" height="360" alt="צילום מסך 2026-04-19 2109g09" src="https://github.com/user-attachments/assets/2dc6be70-1f18-4106-bad8-2bc9caf98128" />
<br><br>
<br><br>


## Phase 2: Queries and constraints

### select queries

**1.** (שתי דרכים) תציג את שם התייר, שם המשפחה, מדינת המוצא שלו – עבור תיירים שעשו הזמנה בחודש ינואר בשנת 2026
<img width="672" height="272" alt="שאילתה11" src="https://github.com/user-attachments/assets/d5dbbfc8-6be6-4251-b4da-2f08b22fd4b2" />
<br><br>
<img width="616" height="62" alt="11" src="https://github.com/user-attachments/assets/51e9d946-ed0c-40d5-8493-be86260392d6" />
<br><br>
<img width="657" height="236" alt="שאילתה12" src="https://github.com/user-attachments/assets/06fb7b10-3a62-4940-8054-8c757a0d577b" />
<br><br>
<img width="622" height="57" alt="12" src="https://github.com/user-attachments/assets/08b5e998-5678-43c3-8413-dc5e8fc314d9" />
<br><br>
<img width="1027" height="293" alt="ש1" src="https://github.com/user-attachments/assets/84e8d180-4b43-43db-ae0c-4333b027de28" />
<br><br>
ההבדל הלוגי: תת-שאילתה עם IN רק בודקת קיום ולא מייצרת כפילויות. לעומתה, JOIN משכפל את שורת התייר עבור כל הזמנה שעשה, מה שמחייב שימוש ב-DISTINCT כדי למחוק את הכפולות.

יעילות: שיטת ה-IN יעילה יותר. היא חוסכת מראש למערכת את כוח העיבוד המיותר שנדרש כדי ליצור כפילויות בזיכרון ואז לסנן אותן
<br><br>

**2.** (שתי דרכים) תציג את שם התייר, כתובת המסעדה, עיר המסעדה ושם המסעדה שעבורה תייר בשם "First80" ביצע הזמנה
<img width="707" height="191" alt="שאילתה21" src="https://github.com/user-attachments/assets/7f36fa90-0175-4d49-945c-08c4106aa10a" />
<br><br>
<img width="608" height="61" alt="21" src="https://github.com/user-attachments/assets/e098caf2-d74c-488f-971f-d0d503d7a067" />
<br><br>
<img width="667" height="211" alt="שאילתה22" src="https://github.com/user-attachments/assets/7528fe87-f741-4385-82a2-e7b0b302bbca" />
<br><br>
<img width="626" height="68" alt="22" src="https://github.com/user-attachments/assets/938e374e-a81c-410c-b1df-57913fec15bc" />
<br><br>
<img width="1032" height="292" alt="ש2" src="https://github.com/user-attachments/assets/725c4f39-b980-4eb3-abe1-c76cc5e753c1" />
<br><br>
ההבדל הלוגי: הבדל של סדר ותחביר בלבד. הצורה הראשונה (JOIN מפורש) מפרידה בצורה מסודרת בין תנאי החיבור של הטבלאות (ON) לבין סינון הנתונים (WHERE). הצורה השנייה מערבבת את שניהם יחד בתוך ה-WHERE.

יעילות: אין שום הבדל ביעילות. מנוע בסיס הנתונים מזהה ששתי השאילתות מבקשות את אותה הפעולה, ובונה עבורן בדיוק את אותה תוכנית הרצה. לכן, זמן הריצה וצריכת המשאבים יהיו זהים לחלוטין.
<br><br>

**3.** (שתי דרכים) תציג את שם המסעדה, שם המנה, כמות הפעמים שהיא הוזמנה, והמחיר הכולל שלה עבור המנה שנקנתה הכי הרבה פעמים במסעדה מסויימת
<img width="1177" height="266" alt="שאילתה41" src="https://github.com/user-attachments/assets/afefe569-8105-473c-9f18-55ca830ea2c2" />
<br><br>
<img width="622" height="66" alt="41" src="https://github.com/user-attachments/assets/a1032086-38af-48fa-aaca-2c2109162607" />
<br><br>
<img width="1160" height="392" alt="שאילתה42" src="https://github.com/user-attachments/assets/45f4c465-5b22-459e-a313-525165d600d6" />
<br><br>
<img width="622" height="78" alt="42" src="https://github.com/user-attachments/assets/121e8675-3ce1-4af7-90c0-11d9bc9401ab" />
<br><br>
<img width="1036" height="237" alt="ש4" src="https://github.com/user-attachments/assets/b80a53fd-7d3d-409b-9df2-fdcb3ae0016f" />
<br><br>

**4.** (שתי דרכים) תציג את שם המסעדה, שם המנה והמחיר שלה, עבור מנות שלא מופיעות באף הזמנה
<img width="822" height="268" alt="שאילתה81" src="https://github.com/user-attachments/assets/531a0b24-9f74-414f-83a6-cec747d87235" />
<br><br>
<img width="612" height="68" alt="81" src="https://github.com/user-attachments/assets/8b1a897a-96cc-4738-9312-346afd78c1f7" />
<br><br>
<img width="941" height="230" alt="שאילתה82" src="https://github.com/user-attachments/assets/ab307995-3339-4c2b-bf71-5359de516062" />
<br><br>
<img width="612" height="67" alt="82" src="https://github.com/user-attachments/assets/19a98ca2-c809-49bd-bb07-04a92c869568" />
<br><br>
<img width="808" height="221" alt="ש8" src="https://github.com/user-attachments/assets/6570c87d-67bb-4da6-99c0-14b79d9f46e0" />
<br><br>

**5.** תציג את שמות ומחירי התפריטים של מסעדות שסוג השירות שלהם הוא "קפה" בסדר עולה של השמות
<img width="637" height="217" alt="שאילתה3" src="https://github.com/user-attachments/assets/e0d7001f-1c2d-4743-ba7d-79deb9766ceb" />
<br><br>
<img width="637" height="67" alt="30" src="https://github.com/user-attachments/assets/833a3c76-feb5-43e0-aa51-64965efe95f9" />
<br><br>
<img width="1037" height="291" alt="ש3" src="https://github.com/user-attachments/assets/96c5c1d6-f228-4ade-a6e1-b977711fb3fb" />
<br><br>

**6.** תציג את שם התייר, מדינת המוצא ומספר השפות שהוא דובר, רק עבור תיירים שמדברים לפחות 2 שפות ושיש להם הזמנות במערכת
<img width="783" height="247" alt="שאילתה5" src="https://github.com/user-attachments/assets/bd5e4536-2e2d-4d0f-8df2-cfc719ceae9e" />
<br><br>
<img width="643" height="63" alt="50" src="https://github.com/user-attachments/assets/127a8aa7-c9d1-4a50-9d32-8050a6b80ec6" />
<br><br>
<img width="1037" height="286" alt="ש5" src="https://github.com/user-attachments/assets/e07991dc-0ebc-49e2-b189-21075b5b17be" />

**7.** תציג את קודי הקופונים, אחוז ההנחה ותאריך הסיום ששייכים למסעדה "Provider2" ולתיירים מארץ "France"
<img width="932" height="275" alt="שאילתה6" src="https://github.com/user-attachments/assets/a3d88d8a-31fd-40b0-9cd4-550778c39821" />
<br><br>
<img width="611" height="67" alt="60" src="https://github.com/user-attachments/assets/d232a0c2-3452-4d81-ad69-3311e90d9314" />
<br><br>
<img width="1032" height="233" alt="ש6" src="https://github.com/user-attachments/assets/175ce1f2-f294-481f-83dd-98b723e69ac8" />
<br><br>

**8.** תציג את מספר ההזמנה, שם התייר המזמין, תאריך ההזמנה המלא למסעדת "Provider1", עבור הזמנות שבוצעו ברבעון האחרון של שנת 2025 
<img width="777" height="292" alt="שאילתה7" src="https://github.com/user-attachments/assets/711f2f14-339e-434a-95fa-7d3f4152f4b1" />
<br><br>
<img width="612" height="68" alt="70" src="https://github.com/user-attachments/assets/100a6aec-a1d2-4a55-a488-d6023b425b84" />
<br><br>
<img width="1031" height="287" alt="ש7" src="https://github.com/user-attachments/assets/e4121d56-a2f7-4958-bdd2-a9309ed96022" />
<br><br>

### update queries

**1.** העלאת המחיר של כל המנות (ב-10%) השייכות לקטגוריה "Drink", אבל רק במסעדות שנמצאות בעיר ספציפית "Jerusalem"
<img width="480" height="246" alt="11" src="https://github.com/user-attachments/assets/0d76295d-1cbe-43f4-89c5-7e7634c811f4" />
<br><br>
<img width="422" height="68" alt="ע1" src="https://github.com/user-attachments/assets/fc588150-4c70-4ef2-85d7-190c751c5b9b" />
<br><br>
<img width="1032" height="287" alt="ע11" src="https://github.com/user-attachments/assets/59152914-117b-4faa-a740-b68243025ad6" />
<br><br>
<img width="1033" height="287" alt="ע12" src="https://github.com/user-attachments/assets/22ea5e2e-ba40-46af-95f3-9e0fa8bae16d" />
<br><br>

**2.** עדכון תאריך הסיום של הקופונים ששייכים לתיירים מארץ "USA"
<img width="782" height="333" alt="22" src="https://github.com/user-attachments/assets/a5a375dd-2ddc-4e44-beae-78f4304dd7db" />
<br><br>
<img width="423" height="68" alt="ע22" src="https://github.com/user-attachments/assets/ecd59032-4c74-4bfa-a01f-b766fc44f204" />
<br><br>
<img width="1032" height="287" alt="ע2" src="https://github.com/user-attachments/assets/0a43112d-a8a4-43f1-a3c4-ccbde5dcdc70" />
<br><br>
<img width="617" height="211" alt="ע222" src="https://github.com/user-attachments/assets/79cae77c-8b6c-4b2e-80fa-cb6d9b91c324" />
<br><br>
<img width="1033" height="283" alt="ע2222" src="https://github.com/user-attachments/assets/27c8db52-4535-4716-815d-47087192b27c" />
<br><br>

**3.** עדכון "סטטוס" ההזמנה ל-"Cancelled" עבור הזמנות שבהן מספר האנשים גדול מ-5, וההזמנה שייכת (ServiceType) למסעדה מסוג "Hotel" 
<img width="593" height="316" alt="33" src="https://github.com/user-attachments/assets/916b103e-39b4-493b-bfc7-f6b51cb91ece" />
<br><br>
<img width="423" height="62" alt="ע33" src="https://github.com/user-attachments/assets/d225c170-3e88-42b3-a29c-0506e7d75eaf" />
<br><br>
<img width="1031" height="287" alt="ע3" src="https://github.com/user-attachments/assets/e93bdde8-3aaa-419b-9269-4a1be61c92ea" />
<br><br>
<img width="567" height="206" alt="ע333" src="https://github.com/user-attachments/assets/2c4372a7-a392-4e56-b0e3-7852c6d1770f" />
<br><br>
<img width="1030" height="290" alt="ע3333" src="https://github.com/user-attachments/assets/671db380-08db-40b6-84da-832c3ef78f9d" />
<br><br>

### delete queries

**1.** מחיקת רשומות מטבלת "TOURIST" עבור תיירים שמעולם לא ביצעו הזמנה במערכת
<img width="642" height="212" alt="מ1111" src="https://github.com/user-attachments/assets/9abe9ab7-c189-4819-86da-feb27ed808a2" />
<br><br>
<img width="422" height="66" alt="מ11" src="https://github.com/user-attachments/assets/0112a7a1-1e0d-4b7e-8168-87832fd6add4" />
<br><br>
<img width="652" height="241" alt="מ111" src="https://github.com/user-attachments/assets/ab1b30bf-d595-43c8-8f54-52767a4b26d3" />
<br><br>
<img width="1277" height="287" alt="מ1" src="https://github.com/user-attachments/assets/5ac2e071-ac7f-42fd-a828-5f9c8145624d" />
<br><br>
<img width="1235" height="297" alt="מ11111" src="https://github.com/user-attachments/assets/455b6f4a-29b8-415f-ab1e-03175b3e163a" />
<br><br>


**2.** מחיקת קופונים מטבלת COUPON שתאריך הסיום שלהם קטן מתאריך ושעת המערכת הנוכחיים
<img width="928" height="213" alt="22222" src="https://github.com/user-attachments/assets/d9b4420d-ea94-4b39-be79-65b4b66f40c3" />
<br><br>
<img width="417" height="67" alt="222" src="https://github.com/user-attachments/assets/96eea133-046c-4193-b9ed-3a12ecbfbe8a" />
<br><br>
<img width="1032" height="286" alt="22" src="https://github.com/user-attachments/assets/82b366cc-bae0-4c4d-980d-94214e055790" />
<br><br>
<img width="932" height="263" alt="2222" src="https://github.com/user-attachments/assets/c62fa015-e277-49d5-87f6-fb80fb89a508" />
<br><br>


**3.** מחיקת כל מנות מהתפריט שהמחיר שלהם קטן מ-15, ושייכים למסעדות שנמצאות בחיפה
<img width="1047" height="440" alt="33333" src="https://github.com/user-attachments/assets/8634e6b0-7654-4b85-9320-64e89f9281c1" />
<br><br>
<img width="427" height="65" alt="333" src="https://github.com/user-attachments/assets/2477ff07-e8e5-4405-ac24-7bb17b269077" />
<br><br>
<img width="531" height="206" alt="3333" src="https://github.com/user-attachments/assets/e454dcbb-2b74-4449-8c6a-0bc3583dbc9b" />
<br><br>
<img width="1037" height="283" alt="33" src="https://github.com/user-attachments/assets/50e3898e-9629-428d-8f73-c7460114b937" />
<br><br>
<img width="890" height="280" alt="333333" src="https://github.com/user-attachments/assets/ea1424e7-8875-44d6-bd34-9e1ca9c71a74" />
<br><br>


### Constraints

**1.** האילוץ קובע שאי אפשר להכניס להזמנה יותר מ-20 אנשים, והוא חוסם אוטומטית כל רישום של מספר גבוה יותר
<img width="1021" height="711" alt="11" src="https://github.com/user-attachments/assets/3d0b1330-82f3-46e5-9cd8-43b61c6079ca" />
<br><br>

**2.** האילוץ מוודא שמספרי הטלפון בטבלה יהיו באורך תקין, והוא חוסם הכנסה של מספרים קצרים מדי (כמו 050995)
<img width="1057" height="701" alt="22" src="https://github.com/user-attachments/assets/81ec7cea-ea66-4ee6-9f6b-f1a995c9cc42" />
<br><br>

**3.** האילוץ על עמודת תאריך הסיום הופך אותה לשדה חובה, והוא מונע מצב שבו מכניסים קופון למערכת בלי לציין מתי הוא מסתיים
<img width="1061" height="712" alt="33" src="https://github.com/user-attachments/assets/35d70892-c217-47f7-830a-a02f8b718ff8" />
<br><br>


### RollbackCommit

**Rollback** 
<img width="1030" height="287" alt="11" src="https://github.com/user-attachments/assets/abd59edb-b0cb-4cc9-a527-0764351a0908" />
<br><br>
<img width="887" height="660" alt="11111" src="https://github.com/user-attachments/assets/deca01ef-1c10-4ba2-a968-e4e2fcc44a1a" />
<br><br>
<img width="588" height="242" alt="111" src="https://github.com/user-attachments/assets/9d4a3da2-5af3-4f4f-90e8-1047a7cc7ca4" />
<br><br>
<img width="1030" height="287" alt="11" src="https://github.com/user-attachments/assets/c1146a5c-7d63-4f57-b9c5-814908dfb087" />
<br><br>

**Commit**
<img width="952" height="317" alt="22" src="https://github.com/user-attachments/assets/a9cc4aec-0f53-40cd-9aba-dd55dd4298f0" />
<br><br>
<img width="846" height="700" alt="2222" src="https://github.com/user-attachments/assets/ed6d1d97-ef6f-4bdd-8114-8eab0672e0d2" />
<br><br>
<img width="700" height="252" alt="צילום מסך 2026-05-04 234154" src="https://github.com/user-attachments/assets/4148cad7-0cf0-446b-a90a-d1cf977b003f" />
<br><br>
<img width="1031" height="322" alt="222" src="https://github.com/user-attachments/assets/fe69f219-ccb5-4eae-a283-2c1eb9f0eac4" />
<br><br>


### Index
**1.** לאחר הוספת האינדקס, ניתן לראות בבירור שהאופטימייזר בחר להשתמש ב-Index Scan במקום לסרוק את כל הטבלה. כתוצאה מכך, זמן הריצה התקצר משמעותית והעומס על בסיס הנתונים פחת, מכיוון שנבדקו רק השורות הרלוונטיות לשאילתה
<img width="771" height="436" alt="111111" src="https://github.com/user-attachments/assets/02f9f57c-35ea-4cd8-805a-9c3f08001e67" />
<br><br>
<img width="1031" height="382" alt="1111" src="https://github.com/user-attachments/assets/5ccc5288-a736-4708-87b5-fd71b8a344be" />
<br><br>
<img width="1036" height="502" alt="11111" src="https://github.com/user-attachments/assets/549cd82c-920c-482c-b170-086e7463e5ba" />
<br><br>

**2.** הוספת האינדקס על עמודת ProviderID הפכה את החיפוש לפי ספק מפעולה של סריקה מלאה (Seq Scan) לגישה ישירה וממוקדת (Index Scan), מה שהוביל לחיסכון משמעותי במשאבי מערכת ולקיצור זמן התגובה של השאילתה
<img width="662" height="416" alt="22222" src="https://github.com/user-attachments/assets/8b8854c7-7e71-465e-8455-35805560e1ec" />
<br><br>
<img width="642" height="221" alt="222" src="https://github.com/user-attachments/assets/79c34893-ade5-4ff1-ba5d-11bce5238fa0" />
<br><br>
<img width="1031" height="321" alt="22" src="https://github.com/user-attachments/assets/3ecbc049-8445-4375-95af-a57d331bc2a7" />
<br><br>
<img width="1033" height="507" alt="2222" src="https://github.com/user-attachments/assets/52bd5a39-d4f6-435c-8065-87e5109b2f9a" />
<br><br>

**3.** האינדקס המשולב שיצרנו מאפשר למערכת לבצע סינון אופטימלי לפי שני קריטריונים בו-זמנית. בזכות המיון המשותף של ItemID ו-ProviderID, השאילתה מבצעת שליפה ישירה של השורות המתאימות בלבד, ללא צורך בסריקה מיותרת של נתונים שאינם עונים על שני התנאים יחד
<img width="805" height="420" alt="33" src="https://github.com/user-attachments/assets/dfedcc34-94f0-4494-bc45-f5f8fd791463" />
<br><br>
<img width="612" height="212" alt="3333" src="https://github.com/user-attachments/assets/5a4f4468-fa80-41b8-972a-9d7c7ff49361" />
<br><br>
<img width="1027" height="415" alt="333" src="https://github.com/user-attachments/assets/24ba61ca-c9be-4476-a1cb-4e5027c71bf6" />
<br><br>
<img width="1033" height="381" alt="33333" src="https://github.com/user-attachments/assets/9596bcd8-c81e-4176-96c1-8d1e0aa4d309" />
<br><br>


### backup2
backups files are kept with the date and hour of the backup:
* 📜 [View `Phase2/backup.backup2-28_4_26`](Phase2/backup.backup2-28_4_26)
<br><br>
<img width="578" height="330" alt="צילום מסך 2026-05-05 001108" src="https://github.com/user-attachments/assets/19e8d46d-ec03-4548-b739-4aa5a7a19ab0" />
<br><br>


## Phase 3: Integration and Views

### The new ERD
<img width="4512" height="2190" alt="erdplus (13)" src="https://github.com/user-attachments/assets/c82a4d85-2593-41ca-b73a-4e9ef221aef3" />
<br><br>

### The new DSD
<img width="4512" height="2190" alt="erdplus (12)" src="https://github.com/user-attachments/assets/fd56c89c-cd78-42ad-a8d6-07ae1aaf9733" />
<br><br>

### Integration Steps Summary
<br><br>
בשלב איחוד בסיסי הנתונים (אגף האטרקציות ואגף המסעדות), זיהינו כפילות במבנה - המערכת שקיבלנו הכילה את טבלת coupon (אגף האטרקציות), בעוד שהמערכת שלנו הכילה גם את טבלת coupon (אגף המסעדות). שתי הטבלאות ייצגו את אותה ישות לוגית אך החזיקו במבנה שדות שונה ובמפתחות ראשיים חופפים שהתחילו שניהם מהערך 1. (אותו מקרה קרה גם בטבלת ה reservation שהיתה פעמיים בבסיס הנתונים)
<br><br>
כדי לבצע אינטגרציה פיזית מלאה ולמנוע אובדן נתונים או שבירת קשרים, פעלנו באופן הבא:
<br><br>
**1.** מיפוי ונטרול אילוצי מפתחות זרים (Foreign Keys)
לפני שינוי הנתונים, מיפינו את הטבלאות ה"בנות" המסתמכות על טבלת המקור coupon (הטבלאות customercoupon ו-attractioncoupon). הסרנו זמנית את אילוצי המפתח הזר (DROP CONSTRAINT) כדי לאפשר את עדכון ערכי ה-IDs ללא שגיאות קשר (Referential Integrity).
<br><br>
**2.** פתרון התנגשויות מפתחות (Primary Key Conflicts)
מאחר ששני בסיסי הנתונים השתמשו במספרים רצים (Auto-Increment) שהתחילו מ-1, העתקה ישירה הייתה גורמת לדריסת נתונים או שגיאות ייחודיות (Unique Violation). פתרנו זאת על ידי הטיית מפתחות (ID Offsetting): הוספנו קבוע לכל ערכי ה-coupon_id של טבלת המקור (וכן לכל המפתחות הזרים המצביעים עליהם בטבלאות הבנות). צעד זה יצר מרווח ביטחון מוחלט ומנע התנגשויות עם הנתונים הקיימים בטבלת היעד.
<br><br>
**3.** השלמת שדות חובה: שדות שהיו קיימים רק בטבלת היעד (כגון startdate ו-providerid) הושלמו באמצעות ערכי ברירת מחדל הגיוניים כדי לעמוד באילוצי ה-NOT NULL של הטבלה המאוחדת.
<br><br>
**4.** החזרת האילוצים ועדכון מונים (Post-Migration)
לאחר העתקה מושלמת של כל הרשומות, קישרנו מחדש את אילוצי המפתחות הזרים של הטבלאות הבנות, אך הפעם ישירות אל הטבלה המאוחדת coupon1. לבסוף, הרצנו פקודת setval כדי לעדכן את המונה האוטומטי (Sequence) של הדטאבייס למספר המקסימלי החדש, מחקנו את טבלת המקור הכפולה (DROP TABLE) ושינינו את שם טבלת היעד המאוחדת לשם הסופי והישן: coupon.
<br><br>


### ERD of the integration
<img width="4512" height="2190" alt="erdplus (14)" src="https://github.com/user-attachments/assets/5130defe-78cd-4616-9579-9418dae3b30c" />
<br><br>

### DSD after integration
<img width="4512" height="2190" alt="erdplus (15)" src="https://github.com/user-attachments/assets/8c472e7e-3f40-449a-8f95-4fab2a60eeda" />
<br><br>

### reverse engineering

מתוך הDSD שנוצר מהבסיס נתונים שקיבלנו יצרנו את הERD שלו בהינדוס לאחור. האלגוריתם:
* **שלב 1:** מיפוי הישויות (Entities), סריקת רשימת הטבלאות הפיזיות בבסיס הנתונים שהתקבל. כל טבלה עצמאית שמייצגת עצם בעולם האמיתי (כגון: tourist, attraction, coupon) מתורגמת למלבן של ישות בתרשים ה-ERD.
<br><br>
* **שלב 2:** הגדרת תכונות (Attributes) ומפתחותעבור כל טבלה, חקירת העמודות וסוגי הנתונים שלהן.עמודות רגילות מתורגמות לשדות (עיגולים) המחוברים לישות. עמודה המוגדרת כמפתח ראשי (Primary Key) מסומנת בקו תחתון בתוך העיגול שלה בתרשים הERD.
<br><br>
* **שלב 3:** זיהוי ונטרול טבלאות קשר (Many-to-Many Bridge Tables), איתור טבלאות פיזיות שכל תפקידן הוא לחבר בין שתי טבלאות אחרות (הן מכילות בעיקר מפתחות זרים, כמו למשל הטבלאות reservedattraction או attractioncoupon). ב-ERD טבלאות אלו אינן מופיעות כמלבן עצמאי, אלא מתורגמות לצורת מעוין של קשר (Relationship) המחבר ישירות בין שתי הישויות.
<br><br>
* **שלב 4:** הגדרת קשרים (Relationships) וריבוי (Cardinality), איתור המפתחות הזרים (Foreign Keys) בטבלאות כדי להבין מי קשור למי. קביעת עוצמת הקשר (יחיד לרבים 1:N, או רבים לרבים N:M) על סמך חוקי העסק המשתקפים באילוצים (Constraints) ובאינדקסים של בסיס הנתונים.
<br><br>
<br><br>

### Alter and create table commands in the integration file
* 📜 [View `/integration.sql`](Phase3/integration.sql)
<br><br>

### Commands for creating views and queries on views in the Views file
<img width="921" height="437" alt="מבט111" src="https://github.com/user-attachments/assets/eef0abe3-11d1-48f6-bb02-79576e645e03" />
<br><br>
<img width="545" height="193" alt="view1" src="https://github.com/user-attachments/assets/258b6a2e-3fce-4ad6-a129-389368397b6e" />
<br><br>
<img width="1365" height="473" alt="מבט11" src="https://github.com/user-attachments/assets/cc6f6394-71d4-4a79-a60f-24782384018b" />
<br><br>
<img width="1075" height="210" alt="שאילתה1" src="https://github.com/user-attachments/assets/5d2df0dc-f134-4682-a57a-afbd182e9cf9" />
<br><br>
<img width="1042" height="287" alt="שאילתה1-1" src="https://github.com/user-attachments/assets/8d52462d-5f15-4838-b6f4-cd9d2c0a08c8" />
<br><br>
<img width="731" height="262" alt="שאילתה2" src="https://github.com/user-attachments/assets/2aa15706-3e0d-4c9b-9243-f5f27443ef23" />
<br><br>
<img width="596" height="290" alt="שאילתה1-2" src="https://github.com/user-attachments/assets/b7678a03-f456-45d9-86ae-9d1cd2750e53" />
<br><br>

#### The second view (on the database we received) is in the Views.sql file.
* 📜 [View `/Views.sql`](Phase3/Views.sql)
<br><br>

### backup3
* 📜 [View `/backup_2_6_2026`](Phase3/backup_2_6_2026)
<br><br>
<br><br>

## Phase 4: PL pgSQL programs

### Functions
פונקציה 1: הפונקציה הזו מקבלת מספר תייר (touristid). היא פותחת Cursor שעובר על כל האטרקציות שהתייר הזה הזמין, מחשבת את סך כל המחיר שלהן, ומחזירה את הסכום הסופי. אם נתנו לה מספר תייר שלא קיים בכלל במערכת, היא תזרוק Exception במקום לקרוס
<br><br>
<img width="1037" height="797" alt="פונקציה11" src="https://github.com/user-attachments/assets/5726f4f7-b0c4-4ae0-9924-3b4d2342618b" />
<br><br>
<img width="532" height="200" alt="פונקציה1" src="https://github.com/user-attachments/assets/054e943e-4e49-4806-8e85-7f6aaefd39c6" />
<br><br>
<img width="1047" height="662" alt="11" src="https://github.com/user-attachments/assets/b8b4655f-05c5-4bc7-807c-615148b5c3ee" />
<br><br>
<img width="932" height="617" alt="111" src="https://github.com/user-attachments/assets/b3ff806f-879f-449d-b87c-1f74a249c13d" />
<br><br>

פונקציה 2: הפונקציה הזו מקבלת מזהה ספק (p_provider_id). היא רצה עם לולאה מובנית על כל הקופונים של אותו ספק בטבלת coupon, סופרת כמה קופונים יש לו בסך הכל, ומחזירה את המספר הסופי.
<br><br>
<img width="981" height="516" alt="f22" src="https://github.com/user-attachments/assets/c1740a4d-d451-41a7-ab18-8d2490b910b7" />
<br><br>
<img width="616" height="248" alt="f2" src="https://github.com/user-attachments/assets/91e0459f-7700-4a56-8b89-fe10aa44d168" />
<br><br>
<img width="1047" height="506" alt="222" src="https://github.com/user-attachments/assets/299c75ba-8f7e-4f33-8173-e250d110808e" />
<br><br>
<img width="1048" height="506" alt="22" src="https://github.com/user-attachments/assets/1ead305e-3393-4bd3-b115-fec417545484" />
<br><br>

### Procedures
פרוצדורה 1: עדכון אוטומטי של כמות אנשים בהזמנה חריגה, נוצרו לנו הרבה הזמנות עם אדם 1 בלבד. הפרוצדורה הזו משתמשת בלולאת FOR (Implicit Cursor) כדי לעבור על כל ההזמנות שבהן מספר האנשים הוא 1, ומעדכנת אותן אוטומטית ל-2 אנשים (ברירת מחדל)
<br><br>
<img width="952" height="507" alt="P11" src="https://github.com/user-attachments/assets/c24491d3-7354-4251-acd1-89c88201896c" />
<br><br>
<img width="575" height="202" alt="P1" src="https://github.com/user-attachments/assets/6498e76e-b1c2-4c08-900c-353bd289f848" />
<br><br>

פרוצדורה 2: החלת סטטוס קופונים מרוכז לפי ספק
הפרוצדורה הזו מקבלת מזהה ספק (p_provider_id) וסטטוס חדש (p_new_status, למשל 'A' או 'U'). היא בודקת קודם כל אם הסטטוס חוקי, ואז מעדכנת בבת אחת את כל הקופונים של אותו ספק לסטטוס החדש. אם הסטטוס לא חוקי, היא זורקת Exception.

<br><br>
<img width="1695" height="960" alt="פרוצ2 לפני" src="https://github.com/user-attachments/assets/096df739-91f5-45e0-843b-4068cdeee135" />
<br><br>
<img width="1729" height="972" alt="פרוצ2 הרצה" src="https://github.com/user-attachments/assets/7dd315ba-6c45-46b8-928a-d51ce11ab2a1" />
<br><br>
<img width="1705" height="991" alt="פרוצ2 אחרי" src="https://github.com/user-attachments/assets/dd3d2945-c643-44cf-ae6a-bcd2e7139526" />
<br><br>
<img width="1781" height="983" alt="פרוצ2 שגיאה" src="https://github.com/user-attachments/assets/9da9ea2f-cd1d-43ef-98d3-5deb123470d6" />
<br><br>


### Triggers
טריגר 1: הגנה מפני עדכון קופונים שפג תוקפם
הטריגר יושב על טבלת coupon. ברגע שמישהו מנסה לעדכן קופון ומנסה להפוך את הסטטוס שלו ל-'A' (פעיל), הטריגר מתערב ובודק אם תאריך התפוגה שלו (enddate) כבר עבר. אם התאריך עבר, הטריגר זורק Exceptionוחוסם פיזית את ה-UPDATE כדי לשמור על אמינות הנתונים!

<br><br>
<img width="1652" height="962" alt="טריגר1" src="https://github.com/user-attachments/assets/2bfa2473-5316-41ae-a522-8d528cc4e5bf" />
<br><br>
<img width="1707" height="439" alt="טריגר1 עובד" src="https://github.com/user-attachments/assets/7d3f1cd0-8cbb-4907-a302-e610639d4d4b" />
<br><br>

טריגר 2: הגבלת כמות אנשים מקסימלית בהזמנה חדשה (בזמן INSERT)
הטריגר הזה יושב על טבלת reservation (הזמנות). לפני שמתווספת שורה חדשה, הוא מוודא שמספר האנשים הגיוני (למשל, לא הגיוני שקבוצה של יותר מ-30 איש תזמין מקום רגיל בלי תיאום מיוחד). אם המספר גדול מ-30, הטריגר קופץ ומונע את ה-INSERT.
<br><br>
<img width="1710" height="1025" alt="טריגר2" src="https://github.com/user-attachments/assets/7a3db75c-6ffc-48f8-9ef9-897a36a21eae" />
<br><br>


### Main programs
התכנית הראשית הראשונה מזמנת את הפונקציה fn_get_tourist_spending, אשר מחשבת את סך ההוצאות של תייר לפי מזהה התייר, ומדפיסה את התוצאה באמצעות RAISE NOTICE. לאחר מכן התוכנית מזמנת את הפרוצדורה pr_optimize_reservation_people, אשר מעדכנת הזמנות שבהן מספר המשתתפים הוא 1 ומגדילה אותו ל־2. בסיום מוצגת הודעת הצלחה. התוכנית כוללת גם טיפול בחריגות, כך שבמקרה של שגיאה תודפס הודעה מתאימה במקום הפסקה לא מבוקרת של הריצה.

<br><br>
<img width="1408" height="1027" alt="ראשית1" src="https://github.com/user-attachments/assets/ca162d53-bb97-495a-abae-06f575cdfe81" />
<br><br>

התכנית הראשית השנייה בתחילת הריצה היא מפעילה את הפונקציה fn_get_provider_coupon_count, אשר סופרת את מספר הקופונים השייכים לספק מסוים ומחזירה את התוצאה. מספר הקופונים מוצג למשתמש באמצעות RAISE NOTICE. לאחר מכן התוכנית מפעילה את הפרוצדורה pr_update_provider_coupon_status, אשר מעדכנת את סטטוס הקופונים של אותו ספק בהתאם לערך שנמסר. בסיום מוצגת הודעת הצלחה. התוכנית כוללת טיפול בחריגות, כך שבמקרה של שגיאה תודפס הודעה מתאימה עם פירוט השגיאה.
<br><br>
<img width="1345" height="986" alt="ראשית2" src="https://github.com/user-attachments/assets/03322187-50cb-42e5-9b8a-01c60f024c91" />
<br><br>


## Phase 5: Graphical interface

  📜 [View `DineReserve_Manual.pdf`](Phase5/DineReserve_Manual.pdf)

<img width="1595" height="1005" alt="צילום מסך 2026-06-23 140621" src="https://github.com/user-attachments/assets/71aff6b0-3eea-472c-b332-6814b71ad195" />
<br><br>
<img width="1602" height="1010" alt="צילום מסך 2026-06-23 140647" src="https://github.com/user-attachments/assets/9c29977c-7c3f-47bc-ae71-e1de468dab63" />
<br><br>
<img width="1601" height="1007" alt="צילום מסך 2026-06-23 140713" src="https://github.com/user-attachments/assets/ddbb289d-910c-4116-98ee-640b06e0fa8b" />
<br><br>
<img width="1602" height="1006" alt="צילום מסך 2026-06-23 140739" src="https://github.com/user-attachments/assets/f61c4ea6-370c-4de5-838f-44d574574ff6" />
<br><br>
<img width="1596" height="1012" alt="צילום מסך 2026-06-23 140813" src="https://github.com/user-attachments/assets/cd19a047-68d9-445c-981a-908874c85233" />
<br><br>
<img width="1602" height="1007" alt="צילום מסך 2026-06-23 140849" src="https://github.com/user-attachments/assets/96dd13ad-02b8-4b14-959e-9971b71050a1" />
<br><br>
<img width="1597" height="1012" alt="צילום מסך 2026-06-23 140913" src="https://github.com/user-attachments/assets/b766a692-b06c-41aa-ac4b-d7b451c02c47" />
<br><br>
<img width="1602" height="1002" alt="צילום מסך 2026-06-23 140938" src="https://github.com/user-attachments/assets/14af9ff2-f0fd-4263-aadf-b8d4fc874818" />
<br><br>
<img width="1591" height="1007" alt="צילום מסך 2026-06-23 143319" src="https://github.com/user-attachments/assets/0273e7cf-8fe6-467e-835b-4d2d78318cc2" />
<br><br>
<img width="1597" height="1011" alt="צילום מסך 2026-06-23 143405" src="https://github.com/user-attachments/assets/0c58486b-f27f-424e-ba68-02a191e9cca2" />
<br><br>
<img width="1596" height="1010" alt="צילום מסך 2026-06-23 143438" src="https://github.com/user-attachments/assets/3b206dff-f9fb-4862-9d99-b7eda7f13b04" />
<br><br>
<img width="1600" height="1012" alt="צילום מסך 2026-06-23 143506" src="https://github.com/user-attachments/assets/19bbb0bf-1180-4d0c-bb8f-810385728b3c" />
<br><br>
<img width="1597" height="1002" alt="צילום מסך 2026-06-23 140555" src="https://github.com/user-attachments/assets/1f017419-1663-42ab-a858-098b32657410" />
<br><br>

