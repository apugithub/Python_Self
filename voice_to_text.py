import speech_recognition as sr
#import pyttsx3
r = sr.Recognizer()
with sr.Microphone() as mic:
    r.adjust_for_ambient_noise(mic, duration=0.3)
    myAud = r.listen(mic)
    FinalText = r.recognize_google(myAud)

print(FinalText)


# After running the code say something