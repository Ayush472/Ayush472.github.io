import speech_recognition as sr
r=sr.Recognizer()
text=""

while text!="no":
    print("Please talk and Say No for Stop")
    with sr.Microphone() as source:
        try:
            audio_data=r.record(source,duration=3)
            print("Getting")
            text=r.recognize_google(audio_data)
            print(text)
            if text == "no":
                print("bye")
            else:
                if text.isnumeric():
                    a = int(text)
                    for i in range(1, 11):
                        print(a, "X", i, "=", a * i)
                else:
                    print("Sorry wrong input")

        except:
            print("Error in input")