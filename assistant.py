# app.py
import streamlit as st
import pyttsx3
from PIL import Image
import time

engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Recipe steps with optional image for each step
recipe_steps = [
    {"text": "Welcome! Today we are making Masala Maggi.", "img": "images/welcome.png"},
    {"text": "Step 1: Boil one and a half cups of water.", "img": "images/step1.png"},
    {"text": "Step 2: Add the Maggi noodles to the water.", "img": "images/step2.png"},
    {"text": "Step 3: Add tastemaker and stir.", "img": "images/step3.png"},
    {"text": "Step 4: Let it cook for 2 to 3 minutes.", "img": "images/step4.png"},
    {"text": "Step 5: Serve hot and enjoy!", "img": "images/step5.png"}
]

if "current_step" not in st.session_state:
    st.session_state.current_step = 0

def speak(text):
    engine.say(text)
    engine.runAndWait()

def show_step():
    step = recipe_steps[st.session_state.current_step]
    st.markdown(f"<h3 style='color:#FF5733'>{step['text']}</h3>", unsafe_allow_html=True)
    try:
        img = Image.open(step['img'])
        st.image(img, use_column_width=True)
    except:
        st.write("Image not found, continue with text.")

def start_recipe():
    st.session_state.current_step = 0
    show_step()
    speak(recipe_steps[0]["text"])

def next_step():
    if st.session_state.current_step < len(recipe_steps) - 1:
        st.session_state.current_step += 1
        show_step()
        speak(recipe_steps[st.session_state.current_step]["text"])
    else:
        st.success("🎉 That was the last step. You're done!")
        speak("That was the last step. You're done!")

def repeat_step():
    show_step()
    speak(recipe_steps[st.session_state.current_step]["text"])

def stop_recipe():
    st.info("Goodbye! Happy Cooking!")
    speak("Goodbye! Happy Cooking!")

# Streamlit UI
st.title("🍜 Masala Maggi Cooking Assistant")
st.markdown("<h5 style='color:blue'>Follow the recipe step by step!</h5>", unsafe_allow_html=True)

# Animated GIF for fun
st.image("images/cooking.gif", use_column_width=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Start"):
        start_recipe()
with col2:
    if st.button("Next"):
        next_step()
with col3:
    if st.button("Repeat"):
        repeat_step()
with col4:
    if st.button("Stop"):
        stop_recipe()

  handle_command(command)
