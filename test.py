import streamlit as st

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

# CSS injection to hide elements and change the background color
hide_streamlit_style = """
<style>
[data-testid="stToolbarActions"] {
    display: none;  /* Hides the toolbar actions */
}

.viewerBadge_container__r5tak {visibility: hidden;}
</style>
<script>
const link = document.querySelector('.viewerBadge_link__qRIco');
    // Add an id attribute
    link.setAttribute('id', 'myDynamicId');
</script>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def main():
    show_requirements()

if __name__ == "__main__":
    main()
