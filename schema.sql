CREATE DATABASE IF NOT EXISTS TaskManagement;

USE TaskManagement;

CREATE TABLE IF NOT EXISTS tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE,
    priority_level ENUM('Low', 'Medium', 'High') NOT NULL,
    status ENUM('Pending', 'In Progress', 'Completed') NOT NULL,
    creation_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);