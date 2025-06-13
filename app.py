#importing the libraries we need
import streamlit as st
import pickle

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Page setup
st.set_page_config(page_title="𝓟𝓪𝔂 𝓜𝓮 𝓟𝓻𝓮𝓽𝓽𝔂", page_icon="🎀")

# Title of the predictor app
st.title("🎀 𝓟𝓪𝔂 𝓜𝓮 𝓟𝓻𝓮𝓽𝓽𝔂 – Predict Your Pay Like a Diva")
st.caption("Smart salary predictions for every hustle.")

# Input age of the user
age = st.number_input("Age", min_value=18, max_value=70, value=25)
#choose gender of the user
gender = st.selectbox("Gender", ["Male", "Female"])
#select education level
education = st.selectbox("Education Level", ["High School", "Bachelor", "Master", "PhD"])
#select their job tittle
import streamlit as st

# Select box for tech jobs
job = st.selectbox(
    "Job Title",
    options=[
        "Software Engineer",
        "Data Scientist",
        "UI/UX Designer",
        "DevOps Engineer",
        "Cybersecurity Analyst"
    ],
    index=None,
    placeholder="Select a job title"
)

#slider for job experience of the user
experience = st.slider("Years of Experience", 0, 40, 1)

# Add spacing
st.markdown("")

# Predict button
if st.button("Predict Salary"):
    gender_val = 1 if gender == "Male" else 0
    edu_map = {"High School": 0, "Bachelor": 1, "Master": 2, "PhD": 3}
    education_val = edu_map[education]
    job_length = len(job)

    features = [[age, gender_val, education_val, job_length, experience]]
    prediction = model.predict(features)

#share the results to the user
    st.success(f"Estimated Salary: kes{prediction[0]:,.2f}")
    st.balloons()