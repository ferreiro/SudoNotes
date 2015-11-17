
searchIcon  = $('.Header-options-search-icon');
searchInput = $('#searchInput');

// Focus on search when "Search icon" is clicked
searchIcon.click(function() {
    searchInput.focus()
});

$('#noteTitleTextarea').focus()