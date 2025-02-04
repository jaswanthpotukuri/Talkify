import speech_recognition as sr 
import pyttsx3
import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        command = ""
        try:
            command = recognizer.recognize_google(audio)
            print("You said: " + command)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Google speech recongition request failed: {0}".format(e))   
        return command.lower() 
    
def greet():
    current_time = datetime.datetime.now() 
    hour = current_time.hour   
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon") 
    else:
        speak("Good Evening")
        
        
def ai_assistant():
    greet()
    speak("I am your AI assistant. How can I help you today ?")
    
    while True:
        command = get_audio()
        
        if "stop" in command:
            speak("Goodbye")
            break
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"The current date is {current_date}")
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")
        else:
            speak("I don't understand that command. Please try again")   
                    
if __name__ == "__main__":
    ai_assistant()            

                  
            
            
                