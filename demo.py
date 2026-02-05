import streamlit as st

st.title("Button Example")
#st.snow()

if st.button("Click Me"):
    st.success("Button clicked!")

if st.checkbox("Show message"):
    st.write("Hello, Streamlit!")

choice = st.radio("Select gender", ["Male", "Female", "Other", "Kids"])
st.write("Selected:", choice)

city = st.selectbox("Choose city", ["Delhi", "Mumbai", "Bangalore"])
st.write("City:", city)

skills = st.multiselect(
    "Select your skills",
    ["Python", "JavaScript", "SQL", "ML"]
)
st.write("Skills:", skills)

age = st.slider("Select age", 1, 100, 5)
st.write("Age:", age)

name = st.text_input("Enter your name")
st.write("Name:", name)

feedback = st.text_area("Enter feedback")
st.write("Feedback:", feedback)

quantity = st.number_input("Enter quantity", min_value=1, max_value=100)
st.write("Quantity:", quantity)

date = st.date_input("Select date")
st.write("Date:", date)

time = st.time_input("Select time")
st.write("Time:", time)

time_12hr = time.strftime("%I:%M %S %p")  # %I → 12-hour, %p → AM/PM
st.write("Time (12-hour):", time_12hr)

file = st.file_uploader("Upload a file")
if file:
    st.write("File name:", file.name)

color = st.color_picker("Pick a color")
st.write("Selected color:", color)

import time
progress = st.progress(0)

for i in range(100):
    time.sleep(0.02)
    progress.progress(i + 1)

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "FaceBook", "Github")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

st.image("photo.jpg", caption="Sunrise by the mountains")

video_file = open("video.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)
