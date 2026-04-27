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
  * [Backup](#backup)
* [Phase 2: Queries and constraints](#Phase-2-Queries-and-constraints)
  * [select queries](#select-queries)


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

### backup

backups files are kept with the date and hour of the backup:
* 📜 [View `backup.backup-19_4_26`](Phase1/backup/backup.backup-19_4_26)
<img width="1691" height="748" alt="image" src="https://github.com/user-attachments/assets/97bf4be2-4b1f-41fb-881e-8d4747fbff0b" />
<br><br>
<img width="606" height="360" alt="צילום מסך 2026-04-19 2109g09" src="https://github.com/user-attachments/assets/2dc6be70-1f18-4106-bad8-2bc9caf98128" />
<br><br>


## Phase 2: Queries and constraints

### select queries

1. The query displays the first name, last name, and country of origin of tourists who made any reservations during January 2026. The information is extracted from the tourists table and relies on filtering dates from the reservations table.
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










