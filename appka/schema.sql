--inventory table

DROP TABLE IF EXISTS inventory;

CREATE TABLE inventory(
    itemId INTEGER PRIMARY KEY AUTOINCREMENT,
    itemName TEXT,
    category TEXT,
    colour TEXT,
    IN_STORE INTEGER,
    descript TEXT
);