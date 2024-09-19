import streamlit as st

from Auth.auth import auth
from Auth.logout import logout
from icon.icon import icon


def show_requirements():
    requirements = """
    streamlit
    selenium
    webdriver-manager
    pandas
    openpyxl
    matplotlib
    aiohttp
    asyncio
    python-dotenv
    """
    st.title("Project Requirements")
    st.markdown("Below are the required packages for this project:")
    st.text_area("requirements.txt", requirements, height=400)

def main():
    icon()
    auth()
    logout()
    show_requirements()
    
if __name__ == "__main__":
    main()
