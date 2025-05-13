-- clinic_booking.sql
-- Description: MySQL schema for a Clinic Booking System
-- Drop existing tables if they exist
DROP TABLE IF EXISTS PrescriptionMedications, Prescriptions, Appointments, Medications, Patients, Doctors, Specializations, Rooms;

-- Specializations table
CREATE TABLE Specializations (
    specialization_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- Doctors table
CREATE TABLE Doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    specialization_id INT,
    FOREIGN KEY (specialization_id) REFERENCES Specializations(specialization_id)
);

-- Patients table
CREATE TABLE Patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(100)
);

-- Rooms table
CREATE TABLE Rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(10) NOT NULL UNIQUE,
    type ENUM('Consultation', 'Surgery', 'Examination') NOT NULL
);

-- Appointments table
CREATE TABLE Appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    room_id INT,
    appointment_date DATETIME NOT NULL,
    reason TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id),
    UNIQUE(patient_id, doctor_id, appointment_date)
);

-- Prescriptions table
CREATE TABLE Prescriptions (
    prescription_id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT NOT NULL,
    notes TEXT,
    date_issued DATE NOT NULL,
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id)
);

-- Medications table
CREATE TABLE Medications (
    medication_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    dosage VARCHAR(50) NOT NULL
);

-- Prescription-Medication join table
CREATE TABLE PrescriptionMedications (
    prescription_id INT,
    medication_id INT,
    quantity INT NOT NULL CHECK (quantity > 0),
    PRIMARY KEY (prescription_id, medication_id),
    FOREIGN KEY (prescription_id) REFERENCES Prescriptions(prescription_id),
    FOREIGN KEY (medication_id) REFERENCES Medications(medication_id)
);

-- Sample data for Specializations
INSERT INTO Specializations (name) VALUES 
('Cardiology'),
('Dermatology'),
('Pediatrics');

-- Sample data for Doctors
INSERT INTO Doctors (full_name, email, phone, specialization_id) VALUES 
('Dr. Alice Kim', 'alice.kim@clinic.com', '0712345678', 1),
('Dr. Brian Otieno', 'brian.otieno@clinic.com', '0723456789', 2),
('Dr. Carol Njeri', 'carol.njeri@clinic.com', '0734567890', 3);

-- Sample data for Patients
INSERT INTO Patients (full_name, date_of_birth, gender, phone, email) VALUES 
('John Mwangi', '1990-06-15', 'Male', '0701234567', 'john.mwangi@example.com'),
('Grace Wanjiru', '1985-09-22', 'Female', '0702345678', 'grace.wanjiru@example.com'),
('Kevin Oloo', '2000-01-05', 'Male', '0703456789', 'kevin.oloo@example.com');

-- Sample data for Rooms
INSERT INTO Rooms (room_number, type) VALUES 
('101', 'Consultation'),
('201', 'Examination'),
('301', 'Surgery');

-- Sample data for Appointments
INSERT INTO Appointments (patient_id, doctor_id, room_id, appointment_date, reason) VALUES 
(1, 1, 1, '2025-05-20 10:00:00', 'Heart check-up'),
(2, 2, 2, '2025-05-21 11:30:00', 'Skin rash'),
(3, 3, 1, '2025-05-22 09:00:00', 'Child fever');

-- Sample data for Prescriptions
INSERT INTO Prescriptions (appointment_id, notes, date_issued) VALUES 
(1, 'Take medication A for 5 days', '2025-05-20'),
(2, 'Apply cream B twice daily', '2025-05-21'),
(3, 'Paracetamol syrup for 3 days', '2025-05-22');

-- Sample data for Medications
INSERT INTO Medications (name, dosage) VALUES 
('Medication A', '500mg'),
('Cream B', 'Apply topically'),
('Paracetamol Syrup', '5ml');

-- Sample data for PrescriptionMedications
INSERT INTO PrescriptionMedications (prescription_id, medication_id, quantity) VALUES 
(1, 1, 10),
(2, 2, 1),
(3, 3, 6);
select * from appointments;


