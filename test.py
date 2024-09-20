import streamlit as st


def show_requirements():
    st.markdown("""
    <style>
    .viewerBadge_container__r5tak {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)
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
  
    show_requirements()
    
if __name__ == "__main__":
    main()
