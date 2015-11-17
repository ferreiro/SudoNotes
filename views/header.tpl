<!DOCTYPE html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>SuperNotes</title>
  <meta name="description" content="The HTML5 Herald">
  <meta name="author" content="SitePoint">

  <link href='https://fonts.googleapis.com/css?family=Raleway:400,500,700|Open+Sans:400,700,600|Roboto:400,300,500,700' rel='stylesheet' type='text/css'>
  <link rel="stylesheet" type="text/css" href="/css/normalize.css" />
  <link rel="stylesheet" href="/css/style.css">
  <link rel="stylesheet" href="/css/profile.css">
  <link rel="stylesheet" href="/css/nice-select.css">

  <link rel="stylesheet" type="text/css" href="/css/ns-default.css" />

  <link rel="stylesheet" href="/css/ns-style-growl.css">
  		<script src="js/modernizr.custom.js"></script>
  		<!--[if IE]>
    		<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
  		<![endif]-->
</head>
<body>

<!-- Import the modal boxes. Before the full page wrapper -->
% include ('modalBoxes.tpl') 

<!-- FullPageWrapper is used when opened modal box. In order to add a blurred effect on the background.-->

<div class="FullPageWrapper">

	<div class="Header-wrapper">
		<div class="Header">
			<div class="Header-logo">
				<a href="/">
					<p>SudoNotes</p>
				</a>
			</div>
			<div class="Header-options">

				% if user != None:
				<div class="Header-options-search">
					<form action="/search" id="SearchForm" method="POST">
						<span class="Header-options-search-icon icon-search"></span>
						<input id="searchInput" name="query" required="required" type="text" placeholder="Search by title or content..." />
					</form>
				</div>

				<div class="Header-options-createNote">
					<a href="/create" id="writeNoteHeaderButton"><p>Create note</p></a>
				</div>
				% end

				% if user == None:

				<div class="Header-options-button button-login">
					<a href="/login">
						<div class="Header-options-button-icon">
							<span class="icon-locked"></span>
						</div>
						<p class="Header-options-button-title">
							Login
						</p>
					</a>
				</div>

				<div class="Header-options-button button-register">
					<a href="/register">
						<div class="Header-options-button-icon">
							<span class="icon-enter"></span>
						</div>
						<p class="Header-options-button-title">
							Register
						</p>
					</a>
				</div>
				
				% end

				% if user != None:

					<%

						# import code for encoding urls and generating md5 hashes
						import urllib, hashlib
						
						# Set your variables here
						
						email 	= user['Email'];
						default = "images/default.png"
						size 	= 100
 						 
						# construct the url
						gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
						#gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
					%>
					
					<div class="Header-options-myprofile" id="dropdownMenu">
						<a href="/profile" class="Header-options-myprofile-resume" >
							<span class="Header-options-myprofile-resume-avatar">
								<img src="{{gravatar_url}}" />
							</span>
							<p class="Header-options-myprofile-resume-name">
								@{{user['Username']}}
								%#{{user['Name']}} 
								%#{{user['Surname']}}
								
							</p>
							<span class="Header-options-myprofile-dropdown">▾</span>
						</a>
					
						<ul class="Header-options-myprofile-menu">

							<li class="Header-options-myprofile-menu-list">
								<a href="/{{user['Username']}}">My notes</a>
							</li>
							<li class="Header-options-myprofile-menu-list">
								<a href="/profile">Profile</a>
							</li>
							<li class="Header-options-myprofile-menu-list">
								<a href="/profile/edit">Edit profile</a>
							</li>
							<li class="Header-options-myprofile-menu-list">
								<a href="/logout">Log out</a>
							</li>

						</ul>
					</div>
				%end

			</div>
		</div>
	</div>
	