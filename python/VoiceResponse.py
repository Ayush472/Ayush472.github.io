import speech_recognition as sr
from playsound import playsound

r=sr.Recognizer()
text=""
while text!="no":
    print("Please talk and Say No for Stop")
    with sr.Microphone() as source:
        audio_data=r.record(source,duration=4)
        text = r.recognize_google(audio_data)
        print(text)
        if text == "hello":
            playsound('hello.mp3')
        elif text == "play some songs":
            playsound('Pushpa.mp3')
        elif text == "hungry":
            print("Let's eat something")
        elif text=="no":
            print("Bye")