-- This script initializes database structure
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);
CREATE TABLE leads (
    id SERIAL PRIMARY KEY,
    source VARCHAR(50) NOT NULL
);