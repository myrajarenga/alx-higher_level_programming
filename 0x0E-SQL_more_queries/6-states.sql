-- create satabase 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- switch to hbtn_0d_usa database
USE hbtn_0d_usa;

-- create table
CREATE TABLE IF NOT EXISTS states(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256)NOT NULL,
    PRIMARY KEY(id),
    UNIQUE KEY unique_id(id)
);
