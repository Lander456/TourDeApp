--inventory table

DROP TABLE IF EXISTS inventory;

CREATE TABLE inventory(
    itemId INTEGER PRIMARY KEY AUTOINCREMENT,
    itemName TEXT,
    category TEXT,
    colour TEXT,
    inStock INTEGER,
    price INTEGER,
    descript TEXT
);

--users

DROP TABLE IF EXISTS users;

CREATE TABLE users(
    userId INTEGER PRIMARY KEY AUTOINCREMENT,
    userName TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role 
);

--cart

DROP TABLE IF EXISTS cart;

CREATE TABLE cart(
    itemId INTEGER PRIMARY KEY AUTOINCREMENT,
    itemName TEXT,
    category TEXT,
    colour TEXT,
    inStock INTEGER,
    price INTEGER,
    descript TEXT
)