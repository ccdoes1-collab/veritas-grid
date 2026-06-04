-- Extend database with more tables
CREATE TABLE audit_logs (
    id SERIAL PRIMARY KEY,
    action TEXT,
    user_id INT REFERENCES users(id)
);
CREATE TABLE security_incidents (
    id SERIAL PRIMARY KEY,
    description TEXT
);