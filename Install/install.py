import sqlite3

usersqlset = """
CREATE TABLE `Docker_Container` (
  `id` integer not null primary key autoincrement,
  `user_email` text NULL,
  `name` text NOT NULL,
  `docker_ID` text NOT NULL,
  `docker_Port` text NOT NULL,
  `token` text NOT NULL,
  `status` text NOT NULL,
  `os` text NOT NULL,
  `time` datetime NOT NULL
)
"""

with sqlite3.connect("Data/Hosting_Data.sqlite3") as hosting:
  user_sql = hosting.cursor()
  hosting.executescript(usersqlset)
  hosting.commit()
  hosting.close()

print('clear')