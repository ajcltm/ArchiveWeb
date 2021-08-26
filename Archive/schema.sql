DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  author_id INTEGER NOT NULL,
  post_dated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  content TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

INSERT INTO user (username, password) values ('ajcltm', '1234');
INSERT INTO post (title, author_id, post_dated, content) values (
    'first article', 1, DATE(), 'hello world'
);

select a.id, a.title, b.username, a.post_dated, a.content from post as a join user as b on a.author_id == b.id;