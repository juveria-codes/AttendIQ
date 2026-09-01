import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard


def teacher_screen():


    style_background_dashboard()
    style_base_layout()


    if "teacher_login_type" not in st.session_state:
         st.session_state.teacher_login_type = "login"

    if st.session_state.teacher_login_type == "login":
        teacher_screen_login()

    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()
    

def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go Back To Home", type="secondary", key = "loginbackbtn1", shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()
    
    st.header('Login using password', text_alignment='center')
    st.space()
    st.space()
    teacher_username = st.text_input('Enter Username', placeholder='your name')
    teacher_password = st.text_input('Enter Password', placeholder='your password',type='password')
    st.divider()

    btnc1, btnc2= st.columns(2)

    with btnc1:
        st.button("Login",icon=':material/passkey:', shortcut='control+enter', width='stretch')
    with btnc2:
        if st.button("Register Instead",icon=':material/passkey:', width='stretch', type='primary'):
            st.session_state.teacher_login_type = "register"
            st.rerun()
        

def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
        
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go Back To Home", type="secondary", key = "loginbackbtn2", shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()
        
        
    st.header('Register your teacher profile', text_alignment='center')

    st.space()
    teacher_username = st.text_input('Enter Username', placeholder='your username')
    teacher_name = st.text_input('Enter your name', placeholder='your name')
    teacher_pass = st.text_input('Enter Password', placeholder='your password',type='password')
    teacher_pass_confirm = st.text_input('Confirm your Password', placeholder='your password',type='password')
    st.divider()
    
    btnc1, btnc2= st.columns(2)
    
    with btnc1:
        st.button("Regiter now",icon=':material/passkey:', shortcut='control+enter', width='stretch')
    with btnc2:
        if st.button("Login Instead",icon=':material/passkey:', width='stretch', type='primary'):
            st.session_state.teacher_login_type='login'
            