#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import request, route, run, template, response, static_file;
from datetime import datetime
from passlib.hash import sha256_crypt

import database_API as db # Module for database connection
import random
import json
import re

#####################################
########## ASSETS ROUTING ###########
#####################################

@route('/views/<filepath:path>')
def file_stac(filepath):
    return static_file(filepath, root="./views")

@route('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/')

@route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/')

@route('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/')

@route('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/')

#################################
########## ENCRYPTION ###########
########## SECURITY   ###########
#################################

def encryptPassword(Password):
	hash = sha256_crypt.encrypt(Password)
	return hash

def verifyPassword(Password, hash):
	return sha256_crypt.verify(Password,hash);

def setCookiesSessionUser(user):

	response.set_cookie("Email", user['Email'], secret="secret123", max_age=100500);
	response.set_cookie("UserID", user['UserID'], secret="secret123", max_age=100500);

def deleteCookiesSessionUser():

	response.set_cookie("Email", '');
	response.set_cookie("UserID", '');

def checkCookiesSessionUser():

	sessionUser   = None;
	sessionEmail  = request.get_cookie("Email", secret="secret123")
	sessionUserID = request.get_cookie("UserID", secret="secret123")

	if (sessionEmail == None or sessionUserID == None):
		return None; # Cookies doesn't match

	identifiedUser = db.getUserbyID(sessionUserID); # Return identified user. If the user was removed from our system, will return null user.
	return identifiedUser;

#################################
######## AUXILIAR FUNC ##########
#################################

### Do not move from here

""" Eliminate sql injection and other things like ' """
def cleanContent(content):
	truncated = str(content);

	if len(truncated) >= 3002:
		truncated[:3000];

	#content = str(request.forms.get('contentNote'));
	#content = re.sub('[^a-zA-Z0-9 \n\.]', '', str(content)); # content wihtout special characters
	
	#cleanTitle = content.replace("'", "\'");

	return truncated

def cleanTitle(title):
	truncated = str(title);
	
	if len(title) >= 152:
		truncated[:150];

	#cleanTitle = re.sub('[^a-zA-Z0-9 \n\.]', '', str(title)); # Title without special characters
	#cleanTitle = title.replace("'", "\'");
	#cleanTitle = cleanTitle.replace(' ', '-');
	return truncated

def generatePermalink(title):
	randNumList = random.sample(range(1, 100), 4); #10 digits rand num
	randomNumber = ''.join(str(e) for e in randNumList);
	
	truncated = str(title)
	if len(truncated) >= 30:
		truncated = truncated[:30] # Truncate Titles if greater than 30

	permalink = truncated + '-' + str(randomNumber);
	return permalink;

def getToday():
	today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	formatedToday = today.replace(" ", "-")
	formatedToday = formatedToday.replace(":", "-");
	return formatedToday

#################################
######### REDIRECTIONS ##########
#################################

def redirect(url):
	response.status = 303
	response.set_header('Location', '/'+ url);

def redirectHome():
	response.status = 303
	response.set_header('Location', '/');

def redirectLogin():
	response.status = 303
	response.set_header('Location', '/login');

def redirectPrivateZone():
	sessionUser = checkCookiesSessionUser();
	return template('privateZone', user=sessionUser); # Private note. Guest can't read this note

def redirectToProfile(username):
	response.status = 303
	sessionUser = checkCookiesSessionUser();

	if (sessionUser == None): # User exists
		return redirectLogin();
	else:
		return response.set_header('Location', '/'+ str(username));

def redirectLoginSuccess():
	sessionUser = checkCookiesSessionUser();
	#print sessionUser
	if sessionUser != None:
		response.status = 303
		response.set_header('Location', '/'+ str(sessionUser['Username']));

#################################
######## LOGIN / LOGOUT #########
#################################

@route('/')
def loginWindow():
	sessionUser = checkCookiesSessionUser();

	if sessionUser != None:
		return redirectToProfile(sessionUser['Username']);

	return template('home', user=sessionUser); #Show login screen

@route('/login')
def loginWindow():
	sessionUser = checkCookiesSessionUser();

	if sessionUser != None:
		return redirectToProfile(sessionUser['Username']);

	return template('login', user=sessionUser); #Show login screen

@route('/login', method='POST')
def login():
	sessionUser = checkCookiesSessionUser();

	email    = request.forms.get('email');
	password = request.forms.get('password');
	user 	 = db.getUserbyEmail(email);
	
	if user == None:
		return template('login-fail', user=None, failError="<span>User not registered on our system.</span><span>Want a free acount? <a href='/register'>Create yours</a></span>");
		return "There's no any user with that email. <p><a href='/login'>Try again </a></p>";

	if verifyPassword(password, user['Password']):
		setCookiesSessionUser(user); #password verified. Set the cookies for the session
		return redirectToProfile(user['Username']);
	else:
		return template('login-fail', user=None, failError="Your email/password doesn't match");
		return "Your password is not correct <p><a href='/login'>Try again </a></p>";

@route('/logout')
def closeOpenSession():
	sessionUser = checkCookiesSessionUser();
	
	if (sessionUser != None): # Delete if user connected
		deleteCookiesSessionUser();
	
	return redirectHome();

#####################################
############# REGISTER ##############
#####################################
 
@route('/register')
def register():
	sessionUser = checkCookiesSessionUser();

	if (sessionUser != None):
		return redirectHome();

	return template('signup', editUser=False, user=sessionUser); #Show login screen

@route('/register', method='POST')
def registerUserDatabase():
	sessionUser = checkCookiesSessionUser();

	if (sessionUser != None):
		return redirectHome();

	# Dictionary with information for new user (following database model)
	
	password = encryptPassword(request.forms.get('passwordsignup'))

	newUser = {
		"UserID": None,
		"Email" : request.forms.get('emailsignup'),
		"Password" : password,
		"Name": request.forms.get('namesignup'),
		"Surname": request.forms.get('surnamesignup'),
		"Username": request.forms.get('usernamesignup'),
		"Birthday": request.forms.get('birthdaysignup'),
		"City": request.forms.get('citysignup'),
		"Premium": 0
	}

	created =  db.createUser(newUser);
	if created: # user created successfully
		return template('signup-success', user=sessionUser);
	else:
		return template('signup-fail', user=None);

#####################################
############## PROFILE ##############
#####################################

#Show the profile for a given user. 
#Dashboard with the Published notes, draft and more stuff... """

@route('/profile')
def userProfile():
	sessionUser = checkCookiesSessionUser();

	if (sessionUser == None):
		return redirectHome();

	user  = db.getUserbyID(sessionUser['UserID']);
	notes = db.getNotesByUserID(user['UserID']);
 
	if user != None:
		return template("profile", user=user, notes=notes);
	else:
		return redirectLogin();

@route('/profile/edit')
def showFormToEditUser():
	sessionUser = checkCookiesSessionUser();
	if (sessionUser == None):
		return redirectHome();

	user = db.getUserbyID(sessionUser['UserID']); # Get a user dictionary

	if user != None and sessionUser['UserID'] == user['UserID']: # if the user exists.
		return template("signup", user=user, editUser=True);
	else:
		return redirectHome();

@route('/profile/edit', method="POST")
def editSessionUser():
	sessionUser = checkCookiesSessionUser();
	
	if (sessionUser == None):
		return redirectLogin();

	user = db.getUserbyID(sessionUser['UserID']);
	
	user['Name'] 	 = request.forms.get('namesignup');
	user['Surname']  = request.forms.get('surnamesignup');
	user['Birthday'] = request.forms.get('birthdaysignup'); 
	user['City'] 	 = request.forms.get('citysignup'); 
 	
	if db.updateUser(user):
		notes = db.getNotesByUserID(user['UserID']);
		return template("profile", notes=notes, user=user);
	else:
		return template("profile-update-fail", user=sessionUser);

#####################################
############### NOTES ###############
#####################################
 
 ##### Write a note

@route('/create')
@route('/create/')
def createNoteForm():
	sessionUser = checkCookiesSessionUser();

	if (sessionUser == None):
		return redirectLogin();

	note = {} # Empty dictionary. Because template for createNote is used also by Edit Note
	colors = db.getColorsAvailable(); # Get colors on our database.
	return template('createNote', note=note, colors=colors, editNote=False, user=sessionUser)

##### DISPLAY: all the notes for a given username

@route('/<username>')
@route('/<username>/')
def profile(username):
	sessionUser = checkCookiesSessionUser();
	
	if (sessionUser == None):
		return redirectHome();

	user = db.getUserbyUsername(username);

	if user != None and user['UserID'] == sessionUser['UserID']: # if user and session is the same as the query user
		notes = db.getNotesByUserID(user['UserID']);
		return template('notes', searchTemplate=False, notes=notes, user=user); # Show the notes for that user!
	else:
		return redirectPrivateZone(); # Users are not ALLOWED 
	
# DISPLAY BY USERNAME/PERMALINK:
# Show a single note given a username and the permalink

def createnewNote(api):
	sessionUser = checkCookiesSessionUser();

	errorNote = {
		# only for the api...
		"error"     : True,
		"message"   : "You're not allowed to do this...",
	}

	if (sessionUser == None):
		if (api):
			response.content_type = 'application/json';
			return json.dumps(errorNote);
		else:
			return template('login', user=None)

	title 	= cleanTitle(request.forms.get('titleNote'));
	content = cleanContent(request.forms.get('contentNote'));
	permalink = generatePermalink(title);
	today 	= getToday();
	color 	= request.forms.get('colorNote');
	private = int(request.forms.get('privateNote'));
	published = int(request.forms.get('publishedNote'));

	newNote = {
		# only for the api...
		"error"     : True,
		"message"   : "Note was not created successfully",

		"NoteID" 	: None,
		"UserID" 	: sessionUser['UserID'],
		"Title" 	: title, # Truncate title to 200 words
		"Permalink" : permalink,
		"Content" 	: content, # Truncate title to 200 words
		"CreatedAt" : today,
		"EditedAt" 	: today,
		"Published" : published,
		"Private" 	: private,
		"Color" 	: color
	}

	createdNote = db.createNote(newNote);

	if createdNote != None:
		if api:
			response.content_type = 'application/json';

			colorToHEX = db.colorToHexadecimal(createdNote['Color']); 
			
			#print colorToHEX

			newNote['ColorHexadecimal'] = colorToHEX;
			newNote['message'] = "Note created successfully"
			newNote['error'] = False;

			return json.dumps(newNote);
		else:
			return template('note-created', user=sessionUser);
			response.status = 303
			response.set_header('Location', '/'+ sessionUser['Username']);
	else:
		if api:
			response.content_type = 'application/json';
			return json.dumps(newNote);
		else:
			return template('createNote', note=newNote, colors=None, user=sessionUser, editNote=False)

@route('/create', method="POST")
def createnewNoteAux():
	api = False;
	return createnewNote(api);

@route('/api/notes/create', method="POST")
def getApiNotes():
	api = True;
	return createnewNote(api);

### UPDATE GET: Note by USERNAME Permalink
@route('/<Username>/<Permalink>/edit', mehod="GET")
def displayNoteToBeupdated(Username, Permalink):
	sessionUser = checkCookiesSessionUser();
	if sessionUser == None:
		return template('login', user=sessionUser)

	note = db.getNoteby_Username_Permalink(Username, Permalink);

	if note == None:
		return redirectHome();

	if sessionUser['UserID'] == note['UserID']:
		colors = db.getColorsAvailable(); # get all the available colors
		return template('createNote', note=note, colors=colors,user=sessionUser, editNote=True)
	
	return redirectPrivateZone(); # Private note. Guest can't read this note

### UPDATE POST: Note by USERNAME Permalink

@route('/update/<NoteID>', method="POST")
def updateNotebyID(NoteID):
	sessionUser = checkCookiesSessionUser();
	if (sessionUser == None):
		return redirectHome();
	
	newTitle 		 = request.forms.get('titleNote');
	newContent 		 = request.forms.get('contentNote');
	updatedTime 	 = datetime.now().strftime('%Y-%m-%d %H:%M:%S');

	#Update fields for the note before inserting into database..
	note 			 = db.getNotebyNoteID(NoteID); #get note object from the previous note.
	note['Title'] 	 = newTitle;
	note['Content']  = newContent;
	note['EditedAt'] = updatedTime;
	note['Color']    = request.forms.get('colorNote');
	note['Private']  = request.forms.get('privateNote');
	note['Published']= int(request.forms.get('publishedNote'));

	if db.updateNote(note): #update the note into the database.

		response.status = 303
		user = db.getUserbyID(note['UserID'])

		response.set_header('Location', '/'+user['Username']+'/'+note['Permalink']);
		return template('singleNote', note=note, user=user); #Show login screen
		return template('singleNote', note=note, user=user);
	else:
		#problems updating note.
		return template('error', user=sessionUser)

@route('/delete/<NoteID>')
def deleteNoteID(NoteID):
	sessionUser = checkCookiesSessionUser();
	if (sessionUser == None):
		return template('login')

	note = db.getNotebyNoteID(NoteID);

	if (note == None): 
		return redirectHome(); # The note doesn't exist on our database 

	userID_note    = note['UserID'];
	userID_session = sessionUser['UserID'];

	if (userID_note == userID_session):
		if (db.deleteNote(NoteID)):
			return template('note-deleted', user=sessionUser);
		else:
			return "Problems deleting that note<a href='/'>Go to your profile</a>"
			return template('error')
	else:
		return redirectPrivateZone(); # Private note. Guest can't read this note

@route('/<Username>#/<Permalink>')
@route('/<Username>/<Permalink>')
def displayNote(Username, Permalink):
	sessionUser = checkCookiesSessionUser();

	note = db.getNoteby_Username_Permalink(Username, Permalink);

	if (note == None):
		return redirectHome(); #return "The note you're trying to read dont exist";

	if sessionUser == None: 
		if int(note['Private']) == 0: #Gues user. Only shows the note if is public
			return template('singleNote', note=note, user=sessionUser);
	if sessionUser != None: # For logged in users. They can read "Public" notes and those notes owned by them
		if int(note['Private']) == 0 or sessionUser['UserID'] == note['UserID']: #la NOTa es publica o el usuario esta conectado
			return template('singleNote', note=note, user=sessionUser);
	
	return redirectPrivateZone(); # Not allowd to see this content

### Search notes by title and content

@route('/search', method='POST')
@route('/search?q=<Keyword>', method="POST")
#@route('/search/<name>', method='GET')
def searchOnNotes():
	sessionUser = checkCookiesSessionUser();
	if (sessionUser == None):
		return template('login', user=None)

	user = db.getUserbyID(sessionUser['UserID'])

	if (user != None):
		Keyword = request.forms.get('query');
		notes = db.searchNotesFromUser(Keyword, sessionUser['UserID']);
		return template('notes', Keyword=Keyword, searchTemplate=True,  notes=notes, user=user);
	else:
		return redirectHome();


#####################################
#####################################
################ API ################
#####################################
#####################################


@route('/api/notes/delete/<NoteID>', mehod="GET")
def deleteNoteID(NoteID):
	sessionUser = checkCookiesSessionUser();

	response.content_type = 'application/json';
	returnedMessage = {
		"NoteID" : NoteID,
		"valid" : "false",
		"deleted": "false",
		"status" : "You're not allowed to do this action"
	}

	if (sessionUser == None):
		return json.dumps(returnedMessage);

	note = db.getNotebyNoteID(NoteID);

	if (note == None): 
		returnedMessage["deleted"] = "false";
		returnedMessage["status"]  = "This note doesn't exist on our system or has changed location";
		return json.dumps(returnedMessage); # The note doesn't exist on our database 

	userID_note    = note['UserID'];
	userID_session = sessionUser['UserID'];

	if (userID_note == userID_session):
		if (db.deleteNote(NoteID)):
			returnedMessage['valid'] = 'true';
			returnedMessage['deleted'] = "true";
			returnedMessage['status'] = "We have deleted your note!";
		else:
			returnedMessage['deleted'] = "false";
			returnedMessage['status'] = "You're not allowed to delete this note.";

	return json.dumps(returnedMessage);

# Get available colors
@route('/api/colors', method='GET')
def getColorsAvailable():
	colors = [];
	response.content_type = 'application/json';

	colors = db.getColorsAvailable();
	#print colors;

	return json.dumps(colors);

# Get available colors for a given user
@route('/api/<user/>colors', method='GET')
def getAvailableColorsUser():
	response.content_type = 'application/json';
	return { "error" : "true" }

@route('/api/notes/<NoteID:int>', method='GET')
@route('/api/notes/<NoteID:int>', method='POST')
def getNodeByID_api(NoteID):
	sessionUser = checkCookiesSessionUser();

	errorNote  = { "NoteID" : NoteID, "valid": "false", "status": "notExist"}
	note 	   = db.getNotebyNoteID(NoteID);

	response.content_type = 'application/json';

	if (note != None):
		if  note['Private'] == 0 or (note['Private'] == 1 and sessionUser['UserID'] == note['UserID']):
			# Is a public note or session user is the owner.
			note['valid'] = "true";
			note['status'] = "OK";
			return json.dumps(note); # return a not empty note.
		else:
			errorNote['valid'] = "false";
			errorNote['status'] = "You don't permissions to see this content. Sorry.";
	else:
		errorNote['valid'] = "false";
		errorNote['status'] = "The note you're trying to read doesn't exist or was removed.";

	return json.dumps(errorNote); # return error note.

	if (sessionUser['UserID'] != note['UserID']):
		errorNote['status'] = "You don't permissions to see this content. Sorry.";
		return json.dumps(errorNote);
	elif (note == None):
		errorNote['status'] = "The note you're trying to read doesn't exist or was removed.";
		return json.dumps(errorNote);
	else:
		# At this point the user is the correct one and the note is not None
		note['valid'] = "true";
		errorNote['status'] = "OK";
		response.content_type = 'application/json'
		return json.dumps(note);



run(host='127.0.0.1', port=3000);