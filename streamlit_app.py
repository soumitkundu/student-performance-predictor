# -*- coding: utf-8 -*-
"""
@file: streamlit_app.py
@author: Soumit Kundu <soumitkundu@gmail.com>
@date: 2025-08-04
@version: 1.0.0
@description: This application uses a pre-trained Machine Learning model to predict student scores based on hours of study.
"""

# Import necessary libraries
import pickle
import numpy as np
import os

# Import the Streamlit library
import streamlit as st

# get the current working directory
cwd = os.getcwd()

# Define the path to the model file
model_file_path = os.path.join(cwd, 'models', 'student_performance_model_lr.pkl')
# Check if the model file exists
if not os.path.exists(model_file_path):
    st.error("Model file not found. Please ensure the model is available in the 'models' directory.")
else:
    # Load the pre-trained model
    student_performance_model_lr = pickle.load(open(model_file_path, 'rb'))

def predict_score(study_hours):
    """Predict the student score based on study hours.
    Args:
        study_hours (str): The number of hours the student has studied.
    Returns:
        str: The predicted score.
    """
    try:
        # Convert the input to integer
        study_hours = int(study_hours)
        # Ensure the input is a valid number
        if study_hours < 0:
            raise ValueError("Study hours cannot be negative.")
        # Prepare the input for prediction
        input_data = np.array([[study_hours]])
        # Make the prediction using the loaded model
        prediction = student_performance_model_lr.predict(input_data)
        # Return the predicted score
        return prediction[0]
    except ValueError as e:
        return f"Invalid input: {e}"
    
# Define the main function to run the Streamlit app
def main():
    st.title("Student Performance Prediction App")
    st.subheader("Predicting Student Scores Based on Study Hours")
    st.text("This application uses a pre-trained Machine Learning model to predict student scores based on hours of study.")

    study_hours = st.text_input("Study Hours","Hours of study to predict student score")
    result=""
    if st.button("Predict"):
        result = predict_score(study_hours)
        try:
            predicted_score = float(result)
            st.success(f"The predicted score for studying {study_hours} hours is: {predicted_score:.2f}")
        except ValueError:
            st.error(result)
    else:
        st.warning("Please enter the number of study hours to get a prediction.")
if __name__=='__main__':
    main()

