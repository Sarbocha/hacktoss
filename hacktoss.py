import speech_recognition as sr
listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if "heads" in command:
            print("You get heads")
        elif "tails" in command:
            print("You get tails")
        else:
            print("Voice not recognized")


except:
    pass
