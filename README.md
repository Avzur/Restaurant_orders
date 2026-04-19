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
  * [Backup](#backup)
* [Phase 2: Integration](#phase-2-integration)

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

Provide the following SQL scripts:

* **Create Tables Script** - The SQL script for creating the database tables is available in the repository:

  📜 [View `create_tables.sql`](createtables.sql)

* **Insert Data Script** - The SQL script for insert data to the database tables is available in the repository:

  📜 [View `insertTables.sql`](insertTables.sql)

* **Drop Tables Script** - The SQL script for droping all tables is available in the repository:

  📜 [View `dropTables.sql`](dropTables.sql)

* **Select All Data Script** - The SQL script for selectAll tables is available in the repository:

  📜 [View `selectAll.sql`](selectAll.sql)

  ### Data

First tool: using [mockaro](https://www.mockaroo.com/) to create csv file

Entering a data to RESERVATION table

* reservation id scope 1-1000 📜 [View `RESERVATION_MOCK_DATA.csv`](RESERVATION_MOCK_DATA.csv)

Entering a data to SERVICEPROVIDER table

* Service provider id scope 1-1000 📜 [View `SERVICEPROVIDER_MOCK_DATA.csv`](SERVICEPROVIDER_MOCK_DATA.csv)

Entering a data to TOURISTDISCOUNT table

* tourist id scope 1-1000 📜 [View `TOURISTDISCOUNT_MOCK_DATA.csv`](TOURISTDISCOUNT_MOCK_DATA.csv)

