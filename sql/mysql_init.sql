CREATE TABLE IF NOT EXISTS species (
    id INT PRIMARY KEY,
    name VARCHAR(40)
);

CREATE TABLE IF NOT EXISTS breed (
    id INT PRIMARY KEY,
    species_id INT NOT NULL,
    name VARCHAR(40),
    KEY `breed_species_id` (`species_id`),
    CONSTRAINT `breed_species_id` FOREIGN KEY (`species_id`) REFERENCES `species`(`id`) 
);

CREATE TABLE IF NOT EXISTS user (
    username VARCHAR(20) PRIMARY KEY,
    password VARCHAR(20) NOT NULL,
    name VARCHAR(40),
    avatar VARCHAR(255),
    email VARCHAR(40),
    address VARCHAR(60),
    zipcode INT,
    is_person BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS pet (
    id INT PRIMARY KEY,
    name VARCHAR(20),
    age DOUBLE,
    gender CHAR(1),
    weight DOUBLE,
    adopt_status VARCHAR(10),
    personality VARCHAR(125),
    color VARCHAR(20),
    image VARCHAR(255),
    hair VARCHAR(6),
    breed_id INT,
    adopt_user VARCHAR(20),
    adopt_time DATETIME
--    KEY `adopt_username` (`adopt_user`),
--    CONSTRAINT `adopt_username` FOREIGN KEY (`adopt_user`) REFERENCES `user`(`username`)
);

CREATE TABLE IF NOT EXISTS posts (
    pet_id INT,
    username VARCHAR(20),
    title VARCHAR(60) NOT NULL,
    open_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    close_time DATETIME,
    description VARCHAR(500),
    PRIMARY KEY (pet_id, username)
);

CREATE TABLE IF NOT EXISTS message (
	id INT  PRIMARY KEY,
	sender VARCHAR(20),
	receiver VARCHAR(20),
	time DATETIME DEFAULT CURRENT_TIMESTAMP,
	content VARCHAR(500),
	new BOOLEAN NOT NULL
);
