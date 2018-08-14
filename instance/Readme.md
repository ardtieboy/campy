# Sqlite user database

create the database with schema

    sqlite3 flaskr.sqlite < schema.sql

log on onto the db

    sqlite3 flaskr.sqlite

check if the db is accessible and empty

    select * from user;

insert users

    insert into user(username, password) values ('Ard','hashed_password')

Where hashed_password is the outcome of this python snipped:

    from werkzeug.security import check_password_hash, generate_password_hash
    print(generate_password_hash('unhashed_password')