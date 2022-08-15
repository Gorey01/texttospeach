import pyttsx3
samir=pyttsx3.init()

voices=samir.getProperty('voices')
samir.setProperty('voice',voices[1].id)
samir.say(input(" "))
samir.runAndWait()
samir.stop()