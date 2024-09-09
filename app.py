import streamlit as st
st.title('Sourov Talukder')
col1, col2 = st.columns(2)
with col1:
    st.image('sourov.jpg')
    st.markdown("""
`Tools` : SQL, Python, Power BI                         
**project link** :https://en.wikipedia.org/wiki/Main_Page
""")
with col2:
    st.write("""Hi i am Sourov 
             \nI am a Data Scientist 
             \nBelow i Created a lot of project""")
    
st.header('Projects')
st.subheader('Data Science')
st.subheader('Data Analysis')
st.subheader('Data Engineering')    
st.subheader('DSA')

st.subheader('SQL')
st.subheader('Python Programming Language')

st.sidebar.title('Projects')
st.sidebar.markdown("""
- Home
- About
- Contact
- Carrer Section
- Login Section
""")

st.sidebar.selectbox('Projects', options=['Python', 'SQL', 'Power BI'])
st.sidebar.button('select')
st.title('Hello teacher')