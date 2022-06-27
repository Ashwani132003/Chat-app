from email import message
import streamlit as st

import socket
from textblob import TextBlob

def server():
    s=socket.socket()
    host = socket.gethostname()
    st.write('Server will srart at host: ',host)
    port = 8080
    s.bind((host,port))
    st.write('Waiting for connection \n')
    s.listen(1)
    conn,addr=s.accept()

    while 1:
        message = st.text_input(str('You >>'))
        message = message.encode()
        conn.send(message)
        st.success('Sent')
        incoming_message = conn.recv(1024)
        incoming_message = incoming_message.decode()
        blob = TextBlob(incoming_message)
        incoming_message = blob.translate(to='es')
        st.write('Friend >>', incoming_message)
        

