% include ('header.tpl', title='Hola')

<div class="SubHeader-Wrap">
	<div class="SubHeader">
		<h1 class="SubHeader-Name">
			<strong>Private</strong> zone<br />
		</h1>
	</div>
</div>


<div class="containter-wrapper">
	<div class="containter">
		<style type="text/css">
			.Zero-NotesWrap:before {
				background-image:url(/images/empty2.jpg);
			}
		</style>
		<div class="Zero-NotesWrap">
			<div class="Zero-Notes">
				<h1 class="Zero-Notes-Title">
					You are trying to accessing a private zone. 

					% if user != None:
						<a href="/profile" style="color:#fff; text-decoration:underline;">Go to your profile</a>
					% else:
						<a href="/login" style="color:#fff; text-decoration:underline;">Login in</a>
						or
						<a href="/register" style="color:#fff; text-decoration:underline;">Create free account</a>
					% end	
				</h1>
			</div>
		</div>
	</div>
</div>

% include ('footer.tpl')

		