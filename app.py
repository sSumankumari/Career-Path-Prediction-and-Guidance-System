import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
import os

# Define the model directory and load the model
model_dir = 'model'
model_path = os.path.join(model_dir, 'ann_model.h5')
loaded_model = load_model(model_path)

# Function to predict the job role based on input features
def predict_job_role(features):
    prediction = loaded_model.predict(np.array([features]))
    predicted_index = np.argmax(prediction, axis=1)[0]
    return job_roles[predicted_index]

# Define the list of job roles
job_roles = [
    'Applications Developer', 'CRM Technical Developer', 'Database Developer',
    'Mobile Applications Developer', 'Network Security Engineer',
    'Software Developer', 'Software Engineer',
    'Software Quality Assurance (QA) / Testing', 'Systems Security Administrator',
    'Technical Support', 'UX Designer', 'Web Developer'
]

# Sidebar for instructions
st.sidebar.header("Instructions for Inputs")
st.sidebar.write("""
- **Coding Skills Rating**: Enter a number between 1 and 10.
- **Self-Learning Capability**: Choose between Yes (1) or No (0).
- **Reading and Writing Skills**: Choose a value between 0 and 2.
- **Memory Capability Score**: Choose a value between 0 and 2.
- For certifications, workshops, interested subjects, and career areas, select multiple options based on your experience and preferences.
""")

# Main page title
st.title('Career Path Prediction and Guidance System')

# Input fields
st.subheader('Input Features')

coding_skills_rating = st.slider('Coding Skills Rating (1-10)', 1, 10, 5)
self_learning_capability = st.selectbox('Self-Learning Capability', [1, 0])
reading_and_writing_skills = st.selectbox('Reading and Writing Skills', [0, 1, 2])
memory_capability_score = st.selectbox('Memory Capability Score', [0, 1, 2])

# Certifications (Multiselect)
st.subheader('Certifications')
certifications_options = [
    'App Development', 'Distro Making', 'Full Stack', 'Hadoop',
    'Information Security', 'Machine Learning', 'Python', 'R Programming',
    'Shell Programming'
]
selected_certifications = st.multiselect('Select your Certifications', certifications_options)

# Workshops (Multiselect)
st.subheader('Workshops')
workshops_options = [
    'Cloud Computing', 'Data Science', 'Database Security', 'Game Development',
    'Hacking', 'System Designing', 'Testing', 'Web Technologies'
]
selected_workshops = st.multiselect('Select your Workshops', workshops_options)

# Interested Subjects (Multiselect)
st.subheader('Interested Subjects')
subjects_options = [
    'Computer Architecture', 'Internet of Things (IoT)', 'Management',
    'Software Engineering', 'Cloud Computing', 'Data Engineering', 'Hacking',
    'Networks', 'Parallel Computing', 'Programming'
]
selected_subjects = st.multiselect('Select your Interested Subjects', subjects_options)

# Interested Career Area (Multiselect)
st.subheader('Interested Career Area')
career_area_options = [
    'Business Process Analyst', 'Cloud Computing', 'Developer', 'Security',
    'System Developer', 'Testing'
]
selected_career_areas = st.multiselect('Select your Interested Career Areas', career_area_options)

# Preferred Type of Company (Selectbox)
st.subheader('Preferred Type of Company')
company_options = [
    'Business Process Analyst (BPA)', 'Cloud Services', 'Finance', 'Product Based',
    'SaaS Services', 'Sales and Marketing', 'Service Based',
    'Testing and Maintenance Services', 'Web Services', 'Product Development'
]
selected_company_type = st.selectbox('Select your Preferred Type of Company', company_options)

# Map selected options to binary feature values (1 for selected, 0 for not selected)
def get_binary_features(selected_options, options_list):
    return [1 if option in selected_options else 0 for option in options_list]

certifications_features = get_binary_features(selected_certifications, certifications_options)
workshops_features = get_binary_features(selected_workshops, workshops_options)
subjects_features = get_binary_features(selected_subjects, subjects_options)
career_area_features = get_binary_features(selected_career_areas, career_area_options)

# Map the selected company type to binary feature values (1 for selected, 0 for others)
company_features = get_binary_features([selected_company_type], company_options)

# Combine all features into a single feature vector
input_features = [
    coding_skills_rating, self_learning_capability, reading_and_writing_skills,
    memory_capability_score
] + certifications_features + workshops_features + subjects_features + career_area_features + company_features

# Prediction button
if st.button('Predict Career Path'):
    prediction = predict_job_role(input_features)
    st.write(f"The recommended career path is: **{prediction}**")
