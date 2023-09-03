CREATE DATABASE IF NOT EXISTS bookstore;

USE bookstore;

CREATE TABLE admins (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    adminame VARCHAR(50) NOT NULL,
    number VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS users (
    userID INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS book (
    bookID INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(50),
    genre VARCHAR(50),
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    orderID INT AUTO_INCREMENT PRIMARY KEY,
    bookID INT,
    orderdate DATE,
    orderamount DECIMAL(10, 2),
    userID INT,
    FOREIGN KEY (bookID) REFERENCES book(bookID),
    FOREIGN KEY (userID) REFERENCES users(userID)
);







