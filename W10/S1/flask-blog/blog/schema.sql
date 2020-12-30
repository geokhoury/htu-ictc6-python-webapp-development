DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

-- Create 'User' table
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

-- Create 'Post' table
CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

-- Create some dummy data

---- Create some users
INSERT INTO user (username, password)
VALUES ("bert", "1234");

INSERT INTO user (username, password)
VALUES ("cookie", "1234");

INSERT INTO user (username, password)
VALUES ("ernie", "1234");

---- Create some posts
INSERT INTO post (author_id, created, title, body)
VALUES (1, CURRENT_TIMESTAMP, "Post 1", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer pulvinar sapien sit amet nunc mollis, ut sagittis nunc venenatis. Maecenas finibus orci sit amet nisl tempus, at suscipit diam condimentum.");

INSERT INTO post (author_id, created, title, body)
VALUES (2, CURRENT_TIMESTAMP, "Post 2", "Mauris pharetra, felis in ornare aliquam, lectus nisl tristique lorem, ut pellentesque diam tortor quis lorem. Nulla pulvinar interdum quam, sit amet porttitor neque condimentum id.");

INSERT INTO post (author_id, created, title, body)
VALUES (3, CURRENT_TIMESTAMP, "Post 3", "Morbi sed iaculis dolor. Fusce at eros orci. Mauris eget pellentesque odio. Aenean interdum lectus libero, suscipit lacinia turpis lobortis et.");

INSERT INTO post (author_id, created, title, body)
VALUES (2, CURRENT_TIMESTAMP, "My Post", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer pulvinar sapien sit amet nunc mollis, ut sagittis nunc venenatis. Maecenas finibus orci sit amet nisl tempus, at suscipit diam condimentum.");

