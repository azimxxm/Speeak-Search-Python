import speech_recognition as sr
import webbrowser
sr.Microphone(device_index=1)
r = sr.Recognizer()
r.energy_threshold = 5000
with sr.Microphone() as source:
    print("Speeak !")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: ".format(text))
        url = 'http://127.0.0.1:8000/search?search='
        search_url = url+text
        webbrowser.open(search_url)
    except:
        print("Can't recognise")
