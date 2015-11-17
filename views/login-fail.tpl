    
    % include ('header.tpl', title='Hola')
    
    <div class="login">
        <div class="login-form">

            <h1>
                Login
            </h1>

            <p class="login-form-error">
                % if failError != None:
                    {{!failError}} 
                    % #http://stackoverflow.com/questions/11779114/bottle-python-rendering-variable-as-text-and-not-html
                % end
            </p>

            <form action="/login" method="post">
                <div>
                    <label for="mail">
                        E-mail:
                    </label>
                    <input class="inputField" name="email" type="email" id="mail" placeholder="Your email" />
                </div>
                <div>
                    <label for="password">
                        Password:
                    </label>
                    <input class="inputField" name="password" placeholder="Password" type="password" />
                </div>
                
                <div class="button">
                    <button class="submitField" type="submit">Access account</button>
                </div>

                <p>
                    Don't you have an ccount? <a href="/register">Register!</a>
                </p>
            </form>
        </div>
    </div> 
    
    % include ('footer.tpl')
