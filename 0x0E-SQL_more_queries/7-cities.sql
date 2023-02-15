-- create satabase 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- switch to hbtn_0d_usa database
USE hbtn_0d_usa;

-- create table states
CREATE TABLE IF NOT EXISTS states(
    id INT PRIMARY KEY,
    name VARCHAR(256)NOT NULL
);
-- create table cities
CREATE TABLE IF NOT EXISTS cities(
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256)NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
