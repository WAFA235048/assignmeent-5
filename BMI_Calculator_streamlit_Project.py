import streamlit as st
import pandas as pd
st.title("Hey user! Let's calculate your BMI!")
Weight=st.slider('Enter your weight(in kg): ', min_value=1, max_value=300)
height=st.slider('Enter your height (in cm): ', min_value=1, max_value=500)
BMI=Weight/((height/100)**2)
BMI = round(float(BMI), 1)
st.write(f'#### Your BMI : {BMI:.1f} ####')
if(BMI>=18.5 and BMI<=24.9):
  st.write('You have a healthy weight. You better maintain your weight like this by doing a lil cardio every day.')
elif(BMI>=25.0 and BMI<=29.9):
  st.write('You are overweight. You better start controling your diet, NOW!')
elif(BMI>=30.0 and BMI<=34.9):
  st.write('You have class 1 Obesity. To avoid health issues you better start exercising, NOW!.')
elif(BMI>=35.0 and BMI<=39.9):
  st.write('You have class 2 Obesity. You better consult your doctor, NOW!.')
elif(BMI>=40.0):
  st.write('You have class 3 obesity. You better visit the hospital, NOW! otherwise, someone else will take you.')
else:
   st.write('You are underweight. You better eat something, NOW!')
st.write("### Following is detailed breakdown of BMI categories: ###")
st.write('- Underweight: BMI less than 18.5')
st.write('- Healthy Weight: BMI between 18.5 and 24.9')
st.write('- Overweight: BMI between 25 and 29.9')
st.write('- Obesity: BMI of 30 or greater.')
st.write('  -->Class 1 Obesity: BMI between 30 and 34.9.')
st.write('  -->Class 2 Obesity: BMI between 35 and 39.9. ')
st.write('  -->Class 3 Obesity (Severe Obesity): BMI of 40 or greater.')
   