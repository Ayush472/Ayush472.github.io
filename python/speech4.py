import speech_recognition as sr
r=sr.Recognizer()
text=""

while text!="no":
    print("Please talk and Say No for Stop")
    with sr.Microphone() as source:
        try:
            audio_data=r.record(source,duration=5)
            print("Getting")
            text=r.recognize_google(audio_data)
            if text == "no":
                print("bye")
            else:
                if text.isnumeric():
                    a = int(text)
                    if a % 2 == 0:
                        print(a, "is even")
                    else:
                        print(a, "is odd")
                else:
                    print("Sorry wrong input")
        except:
            print("Error in input")