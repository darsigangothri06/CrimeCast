import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
import crime_application

cred = credentials.Certificate('crimecast-7ce63-426d5fa6f83a.json')

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

def check_auth():
    try:
        user = auth.get_user_by_email(st.session_state["email"])
        st.session_state.username = user.uid
        st.session_state.useremail = user.email
        st.session_state['authenticated'] = True
    except Exception as e:
        print(e)
        st.session_state['authenticated'] = False
        st.warning('Incorrect email or password! Please try again')
    
    st.session_state["email"] = ""
    st.session_state["password"] = ""

def display_login_signup_ui():
    with st.sidebar:
        st.title('Welcome to CrimeCast')
        choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])
        email = st.text_input('Email Address', key='email')
        password = st.text_input('Password', type='password', key='password')

        if choice == 'Sign Up':
            username = st.text_input("Enter your unique username")
            if st.button('Create my account'):
                user = auth.create_user(email=email, password=password, uid=username)
                st.success('Account created successfully!')
                st.markdown('Please Login using your email and password')
                st.balloons()
        else:
            col1, col2 = st.columns(2)
            with col1:
                st.button('Login', on_click = check_auth)
                    
            with col2:
                if st.button("Sign Out"):
                    if not st.session_state.get('authenticated', False):
                        st.warning('Please login!')
                    else:
                        st.success('User signed out successfully')
                        st.session_state['authenticated'] = False  # Set authenticated to False on signout

def main_app():
    # Your main application logic goes here
    crime_application.main()

def app():
    if "signedout" not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False

    display_login_signup_ui()

  # Only call main_app if user is authenticated
    if st.session_state.get('authenticated', False):
        main_app()

# Only call the app function if not signed out
if not st.session_state.get("signedout",False):
    app()
