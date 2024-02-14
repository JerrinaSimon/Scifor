#1.What is Streamlit, and how does it differ from other web frameworks?
#Streamlit is basically is a python libary used to create a web based application,with the use of simple and minimum functions.When comparing with other framework it will reduce the complexity of creating the web based application model.

#2.Explain the basic structure of a Streamlit app.
#basic structure of streamlit involves
#a) import the streamlit library.
import streamlit as st
#b) display title,header or subheader as st.title(),st.header(),st.subheader() etc
#c)provide user input like text input,sidebar etc.
#d)performing the computation
#e)result can be displayed using st.write() function.
#f)Run the app using streamlit.run

#3.How can you add a title to your Streamlit app?
#Title can be add using the st.title(),It will display the text in title format.
#syntax:st.title(body,anchor=None,*,help=None)
#eg :
import streamlit as st
st.title("Title of the app")
#it will display the output as:Title of the app.

#4.What is the purpose of the st.write() function in Streamlit?
#st.write():it will write the arguments in the streamlit app.it can be of data which includes text,dataframes,charts etc.
#syntax:st.write(*args,unsafe_allow_html=False,**kwargs)
#eg:
import streamlit as st
st.write("display the message")
#output:display the message.

import streamlit as st
import pandas as pd
data=pd.dataframe({'A':[1,2,3],'B':[4,5,6]})
st.write(data)
#output will be in the form of static table

#5.How do you create interactive widgets in Streamlit? Provide examples.
#Interactive widget in streamlit can be created using st.button(), st.sidebar(),st.text_input(),st.checkbox etc function.
#eg:
#import streamlit as st
button=st.button("click")
#output:button displaying with click name.

#another example:
import streamlit as st
st.checkbox("click")
#output:displays a checkox labelled click

import streamlit as st
st.text_input("display a message")
#output:it will display in the text formatting as display a message