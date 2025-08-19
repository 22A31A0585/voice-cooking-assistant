import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# Recipe steps with optional images
recipe_steps = [
    {"text": "Welcome! Today we are making Masala Maggi.", "img": None},
    {"text": "Step 1: Boil one and a half cups of water.", "img": None},
    {"text": "Step 2: Add the Maggi noodles to the water.", "img": None},
    {"text": "Step 3: Add tastemaker and stir.", "img": None},
    {"text": "Step 4: Let it cook for 2 to 3 minutes.", "img": None},
    {"text": "Step 5: Serve hot and enjoy!", "img": None},
]

if "current_step" not in st.session_state:
    st.session_state.current_step = 0

def show_step():
    step = recipe_steps[st.session_state.current_step]
    st.markdown(f"<h3 style='color:#FF5733'>{step['text']}</h3>", unsafe_allow_html=True)
    if step['img']:
        st.image(step['img'], use_column_width=True)
    # JS TTS
    js_code = f"""
    <script>
    var msg = new SpeechSynthesisUtterance("{step['text']}");
    window.speechSynthesis.speak(msg);
    </script>
    """
    components.html(js_code, height=0)

def start_recipe():
    st.session_state.current_step = 0
    show_step()

def next_step():
    if st.session_state.current_step < len(recipe_steps) - 1:
        st.session_state.current_step += 1
        show_step()
    else:
        st.success("🎉 That was the last step. You're done!")

def repeat_step():
    show_step()

def stop_recipe():
    st.info("Goodbye! Happy Cooking!")

st.title("🍜 Masala Maggi Voice Assistant")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Start"): start_recipe()
with col2:
    if st.button("Next"): next_step()
with col3:
    if st.button("Repeat"): repeat_step()
with col4:
    if st.button("Stop"): stop_recipe()
