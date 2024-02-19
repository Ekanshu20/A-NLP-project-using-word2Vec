import streamlit as st
import helper
import pickle

model = pickle.load(open('model.pkl','rb'))

st.header("Duplicate Question Pairs")

q1 = st.text_input("Enter first question")
q2 = st.text_input("Enter second question")

if st.button("Find"):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]
    
    if result:
        st.header("Duplicate")
    else:
        st.header("Not Duplicate")    