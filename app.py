import streamlit as st
st.title("Largest of three Numbers:")

a=st.number_input("Enter First Number:")
b=st.number_input("Enter Second Number:")
c=st.number_input("Enter Third Number:")

if (a>b) and (a>c):
  st.write(a:+"First Number is Largest")
elif (b>a) and (b>c):
  st.write(b:+"Second Number is Largest")
else:
  st.write(c:+"Third Number is Largest")
