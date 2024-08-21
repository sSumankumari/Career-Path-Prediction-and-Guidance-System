import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
import os

# Load the model
model_dir = 'model'
model_path = os.path.join(model_dir, 'ann_model.h5')
loaded_model = load_model(model_path)

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

# Define functions for detailed guidance based on the predicted job role
def provide_guidance(job_role):
    guidance_messages = {
        'Applications Developer': "As an Applications Developer, focus on mastering programming languages and development frameworks. Stay updated with the latest software trends and consider contributing to open-source projects to build a strong portfolio.",
        'CRM Technical Developer': "Specialize in CRM platforms like Salesforce or Microsoft Dynamics. Develop strong customization and integration skills, and gain experience in data management and customer relationship strategies.",
        'Database Developer': "Hone your skills in SQL, database design, and data modeling. Understanding database optimization and experience with big data technologies will be crucial in this role.",
        'Mobile Applications Developer': "Focus on mobile-specific programming languages like Swift and Kotlin. Keep up with the latest mobile development trends and ensure your apps are optimized for performance and user experience.",
        'Network Security Engineer': "Develop deep knowledge in network security protocols, firewalls, and encryption. Obtain relevant certifications such as CISSP or CEH to strengthen your credentials.",
        'Software Developer': "Master key programming languages and software development methodologies. Stay engaged with the developer community to keep your skills current and relevant.",
        'Software Engineer': "Develop a strong understanding of software architecture and engineering principles. Work on projects that challenge your problem-solving abilities and involve large-scale systems.",
        'Software Quality Assurance (QA) / Testing': "Focus on learning automation testing tools and techniques. Experience with both manual and automated testing will enhance your ability to ensure software reliability.",
        'Systems Security Administrator': "Build expertise in system security, including managing firewalls, intrusion detection systems, and anti-virus software. Stay current with security threats and mitigation strategies.",
        'Technical Support': "Develop excellent problem-solving and communication skills. Familiarize yourself with a wide range of software and hardware products to provide effective support.",
        'UX Designer': "Invest in understanding user experience principles, including user research, prototyping, and usability testing. Focus on creating intuitive and accessible designs.",
        'Web Developer': "Stay updated with web technologies and frameworks such as React, Angular, and Node.js. A strong grasp of front-end and back-end development will make you versatile in this field."
    }
    return guidance_messages.get(job_role,
                                 "Explore the specific skills and certifications that align with the job role to advance your career path.")


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
self_learning_capability = st.radio("Self-Learning Capability", [0, 1], index=1, help="Select your self-learning capability.")
reading_and_writing_skills = st.selectbox("Reading and Writing Skills", [0, 1, 2], help="Rate your reading and writing skills.")
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

# Combine all inputs into a single feature vector
user_input = np.array([[coding_skills_rating, self_learning_capability, reading_and_writing_skills,
                        memory_capability_score] + certifications_vector + workshops_vector +
                       subjects_vector + career_area_vector + company_vector])

# Predict the career path
if st.button("🔍 Predict Career Path"):
    prediction = loaded_model.predict(user_input)
    predicted_index = np.argmax(prediction)
    job_roles = ['Applications Developer', 'CRM Technical Developer', 'Database Developer',
                 'Mobile Applications Developer', 'Network Security Engineer', 'Software Developer',
                 'Software Engineer', 'Software Quality Assurance (QA) / Testing',
                 'Systems Security Administrator', 'Technical Support', 'UX Designer', 'Web Developer']
    predicted_job_role = job_roles[predicted_index]
    st.success(f"**Predicted Career Path:** {predicted_job_role}")
    st.info(f"**Guidance:** {provide_guidance(predicted_job_role)}")
