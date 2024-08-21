import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
import os
import random

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
        'Applications Developer': [
            "Applications Developers focus on creating and maintaining software applications that cater to specific needs. To excel in this role, you should have strong programming skills, familiarity with various development frameworks, and a solid understanding of software architecture. Keep up with the latest technologies and best practices in coding to ensure the applications you develop are efficient and scalable. Good problem-solving skills and the ability to work collaboratively with other developers and stakeholders are also crucial.",
            "As an Applications Developer, your role involves designing and developing applications to meet user requirements. It's essential to stay updated with new programming languages, tools, and technologies to enhance your development skills. Work on understanding user needs and ensure that the applications you build are user-friendly and functional. Testing and debugging are key parts of your job, so attention to detail and perseverance are important traits to develop.",
            "To thrive as an Applications Developer, focus on mastering a range of programming languages and development tools. You'll need to write code, test applications, and resolve any issues that arise during the development process. Staying current with industry trends and continuously learning new technologies will help you create innovative and efficient applications. Collaboration with other developers and stakeholders is also crucial for ensuring that the applications meet the desired specifications and user needs.",
            "As an Applications Developer, you should be adept at translating user requirements into functional software applications. Your role requires a deep understanding of various programming languages, frameworks, and development tools. Building and maintaining applications that are reliable and easy to use is key. Emphasize continuous learning and adaptation to new technologies and best practices. Additionally, strong problem-solving skills and effective communication with team members are vital for success in this field.",
            "In the role of an Applications Developer, you will be responsible for developing software applications tailored to user needs. A strong grasp of programming languages, software design principles, and development frameworks is essential. Regularly update your skills by exploring new technologies and techniques. Effective communication and teamwork with other developers and project stakeholders will help in delivering high-quality applications. Ensuring that your applications are both efficient and scalable will contribute to your success in this role."
        ],
        'CRM Technical Developer': [
            "As a CRM Technical Developer, your role involves customizing and optimizing CRM systems to meet business needs. You'll need strong skills in CRM platforms like Salesforce or Microsoft Dynamics, as well as proficiency in scripting and programming languages. Focus on understanding the specific requirements of the organization to tailor the CRM system accordingly. Regularly update your knowledge of CRM technologies and best practices to enhance system performance and user satisfaction.",
            "To excel as a CRM Technical Developer, you should have expertise in CRM systems and a good grasp of database management. Customizing CRM solutions to fit business processes and improve user experience is key. Work closely with stakeholders to understand their requirements and implement appropriate solutions. Continuous learning and keeping abreast of the latest CRM developments will help you deliver effective and innovative solutions that meet organizational needs.",
            "In the role of a CRM Technical Developer, you'll be tasked with configuring and maintaining CRM systems. Strong knowledge of CRM platforms, programming skills, and an understanding of business processes are essential. Ensure that the CRM system is tailored to the specific needs of the organization, and focus on improving user experience through customization and optimization. Staying updated with new CRM features and technologies will help you provide the best solutions for your clients.",
            "As a CRM Technical Developer, your job is to develop and customize CRM systems to meet the needs of the business. Proficiency in CRM platforms and programming languages is crucial. You'll need to work closely with users to understand their needs and implement effective solutions. Regularly review and update your skills to stay current with the latest CRM technologies and best practices. Your role is critical in enhancing the efficiency and effectiveness of CRM systems within the organization.",
            "To be successful as a CRM Technical Developer, focus on mastering CRM systems and related technologies. Your responsibilities include customizing CRM applications to align with business requirements and improving system functionality. Strong technical skills, along with the ability to communicate effectively with stakeholders, are essential. Keep your skills updated with ongoing learning and stay informed about new CRM features and industry trends to deliver optimal solutions."
        ],
        'Database Developer': [
            "As a Database Developer, your role is to design, implement, and maintain database systems that store and manage data effectively. Strong knowledge of database management systems (DBMS), SQL, and data modeling is crucial. Ensure that databases are optimized for performance and security. Regularly update your skills and stay informed about new technologies and best practices to keep your databases efficient and reliable.",
            "To succeed as a Database Developer, focus on mastering database design and management. You'll need strong SQL skills and an understanding of various DBMS technologies. Your role involves creating efficient and secure databases, writing complex queries, and ensuring data integrity. Keeping up with advancements in database technologies and best practices will help you enhance database performance and meet organizational needs effectively.",
            "In the role of a Database Developer, your responsibilities include designing and managing databases that meet business requirements. Expertise in SQL, data modeling, and database optimization is essential. Regularly update your skills and stay abreast of new developments in database technologies. Ensure that your databases are secure, reliable, and performant by implementing best practices and staying informed about industry trends.",
            "As a Database Developer, you'll be tasked with creating and maintaining databases that support business operations. Strong skills in SQL, data design, and database optimization are critical. Your role includes ensuring data accuracy, security, and efficient performance. Stay updated with the latest database technologies and best practices to provide robust and effective database solutions for your organization.",
            "To thrive as a Database Developer, focus on developing a deep understanding of database systems and SQL. Your role involves designing databases, writing queries, and optimizing performance. Ensure data security and integrity while implementing efficient solutions. Continuously improve your skills and knowledge to keep up with advancements in database technology and best practices, thereby providing effective database solutions."
        ],
        'Mobile Applications Developer': [
            "As a Mobile Applications Developer, your role is to create and maintain mobile apps for various platforms, such as iOS and Android. Strong skills in programming languages like Swift and Kotlin, as well as familiarity with mobile development frameworks, are essential. Focus on creating user-friendly, efficient, and high-performance apps. Stay updated with the latest trends in mobile technology and best practices to ensure your apps meet user expectations and perform well.",
            "To succeed as a Mobile Applications Developer, you should be proficient in developing apps for mobile platforms and familiar with various development tools and languages. Understanding user needs and creating intuitive, high-quality mobile experiences is key. Regularly update your skills with new mobile technologies and best practices to keep your apps competitive and ensure they function smoothly across different devices and operating systems.",
            "In the role of a Mobile Applications Developer, you will design and develop mobile applications for iOS and Android platforms. Mastery of mobile programming languages and development environments is crucial. Focus on optimizing app performance and ensuring a seamless user experience. Stay informed about the latest trends and advancements in mobile technology to keep your apps current and effective in meeting user needs.",
            "As a Mobile Applications Developer, your responsibilities include creating apps that run smoothly on mobile devices. Proficiency in programming languages and frameworks specific to mobile development is essential. Keep up with the latest trends in mobile technology to build innovative and user-friendly apps. Pay attention to app performance, security, and user experience to ensure your applications are both functional and engaging.",
            "To excel as a Mobile Applications Developer, focus on mastering the tools and languages used in mobile app development. Your role involves designing and implementing apps for various mobile platforms. Emphasize creating high-quality, efficient apps with a great user experience. Stay updated with the latest mobile development trends and best practices to ensure your apps remain relevant and perform optimally."
        ],
        'Network Security Engineer': [
            "As a Network Security Engineer, your primary role is to protect an organization's network from security breaches and cyber threats. Expertise in network security protocols, firewall management, and intrusion detection systems is essential. Regularly update your knowledge of emerging threats and security technologies to safeguard the network effectively. Strong analytical skills and attention to detail are crucial for identifying and addressing potential security vulnerabilities.",
            "To succeed as a Network Security Engineer, you need to have a deep understanding of network security principles and technologies. Your role involves implementing and managing security measures to protect against unauthorized access and cyber threats. Stay informed about the latest security developments and best practices. Effective problem-solving skills and the ability to analyze and respond to security incidents are key to maintaining a secure network environment.",
            "In the role of a Network Security Engineer, you'll be responsible for designing and implementing security measures to protect the network infrastructure. Proficiency in security tools, firewall configurations, and network monitoring is crucial. Keep your skills updated with the latest security trends and technologies. Focus on identifying and mitigating potential threats to ensure the integrity and confidentiality of the network.",
            "As a Network Security Engineer, your job is to ensure the security and integrity of the organization's network systems. Strong knowledge of network security tools, threat analysis, and incident response is essential. Continuously update your skills to keep pace with evolving security threats and technologies. Your role involves proactively identifying vulnerabilities and implementing measures to prevent security breaches.",
            "To thrive as a Network Security Engineer, focus on mastering network security technologies and best practices. Your responsibilities include protecting network infrastructure from cyber threats and ensuring data confidentiality and integrity. Stay updated with the latest advancements in security tools and threat landscapes. Strong analytical skills and the ability to respond effectively to security incidents are critical for maintaining a secure network environment."
        ],
        'Software Developer': [
            "As a Software Developer, you are responsible for designing, coding, and testing software applications. Proficiency in programming languages and development frameworks is crucial. Focus on creating efficient, scalable, and user-friendly software solutions. Stay updated with industry trends and best practices to ensure that your software meets current standards and effectively addresses user needs. Collaboration with other developers and stakeholders is also important for successful project outcomes.",
            "To excel as a Software Developer, you should have strong coding skills and a solid understanding of software development methodologies. Your role involves developing and maintaining software applications, debugging code, and ensuring software performance. Keeping up with new technologies and development tools will help you create innovative and effective software solutions. Effective communication and teamwork are key to delivering successful software projects.",
            "In the role of a Software Developer, you'll be tasked with writing code, designing software solutions, and performing testing and debugging. Expertise in programming languages and software development tools is essential. Focus on creating robust and user-friendly applications while adhering to best practices in software development. Regularly update your skills and stay informed about industry advancements to enhance your development capabilities.",
            "As a Software Developer, your primary responsibility is to build and maintain software applications that meet user requirements. Strong skills in programming, problem-solving, and software design are crucial. Keep your skills current by learning new technologies and development techniques. Effective communication with team members and stakeholders will help you deliver high-quality software solutions that meet project goals.",
            "To thrive as a Software Developer, focus on mastering programming languages and software development practices. Your role involves creating and optimizing software applications to address user needs effectively. Regularly update your knowledge of new technologies and industry trends. Strong problem-solving skills and the ability to work collaboratively with other developers are key to achieving successful software development outcomes."
        ],
        'Software Engineer': [
            "As a Software Engineer, you are involved in designing, developing, and maintaining software systems and applications. Strong knowledge of software engineering principles, programming languages, and development methodologies is essential. Focus on creating scalable, reliable, and efficient software solutions. Stay updated with industry trends and continuously improve your skills to tackle complex engineering challenges and deliver high-quality software products.",
            "To succeed as a Software Engineer, you should have expertise in software design, development, and testing. Your role involves applying engineering principles to create and maintain software systems. Keep up with the latest advancements in software technologies and methodologies. Effective problem-solving and analytical skills are crucial for developing robust software solutions and addressing technical challenges.",
            "In the role of a Software Engineer, you'll be responsible for designing and implementing software systems that meet user requirements. Mastery of software engineering principles and programming languages is key. Focus on optimizing software performance and ensuring reliability. Regularly update your skills and knowledge of new technologies to stay competitive and effectively address complex engineering problems.",
            "As a Software Engineer, your job is to develop and maintain software systems using engineering principles and practices. Strong coding skills, knowledge of software development methodologies, and an understanding of system architecture are crucial. Stay informed about the latest software technologies and trends. Effective communication and teamwork are important for successfully executing software engineering projects and achieving project goals.",
            "To excel as a Software Engineer, focus on mastering software design and development techniques. Your role involves building and optimizing software systems to meet user needs and project specifications. Keep your skills updated with the latest industry developments and best practices. Strong problem-solving abilities and the capacity to work effectively in a team environment are essential for delivering high-quality software solutions."
        ],
        'Software Quality Assurance (QA) / Testing': [
            "As a Software Quality Assurance (QA) / Testing professional, your role is to ensure that software products meet quality standards and are free of defects. Proficiency in testing methodologies, tools, and techniques is essential. Focus on creating detailed test plans, executing test cases, and reporting issues. Stay updated with the latest testing trends and technologies to ensure thorough and effective quality assurance practices.",
            "To thrive as a Software Quality Assurance (QA) / Testing specialist, you should be adept at identifying and documenting software defects. Your responsibilities include creating test plans, performing various types of testing, and ensuring that the software meets user requirements and quality standards. Regularly update your skills with new testing tools and techniques to enhance your ability to detect and address potential issues.",
            "In the role of a Software Quality Assurance (QA) / Testing professional, you'll be responsible for ensuring the quality and reliability of software products. Expertise in testing methodologies, tools, and attention to detail are crucial. Focus on developing comprehensive test plans, executing tests, and collaborating with developers to resolve issues. Stay informed about the latest advancements in testing technologies and practices to improve your effectiveness.",
            "As a Software Quality Assurance (QA) / Testing expert, your job is to validate software products to ensure they meet quality and performance standards. Strong skills in test planning, execution, and defect management are essential. Keep your skills current with the latest testing tools and methodologies. Effective communication with developers and stakeholders will help in addressing issues and delivering high-quality software.",
            "To excel as a Software Quality Assurance (QA) / Testing professional, focus on mastering testing techniques and tools. Your role involves creating and executing test cases, identifying defects, and ensuring that software meets quality standards. Stay updated with the latest trends in software testing to enhance your effectiveness. Strong attention to detail and the ability to work collaboratively with development teams are key to successful quality assurance."
        ],
        'Systems Security Administrator': [
            "As a Systems Security Administrator, your role involves managing and securing an organization's IT systems and networks. Strong knowledge of security protocols, firewall management, and intrusion detection systems is essential. Focus on implementing and monitoring security measures to protect against cyber threats. Regularly update your skills and stay informed about the latest security technologies and best practices to ensure the integrity and confidentiality of the systems.",
            "To succeed as a Systems Security Administrator, you need a deep understanding of IT security principles and technologies. Your responsibilities include configuring and managing security systems, responding to security incidents, and ensuring compliance with security policies. Keeping up with new security threats and advancements in technology will help you maintain a secure IT environment and protect against potential breaches.",
            "In the role of a Systems Security Administrator, you'll be responsible for safeguarding an organization's IT infrastructure from security threats. Expertise in security tools, protocols, and incident response is crucial. Focus on implementing robust security measures, monitoring system activity, and staying updated with the latest security trends and technologies. Effective problem-solving skills and attention to detail are key to managing and mitigating security risks.",
            "As a Systems Security Administrator, your job is to ensure the security and integrity of IT systems and networks. Strong skills in security administration, threat analysis, and incident management are essential. Regularly update your knowledge of security technologies and best practices. Proactively identify and address potential vulnerabilities to protect the organization's IT assets from cyber threats.",
            "To thrive as a Systems Security Administrator, focus on mastering IT security management and protocols. Your role involves implementing and overseeing security measures to protect against cyber threats and data breaches. Stay informed about the latest security technologies and trends to enhance your effectiveness. Strong analytical skills and the ability to respond effectively to security incidents are critical for maintaining a secure IT environment."
        ],
        'Technical Support': [
            "As a Technical Support specialist, your role involves assisting users with technical issues and ensuring that they have a smooth experience with software and hardware products. Strong problem-solving skills, communication abilities, and knowledge of technical systems are essential. Focus on providing clear and effective solutions, troubleshooting problems efficiently, and staying informed about the latest technologies to offer timely and relevant support.",
            "To excel in Technical Support, you should be skilled in diagnosing and resolving technical issues related to software, hardware, and network systems. Your role includes providing timely assistance to users, troubleshooting problems, and explaining solutions clearly. Regularly update your knowledge of new technologies and support tools to enhance your ability to address various technical challenges effectively.",
            "In the role of Technical Support, you'll be responsible for helping users with technical difficulties and ensuring that their issues are resolved promptly. Strong technical knowledge, problem-solving skills, and effective communication are crucial. Focus on understanding user needs, providing accurate solutions, and keeping up with advancements in technology to improve your support capabilities.",
            "As a Technical Support specialist, your job is to assist users with technical problems and provide solutions to ensure their satisfaction. Proficiency in troubleshooting, technical knowledge, and customer service skills are essential. Stay updated with the latest technological advancements and support practices to offer effective assistance and improve user experiences.",
            "To thrive in Technical Support, focus on mastering troubleshooting techniques and technical knowledge. Your role involves addressing user issues, providing solutions, and ensuring high levels of customer satisfaction. Regularly update your skills with new technologies and support tools to enhance your ability to resolve technical problems efficiently and effectively."
        ],
        'UX Designer': [
            "As a UX Designer, your role involves creating user-centered designs that enhance the overall experience of software and applications. Strong skills in user research, wireframing, and prototyping are essential. Focus on understanding user needs and behaviors to design intuitive and engaging interfaces. Stay updated with the latest UX trends and best practices to create effective and aesthetically pleasing user experiences.",
            "To succeed as a UX Designer, you should be skilled in designing user-friendly interfaces and conducting user research. Your responsibilities include creating wireframes, prototypes, and conducting usability testing to ensure a seamless user experience. Keep up with the latest trends in UX design and continually improve your skills to deliver effective and engaging designs that meet user needs.",
            "In the role of a UX Designer, you'll be responsible for designing intuitive and user-friendly interfaces for software and applications. Expertise in user research, interaction design, and usability testing is crucial. Focus on creating designs that address user needs and enhance their overall experience. Stay informed about the latest UX design trends and techniques to keep your designs relevant and effective.",
            "As a UX Designer, your job is to create designs that provide a positive and engaging user experience. Strong skills in user research, wireframing, and prototyping are essential. Regularly update your knowledge of UX design principles and trends to ensure that your designs are both functional and aesthetically pleasing. Effective communication with stakeholders and users is also important for delivering successful design solutions.",
            "To excel as a UX Designer, focus on mastering user-centered design principles and techniques. Your role involves creating interfaces that are easy to use and visually appealing. Conduct user research, develop wireframes and prototypes, and test designs to ensure they meet user needs. Stay updated with the latest UX trends and best practices to create impactful and user-friendly designs."
        ],
        'Web Developer': [
            "As a Web Developer, your role involves designing, building, and maintaining websites and web applications. Strong skills in HTML, CSS, JavaScript, and web development frameworks are essential. Focus on creating responsive and user-friendly websites that meet client requirements. Stay updated with the latest web development trends and technologies to ensure your websites are modern and effective.",
            "To thrive as a Web Developer, you should be proficient in web technologies and programming languages such as HTML, CSS, and JavaScript. Your responsibilities include developing and maintaining websites, ensuring cross-browser compatibility, and optimizing site performance. Keep up with the latest web development trends and tools to enhance your skills and deliver high-quality web solutions.",
            "In the role of a Web Developer, you'll be responsible for building and maintaining websites and web applications. Expertise in front-end and back-end technologies is crucial. Focus on creating efficient, responsive, and visually appealing websites that provide a seamless user experience. Stay informed about the latest developments in web technologies to keep your skills current and deliver effective web solutions.",
            "As a Web Developer, your job is to design and implement websites and web applications that meet user needs and client specifications. Strong skills in web development languages and frameworks are essential. Regularly update your knowledge of new web technologies and best practices to ensure that your web solutions are innovative and effective. Effective problem-solving and attention to detail are key to successful web development.",
            "To excel as a Web Developer, focus on mastering web development technologies and practices. Your role involves creating and optimizing websites and web applications to enhance user experience and meet project goals. Stay current with the latest trends and advancements in web development to improve your skills and deliver high-quality web solutions that meet modern standards."
        ]
    }
    if job_role in guidance_messages:
        return random.choice(guidance_messages[job_role])
    return "No guidance available for this job role."


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
