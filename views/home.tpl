    
    % include ('header.tpl', title='Hola')
    
    <style type="text/css">
    .Header-wrapper {
        background: transparent;
    }
    .Header-options-button {
        background: transparent !important;
    }
    </style>
    
    <div class="home">
        <div class="home_content">
            <div class="info">
                <h1>
                    Welcome to SudoNotes!
                </h1>
                <p>
                    The easiest way to keep all your ideas,<br /> notes and projects in one place.
                </p>

                <a href="/login" class="toLogin">
                    Login
                </a>
                <a href="/register" class="toRegister">
                    Register
                </a>
            </div>
        </div>
    </div>


    % include ('footer.tpl')
