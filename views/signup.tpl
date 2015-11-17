% include ('header.tpl', title='Hola')

% if editUser == True:
<!-- <div class="containter-wrapper">
	<div class="containter">-->

<style type="text/css">
	.login:before {
		/*background: transparent;*/
	}
</style>

<div class="login" style="background-image: url(../images/profile.jpg);">
    <div class="login-form" style="width:400px;">
		<h1>Edit your information</h1>
		<form action="/profile/edit" method="POST">
%else:
<div class="login">
    <div class="login-form" style="width:400px;">
		<h1>Create your free account</h1>
		<form action="/register" method="POST">
%end 
	<p> 
		<label for="namesignup" class="uname" data-icon="u">Your name</label>

		% if editUser == True:
			<input  class="inputField" id="namesignup" name="namesignup" required="required" type="text" placeholder="Your name" % if editUser == True: value="{{user['Name']}}" %end />
		%else:
			<input  class="inputField" id="namesignup" name="namesignup" required="required" type="text" placeholder="Your name" />
		%end
	</p>
	<p> 
		<label for="surnamesignup" data-icon="u">Your surname</label>
		% if editUser == True:
			<input  class="inputField" id="surnamesignup" name="surnamesignup" required="required" type="text" placeholder="Your surname" value="{{user['Surname']}}" />
		%else:
			<input  class="inputField" id="surnamesignup" name="surnamesignup" required="required" type="text" placeholder="Your surname" />
		%end 
	</p>
	<p> 
		<label for="usernamesignup" class="username" data-icon="u">Your username</label>

		% if editUser == True:
			<p>Username can't be changed</p>
		%else:
			<input  class="inputField" id="usernamesignup" name="usernamesignup" required="required" type="text" placeholder="Username" />
		%end  
	</p>
	<p> 
		<label for="birthdaysignup" class="ubirthday" data-icon="u">Your birthday</label>
		
		% if editUser == True:
			<input  class="inputField" id="birthdaysignup" name="birthdaysignup" required="required" type="date" value="{{user['Birthday']}}" />
		%else:
			<input  class="inputField" id="birthdaysignup" name="birthdaysignup" required="required" type="date"/>
		%end  
	</p>
	<p> 
		<label for="citysignup" class="ucity" data-icon="u">Your city</label>
		
		% if editUser == True:
			<input  class="inputField" id="citysignup" name="citysignup" required="required" type="name" value="{{user['City']}}"/>
		%else:
			<input  class="inputField" id="citysignup" name="citysignup" placeholder="Your city" required="required" type="name"/>
		%end  
	</p>
	<p> 
		<label for="emailsignup" class="youmail" data-icon="e" > Your email</label>

		% if editUser == True:
			<p>Email can't be changed (for now).</p>
		%else:
			<input  class="inputField" id="emailsignup" name="emailsignup" required="required" type="email" placeholder="mysupermail@mail.com"/> 
		%end  
	</p>
	<p> 
		<label for="passwordsignup" class="youpasswd" data-icon="p">Your password </label> 

		% if editUser == True:
			<p>Passwords can't be changed (for now).</p>
		%else:
			<input  class="inputField" id="passwordsignup" name="passwordsignup" required="required" type="password" placeholder="eg. X8df!90EO"/>
		%end 
	</p>
	<p class="signin button"> 
		% if editUser == True:
			<input  class="submitField" type="submit" value="Update data"/> 
		%else:
			<input  class="submitField" type="submit" value="Sign up"/>
			<p class="change_link">  
				Already a member ?
				<a href="/login" class="to_register"> Go and log in </a>
			</p>
		%end 
	</p>
	
</form>

	</div>
</div>

    % include ('footer.tpl')
