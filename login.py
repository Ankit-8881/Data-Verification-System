import streamlit as st

# Set page config for better appearance
st.set_page_config(
    page_title="Login Page",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: black;
    }
    .login-box, .register-box {
        background-color: #1e1e1e;
        color: white;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.4);
        width: 460px;
        margin: auto;
        text-align: center;
    }
    .login-box input, .register-box input {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #555;
        border-radius: 5px;
        background: #2b2b2b;
        color: white;
    }
    .login-box button, .register-box button {
        width: 100%;
        padding: 10px;
        background-color: #007bff;
        border: none;
        border-radius: 5px;
        color: white;
        margin-top:10px;
        font-size: 16px;
        cursor: pointer;
    }
    .login-box button:hover, .register-box button:hover {
        background-color: #0056b3;
        
        
        label { 
        display:inline-block;
        width: 100%;
    text-align: justify;
    }



    }
    .login-box a, .register-box a {
        color: #007bff;
        text-decoration: none;
    }
    .login-box a:hover, .register-box a:hover {
        text-decoration: underline;
    }
    .footer-link {
        display: inline-block;
        margin-top: 15px;
        font-size: 14px;
    }
    .stButton {
    margin-top: 15px ;
    text-align: center;
}
    </style>
    """,
    unsafe_allow_html=True,
)

# Helper function to show the login form
def show_login_form():
    st.markdown(
        """
        <div class="login-box">
            <h2>Login</h2>
            <form>
                <label for="username">Username:</label><br>
                <input type="text" id="username" name="username" placeholder="Enter your username"><br>
                <label for="password">Password:</label><br>
                <input type="password" id="password" name="password" placeholder="Enter your password"><br>
                <button type="submit">Login</button><br>
            </form>
          
        </div>
        """
    , unsafe_allow_html=True)

# Helper function to show the register form
def show_register_form():
    st.markdown(
        """
        <div class="register-box">
            <h2>Register</h2>
            <form>
                <label for="new-username">Username:</label><br>
                <input type="text" id="new-username" name="new-username" placeholder="Enter a username"><br>
                <label for="new-password">Password:</label><br>
                <input type="password" id="new-password" name="new-password" placeholder="Enter a password"><br>
                <label for="confirm-password">Confirm Password:</label><br>
                <input type="password" id="confirm-password" name="confirm-password" placeholder="Confirm your password"><br>
                <button type="submit">Register</button><br>
            </form>
           
        </div>
        """
    , unsafe_allow_html=True)

# Initialize session state to manage views
if "view" not in st.session_state:
    st.session_state.view = "login"

# Display the form based on the current view in session state
if st.session_state.view == "login":
    show_login_form()
    # When the "Register" link is clicked, change the view to "register"
    if st.button("Go to Register"):
        st.session_state.view = "register"
else:
    show_register_form()
    # When the "Login" link is clicked, change the view to "login"
    if st.button("Go to Login"):
        st.session_state.view = "login"
