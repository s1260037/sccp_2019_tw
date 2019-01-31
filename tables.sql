CREATE TABLE users (
 -- 利用者id
 id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

 -- 利用者名義
 name varchar(255) UNIQUE,

 -- 利用者パスワード
 password verchar(255)
);

CREATE TABLE tweets (
 id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
 
 -- id
 user_id INTEGER,

 -- tweet
 text varchar(255),

 -- time
 published_at INTEGER
);
