% include ('header.tpl', title='Hola')

<script type="text/javascript">
   window.setTimeout(function(){

       // Move to a new location or you can do something else
       window.location.href = "/";

   }, 1200);
</script>

<div class="SubHeader-Wrap">
	<div class="SubHeader">
		<h1 class="SubHeader-Name">
			<strong>Note created!</strong><br />
			<a style="color:#fff;">
				We are redirecting to your notes.
			</a>
		</h1>
	</div>
</div>

% include ('footer.tpl')

		
