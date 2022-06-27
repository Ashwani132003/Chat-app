import streamlit as st

import socket
from textblob import TextBlob



def client():
    host = st.text_input(str('Enter the host name: '))
    
    s=socket.socket()
    st.write('Server will srart at host: ',host)
    port = 8080
    s.connect((host,port))
    st.write('Connected to chat server \n')

    while 1:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        blob = TextBlob(incoming_message)
        try:
            incoming_message=blob.translate(from_lang = 'en', to = 'en')
        except:
            pass
        #  = blob.translate(from_lan='en', to='en')
        st.write('Friend >>', incoming_message)
        message = st.text_input(str('You >>'))
        message = message.encode()
        if s.send(message):
            st.success("Sent")
    
