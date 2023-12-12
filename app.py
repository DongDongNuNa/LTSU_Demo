import streamlit as st
import datetime
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


@st.cache_data()
def load_df():
    df = pd.read_csv("./data/titanic.csv")

    survival_options = df.Survived.unique()

    p_class_options = df.Pclass.unique()

    sex_options = df.Sex.unique()

    embark_options = df.Embarked.unique()

    min_fare = df.Fare.min()
    max_fare = df.Fare.max()

    min_age = df.Age.min()
    max_age = df.Age.max()

    return df, survival_options, p_class_options, sex_options, embark_options, min_fare, max_fare, min_age, max_age


def check_rows(column, options):
    return res.loc[res[column].isin(options)]

st.title("Demo dataframe query app")

df, survival_options, p_class_options, sex_options, embark_options, min_fare, max_fare, min_age, max_age = load_df()
res = df

name_query = st.text_input("String match for name")

cols = st.columns(4)

survival = cols[0].multiselect("Survived", survival_options)
p_class = cols[1].multiselect("Passenger Class", p_class_options)
sex = cols[2].multiselect("Sex", sex_options)
embark = cols[3].multiselect("Embarked", embark_options)

range_cols = st.columns(3)
min_fare_range, max_fare_range = range_cols[0].slider("Lowest Fare", float(min_fare), float(max_fare),
                                                [float(min_fare), float(max_fare)])
min_age_range, max_age_range = range_cols[2].slider("Lowest Age", float(min_age), float(max_age),
                                                [float(min_age), float(max_age)])


if name_query != "":
    res = res.loc[res.Name.str.contains(name_query)]

if survival:
    res = check_rows("Survived", survival)

if p_class:
    res = check_rows("Pclass", p_class)

if sex:
    res = check_rows("Sex", sex)

if embarked:
    res = check_rows("Embarked", embarked)


if range_cols[0].checkbox("Use Fare Range"):
    res = res.loc[(res.Fare > min_fare_range) & (res.Fare < max_fare_range)]



if range_cols[2].checkbox("Use Age Range"):
    res = res.loc[(res.Age > min_age_range) & (res.Age < max_age_range)]

removal_columns = st.multiselect("Select volumns to remove", df.columns.tolist())

for column in removal_columns:
    res = res.drop(column, axis = 1)

st.write(res)