% include ('header.tpl', title='Hola')

<style type="text/css">
	body {
		
	}
	/*
	.containter-wrapper {
		position: relative;
	}
	body:after {
		width: 100%;
		height: 100%;
		position: absolute;
		z-index: -1;
		content: '';
		top: 0;
		bottom: 0;
		left: 0;
		background: rgba(0,0,0,.6);
	}
	body:before {
		width: 100%;
		height: 100%;
		position: absolute;
		z-index: -2;
		content: '';
		top: 0;
		bottom: 0;
		left: 0;
		background: rgba(0,0,0,.5);
		background:#000 url(/images/profile.jpg);
		-webkit-filter: blur(10px);
		-moz-filter: blur(10px);
		-o-filter: blur(10px);
		-ms-filter: blur(10px);
		filter: blur(10px);
 
	}*/
</style>

<div class="Profile-Header-wrap">
	<div class="Profile-Header">	
		<h1 class="Profile-Header-Name">
			<strong>{{user['Name']}} {{user['Surname']}}</strong><br />
			<i style="font-size:22px;">@{{user['Username']}}</i>
		</h1>

		<div class="Profile-edit-button">
			<a href="/profile/edit">Edit my profile</a>
		</div>
	</div>
</div>

<div class="containter-wrapper">
	<div class="containter">	

		<div class="Profile-User-Description-Wrap">
			<div class="Profile-User-Description">
				<strong>User information</strong>
				<ul class="Profile-Description-metadata">
					<li class="Profile-Description-metadata-list">
						<b>City:</b> {{user['City']}}</li>
					<li class="Profile-Description-metadata-list">
						<b>Email:</b> {{user['Email']}}
					</li>
					<li class="Profile-Description-metadata-list">
						<b>Birthday:</b> {{user['Birthday']}}
					</li>
					<li class="Profile-Description-metadata-list">
						<b>Premium:</b> {{user['Premium']}}
					</li>
				</ul>
			</div>

			<div class="Profile-User-Description">
				<strong>Location</strong>
				<%
					map = "https://maps.googleapis.com/maps/api/staticmap?center="
					map += str(user['City']);
					#map += "Brooklyn+Bridge,New+York,NY";
					map += "&zoom=13";
					map += "&size=600x300";
					map += "&maptype=roadmap";
					map += "&markers=color:blue%7Clabel:S%7C40.702147,-74.015794"
					map += "&markers=color:green%7Clabel:G%7C40.711614,-74.012318"
					map += "&markers=color:red%7Clabel:C%7C40.718217,-73.998284"
					map += "&key=AIzaSyAuT5YTvhsLCfbLsu2TUxIQ7c7u8ga7ot8"
				%>
				<img src="{{map}}" width="100%"/>
			</div>
		</div>

		<div class="Profile-User-Notes-Wrap">
			<div class="Profile-User-Notes">
				<strong>Drafs: notes don't published yet</strong>
				<ul class="Profile-draft-all">
					%if len(notes) >= 0:
						<% totalDrafts = 0;
						for n in notes:
							if (n['Published'] == 0):
								totalDrafts += 1; %>
								<li class="Profile-draft-entry">
									<a href="/{{user['Username']}}/{{n['Permalink']}}">
										{{n['Title']}}
									</a>
									-
									<a href="/{{user['Username']}}/{{n['Permalink']}}/edit">
										Continue writing
									</a>
								</li>
							%end
						%end
					% end
				</ul>

				% if totalDrafts == 0: 
					<p>You don't have any draft <a href="/create">Start writing a new note!</a></p>
				%end
			</div>

			<div class="Profile-User-Notes" style="margin-top:20px;">
				<strong>Published notes</strong>
				<ul class="Profile-draft-all">
					% print len(notes)
					%if len(notes) == 0:
						<p>You don't have any note <a href="/create">Write one!</a></p>
					%else:
						% for n in notes:
							% if (n['Published'] == 1):
								<li class="Profile-draft-entry">
									<a href="/{{user['Username']}}/{{n['Permalink']}}">
										{{n['Title']}}
									</a>
									-
									<a href="/{{user['Username']}}/{{n['Permalink']}}/edit">
										Edit note
									</a>
								</li>
							%end
						%end
					% end
				</ul>
				<a href="/{{user['Username']}}/">See all your published notes ></a>
			</div>
		</div>


	</div>
</div>


% include ('footer.tpl')