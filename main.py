import streamlit as st
import pandas as pd
import itertools

st.set_page_config(layout='wide')


def display_team_member(team_member_info) -> None:
    """
    Display info for a team member of this company.
    Info is a dictionary with string keys: 'first name', 'last name', 'role', and 'image'.
    All values are also strings.
    Distribute team member info across 3 columns.

    :param team_member_info: first name, last name, role, image file name
    :return: None
    """
    first_name = team_member_info['first name'].title()  # ex: 'mary ann' -> 'Mary Ann'
    last_name = team_member_info['last name'].title()
    full_name = first_name + ' ' + last_name
    role = team_member_info['role']
    image_path = 'images/' + team_member_info['image']
    placeholder_path = 'images/placeholder.png'

    with next(col_iterator):
        st.subheader(full_name)
        st.write(role)
        try:
            st.image(image_path)
        except:
            st.image(placeholder_path, use_column_width=True)  # display placeholder image

    return


lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa
qui officia deserunt mollit anim id est laborum.
"""

st.header("The Best Company")

st.write(lorem_ipsum)

st.subheader("Our Team")

col1, empty1, col2, empty2, col3 = st.columns(5)  # the 2nd and 4th columns will be empty

cols = [col1, col2, col3]
col_iterator = itertools.cycle(cols)

# Read CSV file
csvfile = 'data.csv'
data = pd.read_csv(csvfile, sep=',')  # data is a Pandas DataFrame object
for index, record in data.iterrows():
    try:
        display_team_member(record)
    except ValueError:
        st.write(f"*** Error processing csv record (index=:{index}) - bypassing bad data ***")
