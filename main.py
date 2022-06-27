import streamlit as st

import server
import client

if st.button('Server'):
    server.server()
if st.button('Client'):
    client.client()    