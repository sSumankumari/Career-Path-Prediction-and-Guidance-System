import streamlit as st
import numpy as np
from helper import provide_guidance, predict_career_path

# Set the page configuration, including title and layout
st.set_page_config(
    page_title="Career Path Prediction and Guidance System",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Inject custom CSS for better styling
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    .sidebar .sidebar-content h4 {
        color: #007bff;
    }
    .main .block-container {
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #007bff;
        color: #ffffff;
        font-size: 16px;
        font-weight: bold;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar with detailed instructions
st.sidebar.header("App Instructions")
st.sidebar.write("""
#### Follow the steps below to use this Career Path Prediction and Guidance System:

1. **Enter Your Ratings and Scores:**
   - Provide your ratings for coding skills, self-learning capability, reading and writing skills, and memory capability.
   - For "Reading and Writing Skills" and "Memory Capability Score," use the following scale:
     - **Poor**: 0
     - **Medium**: 1
     - **Excellent**: 2

2. **Select Your Certifications:**
   - Choose all relevant certifications you have completed from the list provided.

3. **Select the Workshops Attended:**
   - Pick the workshops you have participated in that align with your career interests.

4. **Choose Your Interested Subjects:**
   - Select the subjects that you are most passionate about and have a strong understanding of.

5. **Select Your Preferred Career Area:**
   - Indicate the career areas that align with your long-term professional goals.

6. **Choose the Preferred Type of Company:**
   - Select the type of company you would like to work for from the dropdown menu.

7. **Click the 'Predict Career Path' Button:**
   - The system will predict your most suitable career path based on your inputs.

8. **Review Your Predicted Career Path:**
   - Receive a detailed guidance message tailored to your predicted career path, offering insights and next steps to help you achieve your professional goals.
""")

# Collecting user inputs
st.title("🎯 Career Path Prediction and Guidance System")

st.markdown("#### Rate Your Skills and Capabilities")
coding_skills_rating = st.slider("Coding Skills Rating", 1, 10, 5)
self_learning_capability = st.radio("Self-Learning Capability", [0, 1], index=1,
                                    help="Select your self-learning capability.")
reading_and_writing_skills = st.selectbox("Reading and Writing Skills", [0, 1, 2],
                                          help="Rate your reading and writing skills.")
memory_capability_score = st.selectbox("Memory Capability Score", [0, 1, 2], help="Rate your memory capability.")

st.markdown("#### Select Your Certifications")
certifications = st.multiselect("Certifications",
                                ['App Development', 'Distro Making', 'Full Stack', 'Hadoop',
                                 'Information Security', 'Machine Learning', 'Python',
                                 'R Programming', 'Shell Programming'])

st.markdown("#### Select the Workshops Attended")
workshops = st.multiselect("Workshops Attended",
                           ['Cloud Computing', 'Data Science', 'Database Security',
                            'Game Development', 'Hacking', 'System Designing',
                            'Testing', 'Web Technologies'])

st.markdown("#### Choose Your Interested Subjects")
interested_subjects = st.multiselect("Interested Subjects",
                                     ['Computer Architecture', 'IOT', 'Management',
                                      'Software Engineering', 'Cloud Computing',
                                      'Data Engineering', 'Hacking', 'Networks',
                                      'Parallel Computing', 'Programming'])

st.markdown("#### Select Your Preferred Career Area")
interested_career_area = st.multiselect("Interested Career Area",
                                        ['Business Process Analyst', 'Cloud Computing',
                                         'Developer', 'Security', 'System Developer',
                                         'Testing'])

st.markdown("#### Choose the Preferred Type of Company")
type_of_company = st.selectbox("Preferred Type of Company",
                               ['BPA', 'Cloud Services', 'Finance', 'Product Based',
                                'SAaS Services', 'Sales and Marketing', 'Service Based',
                                'Testing and Maintenance Services', 'Web Services',
                                'Product Development'])

# One-hot encode the multiselect and selectbox inputs
certifications_vector = [1 if cert in certifications else 0 for cert in
                         ['App Development', 'Distro Making', 'Full Stack', 'Hadoop', 'Information Security',
                          'Machine Learning', 'Python', 'R Programming', 'Shell Programming']]
workshops_vector = [1 if workshop in workshops else 0 for workshop in
                    ['Cloud Computing', 'Data Science', 'Database Security', 'Game Development', 'Hacking',
                     'System Designing', 'Testing', 'Web Technologies']]
subjects_vector = [1 if subject in interested_subjects else 0 for subject in
                   ['Computer Architecture', 'IOT', 'Management', 'Software Engineering', 'Cloud Computing',
                    'Data Engineering', 'Hacking', 'Networks', 'Parallel Computing', 'Programming']]
career_area_vector = [1 if area in interested_career_area else 0 for area in
                      ['Business Process Analyst', 'Cloud Computing', 'Developer', 'Security', 'System Developer',
                       'Testing']]
company_vector = [1 if company == type_of_company else 0 for company in
                  ['BPA', 'Cloud Services', 'Finance', 'Product Based', 'SAaS Services', 'Sales and Marketing',
                   'Service Based', 'Testing and Maintenance Services', 'Web Services', 'Product Development']]

# Combine all features into a single array
input_data = np.array([coding_skills_rating, self_learning_capability,
                       reading_and_writing_skills, memory_capability_score] +
                      certifications_vector + workshops_vector + subjects_vector +
                      career_area_vector + company_vector).reshape(1, -1)

# Predict the career path
if st.button("🔍 Predict Career Path"):
    prediction = predict_career_path(input_data)
    st.success(f"**Predicted Career Path:** {prediction}")
    st.info(f"**Guidance:** {provide_guidance(prediction)}")
