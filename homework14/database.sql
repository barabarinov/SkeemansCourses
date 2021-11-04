CREATE TABLE IF NOT EXISTS items
(
    id      SERIAL PRIMARY KEY,
    title   VARCHAR(32) NOT NULL UNIQUE,
    amount  SMALLINT NOT NULL,
    price   MONEY NOT NULL
);


CREATE TABLE IF NOT EXISTS users
(
    id         SERIAL PRIMARY KEY,
    username   VARCHAR(20)  NOT NULL UNIQUE,
    password   VARCHAR(128) NOT NULL,
    first_name VARCHAR(30)  NOT NULL,
    last_name  VARCHAR(30)  NOT NULL,
    age        SMALLINT,
    is_admin   BOOLEAN      NOT NULL DEFAULT false
);
