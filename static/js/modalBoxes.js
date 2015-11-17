/////////////////////
// MODAL VARIABLES
/////////////////////

body = $('.FullPageWrapper');

readerWrapper = $('#reader-Wrapper'); // Modal box showed each time user click on a note.
reader 		  = $('#reader');
readerContent = $('#reader-Content');
readerContent_Title= $('#reader-Title');
readerContent_Text = $('#reader-Text');
readerLoader  = $('#reader-loader')
readerClose   = $('#reader-close');

writerWrapper = $('#writer-Wrapper'); // Modal box showed each time user click on a note.
writer 		  = $('#writer');
writerContent = $('#writer-Content');
writerContent_Form= $('#writer-Title');
writerLoader  = $('#writer-loader')
writerClose   = $('#writer-close');

writeNoteBtn  = $('#writeNote')

/////////////////////////
// UPDATE MODAL CONTENT
/////////////////////////

function deleteSingleNote(NoteID) {
	body.find($('#'+NoteID)).unwrap()
	delete $('#'+NoteID)
	console.log($('#'+NoteID).detach())
}
function updateReader(note) {
	// Use the box ide to get the text of title...
	readerContent_Title.html(note['Title']);
	readerContent_Text.html(note['Content']);
}


/////////////////////
// OPEN MODALS
/////////////////////

writeNoteBtn.click(function() {
	displayWriter();
});


function displayWriter() {

	body.addClass('blurredElement');
	body.css({ overflow:'hidden' }); // Scroll not available

	displayAvailableColors('/api/colors'); // Get avaiable colors from the database
	// alert(window.availableColors)
	writerWrapper.slideDown('medium', 'easeInOutQuint'); // Show the modal	
	
	$('#noteTitle').focus(); // Focus on the title to start writing

	return false;
}

function displayReader() {

	body.addClass('blurredElement'); // Blurred effect
	body.css({ overflow:'hidden' }); // Scroll not available
	
	reader.css({ top: (scrollY + 100) }); // Move modal box from top
	readerWrapper.fadeIn('medium', 'easeInOutElastic'); // Show the modal
	
	return false;
}

note = {
	'NoteID'	: '3',
	'UserID'	: '_tuple[1]',
	'Title'		: '_tuple[2]',
	'Permalink' : '_tuple[3]',
	'Content' 	: '_tuple[4]',
	'CreatedAt' : '_tuple[5]',
	'EditedAt' 	: '_tuple[6]',
	'Published'	: '_tuple[7]',
	'Private' 	: '_tuple[8]',
	'Color'		: '_tuple[9]'
}

/////////////////////
// CLOSE MODAL
/////////////////////

writerClose.click(function() { hideWriter('0'); });
readerClose.click(function() { hideReader(); });
closeModalsKeyboardPressed();

function hideWriter(time) {
	changeURL('#/');
	writerWrapper.slideUp('medium', 'easeInOutQuint'); // Hide the modal
	body.css({ overflow:'auto' }); // Scroll available again
	body.removeClass('blurredElement'); // Blurred effect
}

function hideReader() {
	changeURL('#/');
	readerWrapper.hide(0); // Hide the modal
	body.css({ overflow:'auto' }); // Scroll available again
	body.removeClass('blurredElement'); // Blurred effect
}

// Close the modals when ESC key is pressed

function closeModalsKeyboardPressed() {
	$(document).keyup(function(e) {
	    if (e.keyCode == 27) { // escape key maps to keycode `27`
	        hideWriter('slow');
	        hideReader();
	    }
	});
}

////////////////////////
// AUXILIAR FUNCTIONS
////////////////////////

function changeURL (Permalink) {
	window.location = String(Permalink);
} 




function createSingleNote(note, user) {
	
	console.log(note)

	user = {
		UserID   : '1',
		Email  	 : 'Email',
		Password : 'Password',
		Username : 'Username',
		Name 	 : 'Name',
		Surname  : 'Surname',
		Birthday : 'Birthday',
		City 	 : 'City',
		Premium  : 'Premium'
	}

	NoteID 		= note['NoteID'];
	NoteColor 	= note['Color'];
	NoteColorHEX = note['ColorHexadecimal']
	NoteTitle 	= note['Title'];
	NoteContent = note['Content'];
	NoteDate 	= note['CreatedAt'];
	// NoteDate = NoteDate.split(' ')[0];
	Username 	= user['Username'];
	Permalink 	= note['Permalink'];
		
	console.log(NoteColorHEX)

	try {
	    var html  = '<div class="Note-wrapper">';
    		html +=		'<div class="Note" id="' + NoteID +  '">';
    		html += 		'<div class="Note-Options">';
    		html += 			'<span class="Note-Options-link">';
    		html += 				'<div class="icon-cog"></div>';
    		html +=				'</span>';
    		html +=				'<ul class="Note-Options-dropDown">';
    		html +=					'<li><a href="/' + Username + '/' + Permalink + '/edit">';
    		html +=						'Edit Note'
    		html +=					'</a></li>';		
    		html +=					'<li class="Note-Options-delete"><a href="/delete/' + NoteID +'">';
    		html +=						'Delete'
    		html +=					'</a></li>';
    		html +=				'</ul>';
    		html +=			 '</div>';
    		html +=			 '<div class="Note-line-color" style="border-color:#' + NoteColorHEX + '"></div>'
    		html += 		 	'<div class="Note-link">';
    		html +=					'<a href="/' + Username + '/' + Permalink + '"></a>';
    		html +=				'</div>';
    		html +=			 '<h1 class="Note-Title" style="color:#' + NoteColorHEX + '">'  + NoteTitle.substring(0, 60) + '</h1>';
    		html +=			 '<p class="Note-Content">' + (NoteContent.substring(0, 120) + '...' + '</p>');
    		html +=			 '<div class="Note-Metada-Wrapper">';
    		html +=			 	'<div class="Note-Metada">';
    								if (note['Published'] == 1) {
    									html += '<span class="Note-Private"><b>Published </b>' + NoteDate + '</span>';
    								}
    								else {
    									html += '<span class="Note-Private"><b>Draft (?)</b></span>';
    								}

    								if (note['Private']){
    									html += '<span class="Note-Private"><b>Private</b></span>'
    								}
    								else {
    									html += '<span class="Note-Private"><b>Public (?)</b></span>'; 
    								}										
    		html +=					'<span>-</span>';
    		html +=				'</div>';
    		html +=			'</div>';
    		html +=		'</div>';
    		html += '</div>';<!-- Fin de una single note -->
	}
	catch(err) {
		alert(message)
	}
	
	return html;
}	


////////////////////////////////////////
// ARRAYS OF OBJECTS TO INTERACT WITH //
// Adding click actions and more
////////////////////////////////////////

$( ".Note-wrapper" ).each(function clickableNote( index ) {
	
	var Note 	= $(this) // Local variable get from the ARRAY
	  , NoteID 	= $(this).find('.Note').attr('id')
	  , NoteOptions  = Note.find('.Note-Options')
	  , dropdownMenu = Note.find('.Note-Options-dropDown')
	  , dropdownMenuClass = 'Note-Options-dropDown-display'

	/////////////////////////////////////////////////////////
	// ADD actions when click on some layers for the object /
	/////////////////////////////////////////////////////////

	// Open Object: When user clicks on this layer,
	// Opens a modal box with the updated data retrieved
	// from the API.

	$(".Note-link", this).click(function(e) {
		
		API_URL 	= '/api/notes/' + String(NoteID)
		noteTitle 	= Note.find('.Note-Title').html()
		noteContent = Note.find('.Note-Content').html()

		getNoteAndUpdate(API_URL); // Get note from API and update content

		return false;
	});

	// Delete Button: When user clicks this object,
	// A modal box will be opened. If the user acceps
	// it deletes an object.

	$('.Note-Options-delete', this).click(function(e) {
		API_URL = 'api/notes/delete/' + String(NoteID);
		if (confirm("Are you sure you want to delete this note?")) {
			deleteNote(API_URL); // Delete the note given by the url
		}
		return false;
	}); 

	// Show DropdownMenu: when clicks on this layer
	// Opens/Closes a dropdown menu with different options.

	$(".Note-Options-link", this).click(function(e) {
		dropdownMenu.toggleClass(dropdownMenuClass);
		return false;
	});

});

/////////////////////
// API QUERIES
/////////////////////

// Get the note via api
// process the form
$('form#createNewNote').submit(function(event) {
	event.preventDefault();
	note = $("#createNewNote").serialize();
	createNoteViaAPI(note,'/api/notes/create');
	return false;
});


function createNoteViaAPI(note, url) {

	writerLoader.fadeIn(100);

    // We pass a POST petition to /contacta
    // with the data "dataForm"
    $.ajax({
        type        : 'POST',       // define the type of HTTP verb we want to use (POST for our form)
        url         : url, // the url where we want to POST
        data        : note,     // our data object
        dataType    : 'json',       // what type of data do we expect back from the server
        encode      : true
    })
    .done(function(note) {  

    	message = '<p>'+ note['message'] +'</p>';
    	
    	try {
    	    // create the notification
        	notification = new NotificationFx({
        		message : message,
        		layout : 'growl',
        		effect : 'genie',
        		type : 'notice', // notice, warning or error
        		onClose : function() {
        			//bttn.disabled = false;
        		}
        	});
        	notification.show();
    	}
    	catch(err) {
    		alert(message)
    	    console.log(err);
    	}
    	

    	// Done means the page could connect to the url to make the query.    
        if (!note['error']) {

        	hideWriter(0)
        	writerLoader.fadeOut(200);

        	user = {}
        	newHTMLNote = createSingleNote(note, user);

        	if ($('.Zero-NotesWrap').length > 0) {
        		$('.Zero-NotesWrap').hide(0);
        		$('.Profile-Header-wrap').show(0);
        	}

			setTimeout(function() {
				$('.notes-container').prepend(newHTMLNote);
				// $('.notes-container').hide(0).prepend(newHTMLNote).delay(300).fadeIn(1000);
			}, 1000);

        }
    
     })
    .fail(function(response) {
        alert("Problems creating your note... Try later")
    })
    .always(function(response) {
       writerLoader.fadeOut(200);
    });
   
}


// Get all the colors available in our system

function displayAvailableColors(apiURL) {
	try {
		$.getJSON( apiURL, function( json ) {
			window.availableColors = json;
		})
		.error(function() {
			console.log("No available colors")
		})
		.complete(function() { 
			
		});
	}
	catch (err) {
		console.log(err)
	}
}

// Get the note via api

function getNoteAndUpdate(apiUrl) {

	readerContent.hide(0);
	readerLoader.fadeIn(200);

	$.getJSON( apiUrl, function( note ) {
		if (note['valid'] == "true") {	

			newUrl  = "#/";
			newUrl += note['Permalink'];
			newUrl += "/";
			newUrl += note['NoteID'];

			updateReader(note); // Update reader data with the returned object
			changeURL(newUrl);
			displayReader(); // Show specific reader for this object
		}
		else{
			message = '<p>'+ note['status'] +'</p>';

			try {
			    // create the notification
		    	notification = new NotificationFx({
		    		message : message,
		    		layout : 'growl',
		    		effect : 'genie',
		    		type : 'notice', // notice, warning or error
		    		onClose : function() {
		    			//bttn.disabled = false;
		    		}
		    	});
		    	notification.show();
			}
			catch(err) {
				alert(message)
			    console.log(err);
			}
		}
		

	})
	.error(function() {
		message = '<p>Sorry... We couldn\'t retrieve information for that note... Try later</p>';

		try {
		    // create the notification
	    	notification = new NotificationFx({
	    		message : message,
	    		layout : 'growl',
	    		effect : 'genie',
	    		type : 'notice', // notice, warning or error
	    		onClose : function() {
	    			//bttn.disabled = false;
	    		}
	    	});
	    	notification.show();
		}
		catch(err) {
			alert(message)
		    console.log(err);
		}

	})
	.complete(function() { 
		readerLoader.fadeOut(0);
		readerContent.fadeIn(200);
	});
}


function deleteNote(apiUrl) {

	readerContent.hide(0);
	readerLoader.fadeIn(200);

	console.log(apiUrl)

	$.getJSON( apiUrl, function( note ) {
		var message = note['status']
		  , deleted = note['deleted'];

		 console.log(note)
		message = '<p>'+ note['status'] +'</p>';

		// create the notification
		notification = new NotificationFx({
			message : message,
			layout : 'growl',
			effect : 'genie',
			type : 'notice', // notice, warning or error
			onClose : function() {
				//bttn.disabled = false;
			}
		});
		notification.show();

		if (deleted == "true") { 
			deleteSingleNote(note['NoteID']);
		}
		

	})
	.error(function() {
		//alert("Sorry... We couldn't delete that note... Try later")
	})
	.complete(function() { 
		readerLoader.fadeOut(200);
		readerContent.fadeIn(200);
	});
}








