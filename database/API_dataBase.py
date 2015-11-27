#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

dbfile = "./database/notes.sqlite3";
conn   = sqlite3.connect(dbfile);

def openCursor():
	global conn
	cursor = conn.cursor();
	return cursor;


def closeCursor(cursor):
	cursor.close();
 
#####
####GETTING USER OBJECTS
#####

def getUserbyEmailPassword(email, password):
	user   = None;
	cursor = openCursor();
	try:
		query = "Select * from User where User.Email='"+str(email)+"' And User.Password='"+str(password) + "'";
		cursor.execute(query); # Check if the email and password exists on our database
		user = cursor.fetchone(); # Get the returned object for the database
		closeCursor(cursor);
	except:
		print "Can't retrieve a user"

	return user;

def getUserbyUsername(username):
	user   = None;
	cursor = openCursor();
	try:
		query = "Select * from User where User.Username='"+str(username)+"'";
		cursor.execute(query); # Check if the email and password exists on our database
		user_tuple = cursor.fetchone(); # Get the returned object for the database
		user = usertupleToDictionary(user_tuple);
		closeCursor(cursor);
	except:
		print "Can't retrieve a user"

	return user;


def getUserbyEmail(Email):
	user   = None;
	cursor = openCursor();
	try:
		query = "Select * from User where User.Email='"+str(Email)+"'";
		cursor.execute(query); # Check if the email and password exists on our database
		user_tuple = cursor.fetchone(); # Get the returned object for the database
		user = usertupleToDictionary(user_tuple);
		closeCursor(cursor);
	except:
		print "Can't retrieve a user"

	return user;


def getUserbyID(id):
	user   = None;
	cursor = openCursor();
	try:
		query = "Select * from User where User.UserID='"+str(id)+"'";
		cursor.execute(query); # Check if the email and password exists on our database
		user_tuple = cursor.fetchone(); # Get the returned object for the database
		user = usertupleToDictionary(user_tuple);
		closeCursor(cursor);
	except:
		print "Can't retrieve a user"

	return user;


#####
####GETTING NOTES OBJECTS
#####

def getNotebyNoteID(NoteID):
	note   = None;
	cursor = openCursor();
	try:
		query = "Select * from Notes where Notes.NoteID="+str(NoteID);
		cursor.execute(query); # Check if the email and password exists on our database
		noteTuple = cursor.fetchone(); # Get the returned object for the database
		note = notetupleToDictionary(noteTuple);
		#print note;
		closeCursor(cursor);
	except:
		print "Can't get notes given a userID and NoteID"

	return note;

def getNotebyPermalink(Permalink):
	note   = None;
	cursor = openCursor();
	try:
		query = "Select * from Notes where Notes.Permalink='"+str(Permalink)+"'";
		#print query
		cursor.execute(query); # Check if the email and password exists on our database
		noteTuple = cursor.fetchone(); # Get the returned object for the database
		note = notetupleToDictionary(noteTuple);
		closeCursor(cursor);
	except:
		print "Can't retrieve a user"

	return note;

def getNoteby_Username_Permalink(Username, Permalink):
	note   = None;
	cursor = openCursor();
	try:
		query = "Select * from Notes join User where User.Username='"+str(Username)+"' And Notes.Permalink='"+str(Permalink)+"'";
		#print query
		cursor.execute(query); # Check if the email and password exists on our database
		noteTuple = cursor.fetchone(); # Get the returned object for the database
		note = notetupleToDictionary(noteTuple);
		closeCursor(cursor);
	except:
		print "Can't get notes by this UserID and Permalink"

	return note;

#####
####GETTING COLORS OBJECTS
#####
""" Get all the avaliable colors for our database """
def getColorsAvailable():
	availableColors = []; # array of dictionaries
	try:

		cursor = openCursor();
		query = "Select * from Colors";
		cursor.execute(query); # Check if the email and password exists on our database
		colors = cursor.fetchall(); # Get the returned object for the database
		
		for color in colors:
			colorDict = {
				'Name' : color[0],
				'Color': color[1]
			}
			availableColors.append(colorDict);

		closeCursor(cursor);
	except:
		availableColors = None
		print "Can't retrieve all the colors"

	return availableColors;

""" Passing a color name, it returns the hexadecimal representation on our database """
def colorToHexadecimal(colorName):
	hexadecimalColor = "222222"; # default color
	try :
		colors = [] # array of dicionaries
		colors = getColorsAvailable();

		for c in colors:
			if c['Name'] == colorName:
				return c['Color']; # Color in hexadecimal
	except:
		print "Color not found"
	
	return hexadecimalColor;

""" Get all the avaliable colors for our database """
def getColorFromNote(NoteID):
	color = "";
	cursor = openCursor();
	try:
		query = "Select Name from Colors join Notes where NoteID=" + str(NoteID);
		cursor.execute(query); # Check if the email and password exists on our database
		color = cursor.fetchone()[0]; # Get the returned object for the database
		
		closeCursor(cursor);
	except:
		print "Can't retrieve color for noteID"

	return color;


# FetchAll notes for a given user id
# Add all the notes returned by the query into a list

def validNotes(notes):
	return (notes != None);

# Convert a note as a tuple into a Dictionary and return it

def usertupleToDictionary(_tuple):
	if (type(_tuple) != tuple):
		return None;

	user = {} # Return a Dictionary with a NOTE

	try:
		user['UserID'] = _tuple[0]
		user['Email'] = _tuple[1]
		user['Password'] = _tuple[2]
		user['Username'] = _tuple[3]
		user['Name'] = _tuple[4]
		user['Surname'] = _tuple[5]
		user['Birthday'] = _tuple[6]
		user['City'] = _tuple[7]
		user['Premium'] = _tuple[8]
	except:
		user = None; # invalid. Return empty

	return user;

def notetupleToDictionary(_tuple):
	if (type(_tuple) != tuple):
		return None;
	
	note = {} # Return a Dictionary with a NOTE

	try:
		note['NoteID'] 		= _tuple[0]
		note['UserID'] 		= _tuple[1]
		note['Title'] 		= _tuple[2]
		note['Permalink'] 	= _tuple[3]
		note['Content'] 	= _tuple[4]
		note['CreatedAt'] 	= _tuple[5]
		note['EditedAt'] 	= _tuple[6]
		note['Published']	= _tuple[7]
		note['Private'] 	= _tuple[8]
		note['Color'] 		= _tuple[9]
	except:
		note = None;

	return note;

def getNotesByUserID(UserID):
	notes_arr = []; # Array of dictionary (with notes)
	cursor = openCursor();
	try:
		query = "Select * from Notes where Notes.UserID=" + str(UserID) + " ORDER BY CreatedAt DESC";
		#print query
		cursor.execute(query); # Check if the email and password exists on our database
		notes_tuples = cursor.fetchall(); # Get tuples returned by database
	
	except:
		print "Can't retrieve notes for a userID"

	try:
		# notes are tuples. So convert to dict and add to Notes array
		for n in notes_tuples:
			convertedNote = notetupleToDictionary(n); # tuple to dictionary
			#print convertedNote
			
			try:
				query = "Select * from Colors where Colors.Name='"+convertedNote['Color']+"'";
				cursor.execute(query);
				color = cursor.fetchone()
				convertedNote['ColorName'] = color[0]
				convertedNote['Color'] 	   = color[1]
			except:
				print "Color for a note doesn't match with the database"
			
			notes_arr.append(convertedNote); # Append dictionary
	except:
		print "Can't convert from tuple to dictionary"

	closeCursor(cursor);
	return notes_arr;

""" Create a user in the database if the user doesn't exist """

def createUser(user):
	try:
		cursor = openCursor();

		UserID   = None
		Email  	 = user['Email']
		Password = user['Password'];
		Username = user['Username'];
		Name 	 = user['Name'];
		Surname  = user['Surname'];
		Birthday = user['Birthday'];
		City 	 = user['City'];
		Premium  = user['Premium'];

		query = "Insert into User values(?,?,?, ?,?,?, ?,?,?)";
		cursor.execute(query, (UserID, Email, Password, Username, Name, Surname, Birthday, City, Premium));
		conn.commit();
		closeCursor(cursor);

		return True;

	except:
		return False;


def updateUser(userUpdated):
	try:
		cursor = openCursor();

		query  = "Update User SET "
		query += "Name ='" + str(userUpdated['Name']) + "',  ";
		query += "Surname ='" + str(userUpdated['Surname']) + "', ";
		query += "Birthday ='" + str(userUpdated['Birthday']) + "', ";
		query += "City ='" + str(userUpdated['City']) + "'";
		query += " where User.UserID=" + str(userUpdated['UserID']);

		cursor.execute(query);
		conn.commit();
		closeCursor(cursor);

		return True;

	except:
		return False;

""" Create a user in the database if the user doesn't exist """

def createNote(note):

	returnedNote = None;
	cursor = openCursor();

	try:
		entry  = ("NULL,");
		entry += str(note['UserID']) + ",";
		entry += ("'" + str(note['Title']) + "',");
		entry += ("'" + str(note['Permalink']) + "',");
		entry += ("'" + str(note['Content']) + "',");
		entry += ("'" + str(note['CreatedAt']) + "',");
		entry += ("'" + str(note['EditedAt']) + "',");
		entry += (str(note['Published']) + ",");
		entry += (str(note['Private']) + ",");
		entry += ("'" + str(note['Color']) + "'");

		cursor.execute("Insert into Notes values(" + entry + ")"); 

		note['NoteID'] = cursor.lastrowid; # IMPORTANT! Set the note id before returning. 

		conn.commit();
		closeCursor(cursor);

		return note;

	except:
		print "Problems inserting on the database";
		return None;

def updateNote(noteUpdated):
	cursor = openCursor();

	query  = "Update Notes SET "
	query += "Title ='" + str(noteUpdated['Title']) + "',  ";
	query += "Color ='" + str(noteUpdated['Color']) + "', ";
	query += "Content ='" + str(noteUpdated['Content']) + "', ";
	query += "Private =" + str(noteUpdated['Private']) + ", ";
	query += "Published =" + str(noteUpdated['Published']) + ", ";
	query += "EditedAt ='" + str(noteUpdated['EditedAt']) + "'";
	query += " where Notes.NoteID=" + str(noteUpdated['NoteID']);
	query += " and Notes.UserID=" + str(noteUpdated['UserID']);

	cursor.execute(query);
	conn.commit();
	closeCursor(cursor);

	return True; # Updated.

def deleteNote(NoteID):
	try:
		cursor = openCursor();
		query  = "delete from Notes where notes.NoteID=" + str(NoteID) + ""
		cursor.execute(query);
		conn.commit();
		closeCursor(cursor);
	except:
		return False; #print "somethings go wrong"

	return True; # We delete a note succesfully



def searchNotesFromUser(Keyword,UserID):
	if (Keyword == None or UserID == None):
		return [];

	MatchedNotes = []
	
	cursor = openCursor();
	query  = "select * from Notes where "
	query += "Notes.UserID="+str(UserID) + " ";
	query += " and ("
	query += "Notes.Title like '%"+ str(Keyword) +"%' ";
	query += " or Notes.Content like '%"+ str(Keyword) +"%' ";
	query += ")"

	cursor.execute(query);
	#print query

	for _tuple in cursor.fetchall():
		convertedNote = notetupleToDictionary(_tuple); # tuple to dictionary
		MatchedNotes.append(convertedNote)
		#print convertedNote

	closeCursor(cursor);
	return MatchedNotes
