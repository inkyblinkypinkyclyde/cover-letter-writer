DROP TABLE IF EXISTS cover_letter_data;

CREATE TABLE cover_letter_data (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    data TEXT
);