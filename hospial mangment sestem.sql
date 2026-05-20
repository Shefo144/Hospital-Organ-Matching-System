-- =========================================
-- RESET DATABASE
-- =========================================
USE master;
GO

IF EXISTS (SELECT * FROM sys.databases WHERE name = 'MegaHospitalDB')
BEGIN
    ALTER DATABASE MegaHospitalDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE MegaHospitalDB;
END
GO

CREATE DATABASE MegaHospitalDB;
GO

USE MegaHospitalDB;
GO

-- =========================================
-- TABLES
-- =========================================

CREATE TABLE Donor (
    donor_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(50),
    age INT,
    blood_type VARCHAR(5),
    phone VARCHAR(20)
);

CREATE TABLE Patient (
    patient_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(50),
    age INT,
    blood_type VARCHAR(5),
    address VARCHAR(100)
);

CREATE TABLE Doctor (
    doctor_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(50),
    specialization VARCHAR(50)
);

CREATE TABLE Nurse (
    nurse_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(50)
);

CREATE TABLE Hospital (
    hospital_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE BloodBank (
    bank_id INT PRIMARY KEY IDENTITY(1,1),
    hospital_id INT,
    capacity INT,
    FOREIGN KEY (hospital_id) REFERENCES Hospital(hospital_id)
);

CREATE TABLE Donation (
    donation_id INT PRIMARY KEY IDENTITY(1,1),
    donor_id INT,
    bank_id INT,
    donation_date DATE,
    FOREIGN KEY (donor_id) REFERENCES Donor(donor_id),
    FOREIGN KEY (bank_id) REFERENCES BloodBank(bank_id)
);

CREATE TABLE Surgery (
    surgery_id INT PRIMARY KEY IDENTITY(1,1),
    patient_id INT,
    doctor_id INT,
    donor_id INT,
    surgery_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id),
    FOREIGN KEY (donor_id) REFERENCES Donor(donor_id)
);

CREATE TABLE Matches (
    donor_id INT,
    patient_id INT,
    match_date DATE,
    PRIMARY KEY (donor_id, patient_id),
    FOREIGN KEY (donor_id) REFERENCES Donor(donor_id),
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id)
);

CREATE TABLE Assists (
    nurse_id INT,
    surgery_id INT,
    PRIMARY KEY (nurse_id, surgery_id),
    FOREIGN KEY (nurse_id) REFERENCES Nurse(nurse_id),
    FOREIGN KEY (surgery_id) REFERENCES Surgery(surgery_id)
);

GO
-- =========================================
-- INSERT DATA
-- =========================================

INSERT INTO Donor (name, age, blood_type, phone) VALUES
('Ali',25,'A+','01011111111'),
('Mona',30,'O+','01022222222'),
('Khaled',28,'B+','01033333333'),
('Nour',22,'AB+','01044444444'),
('Hassan',35,'A-','01055555555');

INSERT INTO Patient (name, age, blood_type, address) VALUES
('Sara',20,'A+','Cairo'),
('Omar',35,'O+','Giza'),
('Laila',27,'B+','Zagazig'),
('Hana',40,'AB+','Mansoura'),
('Yara',19,'A-','Alex');

INSERT INTO Doctor (name, specialization) VALUES
('Dr.Ahmed','Cardiology'),
('Dr.Mohamed','Surgery'),
('Dr.Khaled','Neurology');

INSERT INTO Nurse (name) VALUES
('Nurse1'),('Nurse2'),('Nurse3');

INSERT INTO Hospital (name, city) VALUES
('Cairo Hospital','Cairo'),
('Zagazig Hospital','Zagazig');

INSERT INTO BloodBank (hospital_id, capacity) VALUES
(1,100),(2,150);

INSERT INTO Donation (donor_id, bank_id, donation_date) VALUES
(1,1,'2024-01-10'),
(2,2,'2024-02-15'),
(3,1,'2024-03-20'),
(4,2,'2024-04-05'),
(5,1,'2024-05-01');

INSERT INTO Matches VALUES
(1,1,'2024-01-11'),
(2,2,'2024-02-16'),
(3,3,'2024-03-21'),
(4,4,'2024-04-06'),
(5,5,'2024-05-02');

INSERT INTO Surgery (patient_id, doctor_id, donor_id, surgery_date) VALUES
(1,1,1,'2024-01-15'),
(2,2,2,'2024-02-20'),
(3,3,3,'2024-03-25');

INSERT INTO Assists VALUES
(1,1),(2,2),(3,3);

GO

-- =========================================
-- SELECT + WHERE
-- =========================================

SELECT * FROM Donor;
SELECT * FROM Patient;
SELECT * FROM Doctor;

SELECT * FROM Patient WHERE age > 25;
SELECT * FROM Donor WHERE blood_type = 'A+';

GO

-- =========================================
-- UPDATE
-- =========================================

UPDATE Donor SET age = 26 WHERE donor_id = 1;
UPDATE Patient SET name = 'Sara Ahmed' WHERE patient_id = 1;

GO

-- =========================================
-- DELETE
-- =========================================

DELETE FROM Donation WHERE donation_id = 5;

GO

-- =========================================
-- JOINS
-- =========================================

SELECT D.name AS Donor, P.name AS Patient
FROM Matches M
JOIN Donor D ON M.donor_id = D.donor_id
JOIN Patient P ON M.patient_id = P.patient_id;

SELECT H.name, B.capacity
FROM Hospital H
JOIN BloodBank B ON H.hospital_id = B.hospital_id;

SELECT P.name, D.name, S.surgery_date
FROM Surgery S
JOIN Patient P ON S.patient_id = P.patient_id
JOIN Doctor D ON S.doctor_id = D.doctor_id;

GO

-- =========================================
-- GROUP BY
-- =========================================

SELECT blood_type, COUNT(*) FROM Donor GROUP BY blood_type;
SELECT doctor_id, COUNT(*) FROM Surgery GROUP BY doctor_id;

GO

-- =========================================
-- VIEWS
-- =========================================

CREATE VIEW Full_View AS
SELECT P.name AS Patient, D.name AS Doctor, S.surgery_date
FROM Surgery S
JOIN Patient P ON S.patient_id = P.patient_id
JOIN Doctor D ON S.doctor_id = D.doctor_id;

GO

SELECT * FROM Full_View;

GO

-- =========================================
-- FUNCTIONS
-- =========================================

CREATE FUNCTION CountDonations (@id INT)
RETURNS INT
AS
BEGIN
    DECLARE @c INT;
    SELECT @c = COUNT(*) FROM Donation WHERE donor_id = @id;
    RETURN @c;
END;

GO

SELECT dbo.CountDonations(1);

GO

-- =========================================
-- STORED PROCEDURES
-- =========================================

CREATE PROCEDURE AddDonor
@name VARCHAR(50),
@age INT,
@blood VARCHAR(5)
AS
BEGIN
INSERT INTO Donor(name,age,blood_type)
VALUES(@name,@age,@blood);
END;

GO

CREATE PROCEDURE GetPatients
AS
BEGIN
SELECT * FROM Patient;
END;

GO

EXEC GetPatients;

GO

-- =========================================
-- TRIGGER
-- =========================================

CREATE TRIGGER prevent_delete_patient
ON Patient
INSTEAD OF DELETE
AS
BEGIN
IF EXISTS (SELECT 1 FROM Surgery WHERE patient_id IN (SELECT patient_id FROM deleted))
PRINT 'Cannot delete patient!';
ELSE
DELETE FROM Patient WHERE patient_id IN (SELECT patient_id FROM deleted);
END;

GO

-- =========================================
-- EXTRA QUERIES 
-- =========================================

SELECT * FROM Donation ORDER BY donation_date;
SELECT * FROM Patient ORDER BY age DESC;

SELECT DISTINCT blood_type FROM Donor;

SELECT COUNT(*) FROM Patient;
SELECT AVG(age) FROM Donor;

GO