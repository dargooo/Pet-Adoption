CREATE TABLE species (
    id INT PRIMARY KEY,
    name VARCHAR(40)
);

CREATE TABLE breed (
    id INT PRIMARY KEY,
    species_id INT,
    name VARCHAR(40),
    KEY `breed_species_id` (`species_id`),
    CONSTRAINT `breed_species_id` FOREIGN KEY (`species_id`) REFERENCES `species`(`id`) 
);

CREATE TABLE user (
    username VARCHAR(20),
    password VARCHAR(20),
    name VARCHAR(40),
    avatar VARCHAR(255),
    email VARCHAR(40),
    address VARCHAR(60),
    zipcode INT,
    preference VARCHAR(125),
    is_person BOOLEAN
);

CREATE TABLE pets(
    id INT PRIMARY KEY,
    name VARCHAR(20),
    age DOUBLE,
    weight DOUBLE,
    adopt_status VARCHAR(10),
    personality VARCHAR(125),
    color VARCHAR(20),
    image VARCHAR(255),
    hair VARCHAR(6),
    breed_id INT,
    adopt_user VARCHAR(20),
    adopt_time DATETIME,
    KEY `adopt_username` (`adopt_user`),
    CONSTRAINT `adopt_username` FOREIGN KEY (`adopt_user`) REFERENCES `user`(`username`)
);

CREATE TABLE posts (
    pet_id INT PRIMARY KEY,
    username VARCHAR(20) PRIMARY KEY,
    title VARCHAR(40),
    open_time DATETIME,
    close_time DATETIME,
    description DATETIME(500)
);
