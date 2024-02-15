import streamlit as st
from streamlit.logger import get_logger
import streamlit_authenticator as stauth

LOGGER = get_logger(__name__)
st.set_page_config(
        page_title="RCD-CM Dashboard",
        page_icon="👋")

def run():


    st.write("# Welcome to RCD-CM Dashboard! 👋")

    st.sidebar.success("Select a page above.")
    
    st.markdown(
        """
        RCD-CM is short for Research Computing and Data (computing, data, and related infrastructure and services) Capabilities Model. 
        This Capabilities Model was developed by a collaboration of the Campus Research Computing Consortium ([CaRCC](https://carcc.org/)), 
        [Internet2](https://www.internet2.edu), and [EDUCAUSE](https://www.educause.edu/) with support from the National Science Foundation.

        For help or feedback, Please [email us](shuail@uark.edu).

        ### What is a Capabilities Model? 
        - [Capabilities Model](https://docs.google.com/document/d/15xiDXMta7AlEvE6IpW4mvadAiW2PPshmBi73AVHTm9g/view)

        ### Want to learn more?
        There are five key concepts that underlie the Model, around which the tool is organized. These are:
        - [The Five Facings](https://docs.google.com/document/d/15xiDXMta7AlEvE6IpW4mvadAiW2PPshmBi73AVHTm9g/view#bookmark=id.ob00r3jiplo)
        - [Deployment at Institution](https://docs.google.com/document/d/15xiDXMta7AlEvE6IpW4mvadAiW2PPshmBi73AVHTm9g/view#bookmark=id.ivn04nyto9md)
        - [Multi-Institutional Collaboration](https://docs.google.com/document/d/15xiDXMta7AlEvE6IpW4mvadAiW2PPshmBi73AVHTm9g/view#bookmark=id.mblad4sge5ul)
        - [Service Operating Levels](https://docs.google.com/document/d/15xiDXMta7AlEvE6IpW4mvadAiW2PPshmBi73AVHTm9g/view#bookmark=id.m1sn1k4wtrai)
        - [Support Levels](https://docs.google.com/document/d/15xiDXMta7AlEvE6IpW4mvadAiW2PPshmBi73AVHTm9g/view#bookmark=id.uf3g0hetwv8c)
        
        ### RCD-CM Survey
        - Our shortened version RCD-CM survy link [Qualtrics Survey](https://uark.qualtrics.com/jfe/form/SV_09aGmseG54YpUbk)
    """ )
    author_dtl = "<strong>Happy Playing: 😎 Shuai Liu: shuail@uark.com</strong>"    
    st.markdown(author_dtl, unsafe_allow_html=True)
    #st.write(" For help or feedback, Please[email us](shuail@uark.edu) ")
###############33


    def login():
        password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("Login") and password == "RCDCM":
            st.sidebar.success("Login successful!")
            return True
        return False


if __name__ == "__main__":
    run()
#streamlit run c:/Users/shuail/VScode/RCD-CM-app/Home.py
#python -m streamlit run c:/Users/shuail/VScode/RCD-CM-app/Home.py
# https://blog.streamlit.io/streamlit-authenticator-part-1-adding-an-authentication-component-to-your-app/
