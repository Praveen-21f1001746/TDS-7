import streamlit as st
st.title("Largest of three Numbers:")

a=st.number_input("Enter First Number:")
b=st.number_input("Enter Second Number:")
c=st.number_input("Enter Third Number:")

if (a>b) and (a>c):
  st.write(a,"which is first number is the largest")
elif (b>a) and (b>c):
  st.write(b,"which is second number is largest")
else:
  st.write(c,"which is third number is largest")
