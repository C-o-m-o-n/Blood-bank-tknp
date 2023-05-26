import mysql.connector

mydb = mysql.connector.connect(
  host='containers-us-west-55.railway.app',
  #'database_host',
  port='6549',
  #'database_port'
  user='root',
  passwd='iHUPZcoYYUQ96En6chw2'
# 'database_password'#
  )

my_cursor = mydb.cursor()
my_cursor.execute("USE railway")
my_cursor.execute("""
CREATE TABLE users (
  id INTEGER PRIMARY KEY, 
  username VARCHAR(250),
  email VARCHAR(250),
  password VARCHAR(256),
  profile_pic VARCHAR(250),
  pic_file_path VARCHAR(256)
);
""")
my_cursor.execute("""
CREATE TABLE blog_post (
   id INTEGER PRIMARY KEY,
   title VARCHAR(250),
   content TEXT,
   date_posted DATETIME DEFAULT (NOW()),
   poster_id INTEGER,
   FOREIGN KEY (poster_id) REFERENCES users (id)
);
""")
my_cursor.execute("""
CREATE TABLE likes (
  id INTEGER PRIMARY KEY,
  username INTEGER,
  post_id INTEGER,
  date_posted DATETIME DEFAULT (NOW())
  FOREIGN KEY (username) REFERENCES users (id),
  FOREIGN KEY (post_id) REFERENCES blog_post (id)
);
""")

my_cursor.execute("""
CREATE TABLE comments (
  id INTEGER PRIMARY KEY,
  content TEXT,
  date_posted DATETIME DEFAULT (NOW());
  username im=INTEGER;
  post_id INTEGER,
  FOREIGN KEY (username) REFERENCES users (id),
  FOREIGN KEY (post_id) REFERENCES blog_post (id)
);
""")





# my_cursor.execute("""
# ALTER TABLE likes 
# MODIFY COLUMN username  INTEGER;
# """)
# my_cursor.execute("""
# ALTER TABLE comments
# ADD FOREIGN KEY (username) REFERENCES users (id);
# """)

# my_cursor.execute("SHOW TABLES")