# Career Path Prediction and Guidance System

This project is a **Career Path Prediction and Guidance System** built using a Streamlit web application. The system provides users with personalized career path predictions based on their skills, certifications, workshops attended, and career interests.

## Features

- **User-Friendly Interface:** Simple and intuitive interface for inputting personal ratings, scores, and career preferences.
- **Career Path Prediction:** Predicts the most suitable career path based on user inputs.
- **Guidance System:** Offers tailored guidance and recommendations to help users achieve their professional goals.

## Getting Started

### Prerequisites

- Python 3.8+
- Streamlit
- Numpy

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sSumankumari/Career-Path-Prediction-and-Guidance-System
    cd career-path-prediction
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    streamlit run app.py
    ```

## How It Works

1. **Enter Your Ratings and Scores:** Provide ratings for your coding skills, self-learning capability, reading and writing skills, and memory capability.
2. **Select Your Certifications:** Choose relevant certifications from the provided list.
3. **Select the Workshops Attended:** Pick the workshops you have attended.
4. **Choose Your Interested Subjects:** Select the subjects you are most passionate about.
5. **Select Your Preferred Career Area:** Indicate the career areas that align with your long-term goals.
6. **Choose the Preferred Type of Company:** Select the type of company you would like to work for.
7. **Predict Career Path:** Click the "Predict Career Path" button to get your prediction and guidance.

## Project Structure

- `app.py`: Main application file containing the Streamlit app.
- `helper.py`: Contains helper functions like `predict_career_path` and `provide_guidance`.
- `requirements.txt`: Lists all Python packages required to run the project.
