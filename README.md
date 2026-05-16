#  Hospital Organ Matching System

A desktop application built with *Python (Tkinter)* and *SQLite* to manage patients and organ donors and automatically match them based on blood type and required/donated organ.

---

##  Features

- Add / Update / Delete Patients  
- Add / Update / Delete Donors  
- View all records in a table (Treeview)  
- Automatic matching between patients and donors  
- Match based on:
  - Blood Type
  - Organ Type  

---

##  Matching Logic

A match happens when:

- Patient blood type = Donor blood type  
- Patient needed organ = Donor donated organ  

Implemented using SQL INNER JOIN.

---

##  Database

Database file:

hospital.db


### Tables

#### Patient
- patient_id (Primary Key)
- patient_name
- blood_type
- needed_organ

#### Donor
- donor_id (Primary Key)
- donor_name
- blood_type
- donated_organ

---

##  How to Run

### 1. Install Python
Make sure Python 3 is installed.

### 2. Run the program
bash
python hospital_system.py


No external libraries required.

---

##  Interface

The system includes:

- Patient management panel  
- Donor management panel  
- Control buttons:
  - Show Patients  
  - Show Donors  
  - Show Matching Results  
- Data table display (Treeview)

---

##  Tech Stack

- Python  
- Tkinter (GUI)  
- SQLite (Database)

---

##  Functions

- add_patient()  
- add_donor()  
- update_patient()  
- update_donor()  
- delete_patient()  
- delete_donor()  
- show_patients()  
- show_donors()  
- show_matching()  

---

##  Future Improvements

- Search feature  
- Login system  
- Better UI design  
- Export to Excel/PDF  
- Advanced matching rules (priority / urgency)

---

##  Author

Simple hospital management system for learning:
- GUI development  
- Database integration  
- CRUD operations
