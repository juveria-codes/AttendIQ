import streamlit as st

from supabase import create_client, Client

supabase : Client =(
    st.secrets['SUPABASE_URL'],
    st.secrets['SUPABASE_KEY']
)