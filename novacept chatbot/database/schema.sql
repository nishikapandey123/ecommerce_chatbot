CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    preferences JSONB
);

CREATE TABLE data_sources (
    id SERIAL PRIMARY KEY,
    source_type VARCHAR(50),
    content TEXT
);
