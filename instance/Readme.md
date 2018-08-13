sqlite3 flaskr.sqlite < schema.sql

sqlite3 flaskr.sqlite

select * from user;

insert into user(username, password) values ('Ard','hashed_password')

Where hashed_password is the outcome from:

    from werkzeug.security import check_password_hash, generate_password_hash
    print(generate_password_hash('unhashed_password')

Add users this way.