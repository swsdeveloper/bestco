import streamlit as st
import pandas
import itertools

st.set_page_config(layout='wide')


def display_team_member(team_member_info) -> None:
    """
    Display info for a team member of this company.
    Info is a dictionary with keys: name, position, and image

    :param team_member_info: name, position, image
    :return: None
    """
    return


lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa
qui officia deserunt mollit anim id est laborum.
"""

st.title("The Best Company")

st.write(lorem_ipsum)

st.header("Our Team")
