import streamlit as st


def show_requirements():
    
    requirements = """
    streamlits
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
    st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    show_requirements()
    
if __name__ == "__main__":
    main()
