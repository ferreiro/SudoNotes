import sqlite3

conn   = sqlite3.connect('notes.sqlite3')
conn.execute("PRAGMA foreign_keys = ON")

cursor = conn.cursor()

cursor.execute("insert into User values (NULL,'jorge@ferreiro.com', '123', 'ferreiro', 'Jorge', 'Garcia', '16/03/1995', 'Madrid', 0)");
cursor.execute("insert into Tag values ('Hello', 1, 1, '000000')");

cursor.execute("insert into User values (NULL,'test@example.com', '123', 'tomasso', 'Tommaso', 'Innocenti', '30/09/1991', 'Arezzo', 0)");
cursor.execute("insert into Notes values (NULL, 2, 'How to make pasta','how-make-pasta' ,'So. We have to call Luigi.', '16/03/2015', '16/03/2020', 1, 0)");
cursor.execute("insert into Tag values ('Hello', 2, 2, '000000')");

cursor.execute("insert into User values (NULL,'test1@example.com', '123', 'paco', 'Paco', 'Innocenti', '30/09/1991', 'Arezzo', 0)");
cursor.execute("insert into User values (NULL,'test2@example.com', '123', 'susana', 'Susana', 'Innocenti', '30/09/1991', 'Arezzo', 0)");

cursor.execute("Select * from Tag where Tag.UserID=1 and Tag.TagNameID='Hello'");
cursor.execute("Select * from User where User.UserID=1");
cursor.execute("Select DISTINCT Email from Tag join User on Tag.TagNameID='Hello' ");
cursor.execute("Select DISTINCT Email from Tag join User on Tag.TagNameID='Hello' ");

conn.commit()
cursor.close()
