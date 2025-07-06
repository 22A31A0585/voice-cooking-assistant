import speech_recognition as sr
import pyttsx3

# Initialize engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Recipe data
recipes = {
    "maggi": {
        "ingredients": ["1.5 cups water", "1 packet noodles", "Tastemaker"],
        "steps": [
            "Boil water.",
            "Add Maggi noodles.",
            "Add tastemaker and stir.",
            "Cook for 2 to 3 minutes.",
            "Serve hot and enjoy!"
        ]
    },
    "pasta": {
        "ingredients": ["1 cup pasta", "2 cups water", "Salt", "Oil"],
        "steps": [
            "Boil pasta with water and salt.",
            "Cook until soft.",
            "Drain and add oil.",
            "Mix with sauce if needed.",
            "Serve warm."
        ]
    },
    "biryani": {
        "ingredients": ["Basmati rice", "Veg/Chicken", "Biryani masala", "Curd", "Onion", "Oil"],
        "steps": [
            "Soak rice.",
            "Cook veg or chicken with masala.",
            "Layer rice and gravy.",
            "Dum cook for 15 minutes.",
            "Garnish and serve."
        ]
    },
    "upma": {
        "ingredients": ["Rava", "Mustard", "Curry leaves", "Water", "Salt"],
        "steps": [
            "Roast rava.",
            "Heat oil, add mustard and curry leaves.",
            "Add water and salt.",
            "Add rava and stir continuously.",
            "Cook until thick."
        ]
    },
    "tea": {
        "ingredients": ["Water", "Tea powder", "Sugar", "Milk"],
        "steps": [
            "Boil water with tea powder.",
            "Add sugar.",
            "Add milk.",
            "Boil for 2 minutes.",
            "Strain and serve."
        ]
    },
    "fried rice": {
        "ingredients": ["Cooked rice", "Veggies", "Soy sauce", "Oil"],
        "steps": [
            "Heat oil in pan.",
            "Add chopped vegetables.",
            "Add rice and soy sauce.",
            "Mix well and stir-fry.",
            "Serve hot."
        ]
    },
    "pulao": {
        "ingredients": ["Rice", "Vegetables", "Spices", "Oil"],
        "steps": [
            "Heat oil and add spices.",
            "Add vegetables.",
            "Add rice and water.",
            "Cook until rice is done.",
            "Serve with raita."
        ]
    },
    "oats smoothie": {
        "ingredients": ["Oats", "Milk", "Banana", "Honey"],
        "steps": [
            "Soak oats in milk.",
            "Add banana and honey.",
            "Blend well.",
            "Serve chilled."
        ]
    },
    "lemon rice": {
        "ingredients": ["Cooked rice", "Lemon", "Mustard", "Chilies", "Oil"],
        "steps": [
            "Heat oil, add mustard and chilies.",
            "Add cooked rice.",
            "Add lemon juice.",
            "Mix and serve."
        ]
    },
    "chicken curry": {
        "ingredients": ["Chicken", "Onion", "Tomato", "Spices", "Oil"],
        "steps": [
            "Marinate chicken.",
            "Fry onions and tomatoes.",
            "Add chicken and spices.",
            "Cook until done.",
            "Garnish and serve."
        ]
    },
    "chapati": {
        "ingredients": ["Wheat flour", "Water", "Salt"],
        "steps": [
            "Mix flour, salt, and water.",
            "Make dough and roll.",
            "Cook on hot tawa.",
            "Flip and cook both sides.",
            "Serve hot."
        ]
    },
    "dosa": {
        "ingredients": ["Dosa batter", "Oil"],
        "steps": [
            "Heat tawa.",
            "Spread dosa batter.",
            "Drizzle oil.",
            "Flip and cook.",
            "Serve with chutney."
        ]
    },
    "idly": {
        "ingredients": ["Idly batter", "Oil for greasing"],
        "steps": [
            "Grease idly moulds.",
            "Pour batter.",
            "Steam for 10-12 mins.",
            "Cool and unmould.",
            "Serve with chutney."
        ]
    },
    "omelet": {
        "ingredients": ["Eggs", "Salt", "Pepper", "Onion", "Oil"],
        "steps": [
            "Beat eggs with salt and pepper.",
            "Add chopped onion.",
            "Pour in hot pan.",
            "Flip when cooked one side.",
            "Serve hot."
        ]
    }
}

# State
current_recipe = None
current_step = 0

# Voice
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Listen
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except:
            return ""

# Handle Commands
def handle_command(cmd):
    global current_recipe, current_step

    if "show recipes" in cmd:
        speak("We have the following recipes:")
        for name in recipes.keys():
            speak(name)

    elif cmd.startswith("start "):
        recipe_name = cmd.replace("start ", "").strip()
        if recipe_name in recipes:
            current_recipe = recipe_name
            current_step = 0
            speak(f"Starting {recipe_name}. Say 'ingredients' to hear them.")
        else:
            speak("Sorry, that recipe is not available.")

    elif "ingredients" in cmd:
        if current_recipe:
            ing = recipes[current_recipe]["ingredients"]
            speak(f"Ingredients for {current_recipe}:")
            for item in ing:
                speak(item)
        else:
            speak("Please say 'start' followed by a recipe name first.")

    elif "next" in cmd:
        if current_recipe:
            steps = recipes[current_recipe]["steps"]
            if current_step < len(steps):
                speak(steps[current_step])
                current_step += 1
            else:
                speak("That was the last step. You are done!")
        else:
            speak("Please start a recipe first.")

    elif "repeat" in cmd:
        if current_recipe and current_step > 0:
            speak(recipes[current_recipe]["steps"][current_step - 1])
        else:
            speak("No step to repeat yet.")

    else:
        speak("Sorry, I didn't understand. Try 'show recipes', 'start maggi', 'ingredients', 'next', or 'repeat'.")

# Run
speak("Say 'show recipes' to hear available dishes.")
while True:
    command = listen()
    if "stop" in command or "exit" in command:
        speak("Goodbye! Happy Cooking!")
        break
    handle_command(command)
