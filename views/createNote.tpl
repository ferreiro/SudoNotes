% include ('header.tpl', title='Hola')
	

	<div class="SubHeader-Wrap">
		<div class="SubHeader">
			<h1 class="SubHeader-Name">
				<strong>
					% if editNote == True:
						Edit
					% else:
						Write
					%end
				</strong>
				note
			</h1>
		</div>
	</div>

		<style type="text/css">
			form {
				width: 500px;
				margin: 0 auto;
			}
			.note-Title {
				width: 100%;
				min-height: 100px;
				font-size: 100px;
				font-family: arial;
				border:0;
				outline: 0;
				background: transparent;
			}
			.note-Content {
				width: 100%;
				min-height: 200px;
				font-size:30px;
				font-family: arial;
				border:0;
				outline: 0;
				background: transparent;
			}
			.note-save {
				padding: 10px 20px;
				font-size: 20px;
				background: #f4f4f4;
				color: #000;
				border:0;
			}
		</style>

<div class="containter-wrapper">
	<div class="containter">			

		% if editNote == True:
		<form action="/update/{{note['NoteID']}}" method="POST"> 
		%else:
		<form action="/create" method="POST"> 
		%end 

			<div class="writeNote-form-options">

				<div class="writeNote-form-options-select">
					<select name="publishedNote">
					  <option value="1">Published</option>
					  <option value="0">Save as draft</option>
					</select>
				</div>	

				<div class="writeNote-form-options-select">
					<select name="privateNote">
					  <option value="1">Private</option>
					  <option value="0">Public</option>
					</select>
				</div>

				<div class="writeNote-form-options-select">
				% if colors != None: 
					% if editNote == True:
						<select name="colorNote">
							<option value="white">Change color</option>
						% for color in colors:
						  <option value="{{color['Name']}}">{{color['Name']}}</option>
						% end
						</select>
					%else:
						<select name="colorNote">
						% for color in colors:
						  <option value="{{color['Name']}}">{{color['Name']}}</option>
						% end
						</select>
					%end
				% end
				</div>

				% if editNote == True:
					Current color: {{note['Color']}} <br />
				% end
			</div>

			<div>
				%print note
				% if editNote == True:
					<input id="noteTitleTextarea" class="note-Title" name="titleNote" required="required" type="text" placeholder="Title..." value="{{note['Title']}}" />
				%else:
					<input id="noteTitleTextarea" class="note-Title" name="titleNote" required="required" type="text" placeholder="Note title" value="" />
				%end
			</div>
			<p>

				% if editNote == True:
					<textarea id="noteContent" class="note-Content" name="contentNote" required="required" type="text" placeholder="Start writing your note..." value="{{note['Content']}}">{{note['Content']}}</textarea>
				%else:
					<textarea id="noteContent" class="note-Content" name="contentNote" required="required" type="text" placeholder="Start writing your note..."></textarea>
				%end
				
			</p>

			<div class="writeNote-form-sent">
				<input type="submit" class="writeNote-form-Sent submitField" value="Publish note"/> 
			</div>

		</form>

		
		</div>
	</div>


% include ('footer.tpl')
