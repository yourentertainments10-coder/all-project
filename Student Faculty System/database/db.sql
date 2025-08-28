-- Step 2: Database Design (MySQL)

-- 1. Users Table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL, -- hashed password
    role ENUM('student', 'faculty') NOT NULL
);

-- 2. Students Table (only for student roles)
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    course VARCHAR(100) NOT NULL,
    semester INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES users(id) ON DELETE CASCADE
);

-- 3. Assignments Table
CREATE TABLE assignments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    grade VARCHAR(10),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- 4. Attendance Table
CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    date DATE NOT NULL,
    status ENUM('Present', 'Absent') NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);
