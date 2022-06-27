import streamlit as st

import socket
from textblob import TextBlob

def client():
    s=socket.socket()
    host = st.text_input(str('Enter the host name: '))
    st.write('Server will srart at host: ',host)
    port = 8080
    s.connect((host,port))
    st.write('Connected to chat server \n')
    # s.listen(1)
    # conn,addr=s.accept()

    while 1:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        blob = TextBlob(incoming_message)
        incoming_message = blob.translate(to='es')
        st.write('Friend >>', incoming_message)
        message = st.text_input(str('You >>'))
        message = message.encode()
        s.send(message)
        st.success("Sent")
    