import speech_recognition as sr
import pyttsx3

engine=pyttsx3.init()
engine.setProperty('rate',150)
recipe_steps=[
  "Welcome! Today we are making Masala Maggi.",
  "Step 1: Boil one and a half cups of water.",
  "Step 2 : Add the Maggi noodles to the water",
  "Step 3 : Add tastemaker and Stir.",
  "Step 4 : Let it cook for 2 to 3 minutes.",
  "Step 5 : Serve hot and enjoy!"
]
current_step=0
def speak(text):
  print("Assistant",text)
  engine.say(text)
  engine.runAndWait()
def listen():
  recognizer=sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    try:
      audio=recognizer.listen(source,timeout=5)
      command=recognizer.recognize_google(audio)
      print("you said",command)
      return command.lower()
    except:
      return ""
def handle_command(cmd):
  global current_step
  if "start" in cmd:
    current_step=0
    speak(recipe_steps[current_step])
  elif "next" in cmd:
    if current_step <len(recipe_steps)-1:
      current_step+=1
      speak(recipe_steps[current_step])
    else:
      speak("That was the last step.You're done!")
  elif "repeat" in cmd:
    speak(recipe_steps[current_step])
  else:
    speak("Sorry, I didn't understand.Say 'next','repeat',or'start'.")
  
speak("Say 'start' to begin cooking.")
while True:
  command =listen()
  if "exit" in command or "stop" in command:
    speak("Goodbye! Happy Cooking!")
    break
  handle_command(command)