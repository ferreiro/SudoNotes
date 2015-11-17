
	% if user != None:

		<div class="modal-Wrapper" id="reader-Wrapper">
			<div class="singleNote" id="reader">

				<div class="modal-close" id="reader-close">
					<span class="icon-close"></span>
				</div>
				
				<div class="modal-loader" id="reader-loader"></div>

				<div class="modal-Content" id="reader-Content">
					<h1 class="singleNote-Title" id="reader-Title">Title</h1>
					<p class="singleNote-Content" id="reader-Text">Content</p>
				</div>
				
			</div>
		</div>

		<div class="writeNote-button" id="writeNote">
			<span class="icon-mode_edit"></span>
		</div>
		
		<div class="modal-Wrapper" id="writer-Wrapper">
			<div class="singleNote" id="writer">

				<div class="modal-close" id="writer-close">
					<span class="icon-close"></span>
				</div>
				
				<div class="modal-loader" id="writer-loader"></div>

				<div class="modal-Content" id="writer-Content">


					<form action="/api/notes/create" id="createNewNote" method="POST"> 
						
						<!--<h1 class="writeNote-form-title">Write a note</h1>
						-->

						<div class="writeNote-form">

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
									<select name="colorNote">
										<option value="black">Black</option>
										<option value="red">Red</option>
										<option value="blue">Blue</option>
										<option value="green">Green</option>
										<option value="purple">Purple</option>
									</select>
								</div>	
						
							</div>

							<textarea class=" writeNote-form-title singleNote-Title" id="noteTitle" name="titleNote" type="text" placeholder="Title of your note" required></textarea> 
	 						
	 						<textarea id="noteContent" class="writeNote-form-Content singleNote-Content" name="contentNote" type="text" placeholder="Start writing your note..."></textarea>
							
							<div class="writeNote-form-sent">
								<input type="submit" class="writeNote-form-Sent submitField" value="Publish note"/> 
							</div>

						</div>
					</form>


				</div>
				
			</div>
		</div>
	%end


