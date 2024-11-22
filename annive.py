import streamlit as st
from streamlit_extras import row

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

img = r"a.jpg"
img2 = r"c.jpg"
img3 = r"abc.jpg"
img4 = r"def.jpg"
img5 = r"hij.jpg"
img6 = r"cha.jpg"
img7 = r"dir1.jpg"
cols = st.columns([1,3,1])
    
with cols[1]:
    st.header("Our Mermories")
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
        st.image(img5)
    with cols[1]:
        st.image(img6)
    with cols[2]:
        st.image(img7)


