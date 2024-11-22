import streamlit as st
from streamlit_extras import row
import hydralit_components as hc
from streamlit_extras.let_it_rain import rain 

st.set_page_config(layout="wide")
css = """
<style>
 .ezrtsby0 {
    display : none!important;
}
</style>

"""

st.markdown(css, unsafe_allow_html=True)

def main():
    rain(
        emoji="♥"
    )

main()

img = r"C:\Users\dyyk\Desktop\NMM\a.jpg"
img2 = r"C:\Users\dyyk\Desktop\NMM\c.jpg"
img3 = r"C:\Users\dyyk\Desktop\NMM\abc.jpg"
img4 = r"C:\Users\dyyk\Desktop\NMM\def.jpg"
img5 = r"C:\Users\dyyk\Desktop\NMM\hij.jpg"
cols = st.columns([1,3,1])
    
with cols[1]:
    st.header("Our Anniversary")
    with st.container(border=True):
        st.image(img, caption="Our Anniversary")

with st.container(border=True):
    cols = st.columns([1,1,1])
    with cols[0]:
        st.image(img2)
    with cols[1]:
        st.image(img3)
    with cols[2]:
        st.image(img4)
    

with st.container(border=True):
    cols = st.columns([1,1,1])
    with cols[0]:
        st.image(img2)
    with cols[1]:
        st.image(img3)
    with cols[2]:
        st.image(img4)


