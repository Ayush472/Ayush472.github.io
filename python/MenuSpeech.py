import speech_recognition as sr
r=sr.Recognizer()

print("Order Please")
text = ""
print("Menu: Pasta /Momos / Coffee / Rice / Roll")

while text!="ok":
    print("What u want to eat ??")
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=4)
        print("Wait...")
        text = r.recognize_google(audio_data)
        print(text)
        if text == "pasta":
            a = int(input("Enter Qnty. =>"))
            print("Total =>", a * 300, "Rs.")
        elif text == "momos":
            b = int(input("Enter Qnty. =>"))
            print("Total =>", b * 150, "Rs.")
        elif text == "coffee":
            c = int(input("Enter Qnty. =>"))
            print("Total =>", c * 250, "Rs.")
        elif text == "rice":
            d = int(input("Enter Qnty. =>"))
            print("Total =>", d * 250, "Rs.")
        elif text == "roll":
            e = int(input("Enter Qnty. =>"))
            print("Total =>", e * 300, "Rs.")
        elif text == "done":
            print("---Your Bill ---")
            print("Bill =>", a*300 + b*150 + c*250 + d*250 + e*300, "Rs.")
            print("\n---Thank You---")
        else:
            print("order something else!!")