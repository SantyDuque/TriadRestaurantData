import streamlit as st

def page2():
    st.title("Proximamente")
    st.write("Aca estara el analisis de proximas bases de datos")

st.logo("Images/Logo2.PNG", icon_image="Images/Logo1.png")

pg = st.navigation([
    st.Page("ResRev.py", title="Restaurant Revenue", icon="🍽"),
    st.Page(page2, title="Proximamente", icon=None)
])

pg.run()