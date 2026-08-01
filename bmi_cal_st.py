import google.genai as genai
import streamlit as st

GOOGLE_API_KEY = st.secrets["GOGGLE_API_KEY"] # Replace with your actual API key

client = genai.Client(api_key=GOOGLE_API_KEY) # Establishes the connection with Gemini AI

st.title("BMI Calculator with AI Nutritionist")

wt = st.number_input("Enter your weight in kilograms: ")
ht = st.number_input("Enter your height in meters: ")

bmi = wt / (ht ** 2)
st.write(f"Your BMI is: {bmi:.2f}")

prompt = prompt = f"""analyze the bmi and comment  for a person whose weight in kgs is {wt}
and height in meters is {ht}, and bmi is {bmi}."""


if st.button("Analyze your bmi with AI"):
   st.write("Analyzing your bmi with AI...")
response = client.models.generate_content(
    model = "gemini-3.6-flash",
    contents = prompt)
st.write(response.text)