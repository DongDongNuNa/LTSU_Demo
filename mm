"""
user_text = st.text_input("Input some text here")
st.write(user_text)

default_text = st.text_area("Input some text here", "default text")
st.write(user_text)

user_number = st.number_input("Input Number",
                               min_value = 1, 
                               max_value = 10,
                               value = 5,
                               step = 1)
st.write(user_number)

slider_number = st.slider("Select your Number",
                            min_value = 1,
                            max_value = 10,
                            value = 5,
                            step = 1)
                  
st.write(slider_number)

user_date = st.date_input("Select your date",
                            value = datetime.date(2000, 6, 12),
                            min_value = datetime.date(2000, 1, 12),     #what does 2000 means?
                            max_value = datetime.date(2001, 1, 12)      #why 2001?
                            )

st.write(user_date)

user_time = st.time_input("Select your time",
                            value = datetime.time(6, 12)
                            )
st.write(user_time)

checked = st.checkbox("Select this checkbox")
st.write(f"Current state of checkbox: {checked}")

state = st.button("click to change current state")
st.write(f"button has been PRESSED: {state}")

options = ["Red", "Blue", "Yellow"]
radio_selection = st.radio("Select Color", options)
st.write(f"Color selected is {radio_selection}")


options = ["Red", "Blue", "Yellow"]
selectbox_selection = st.selectbox("Select Color", options)
st.write(f"Color selected is {selectbox_selection}")

options = ["Red", "Blue", "Yellow"]
multiselect_selection = st.multiselect("Select Color", options)
st.write(f"Color selected is {multiselect_selection}")


if "prev_word_count" not in st.session_state:
    st.session_state['prev_word_count'] = 5

text = st.text_area('Paste text here to get word count.', 'This is some default text.')
word_count = len(text.split())
change = word_count - st.session_state.prev_word_count
st.metric('word Count', word_count, change)
st.session_state.prev_word_count = word_count

"""
