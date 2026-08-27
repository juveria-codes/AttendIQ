import streamlit as st

def style_background_home():
    st.markdown("""
            <style>
             .stApp{
             background : #5865F2 !important;
             }
            </style>
                """

            ,unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown("""
            <style>
             .stApp{
             background : #E0E3FF !important;
             }
            </style>
                """

            ,unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
            /*hide top bar default on streamlit*/

            #MainMenu, footer, header{
                visibility:hidden;   
                }
        </style>        """

            ,unsafe_allow_html=True)