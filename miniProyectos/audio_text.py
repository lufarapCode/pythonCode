import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile("prueba.wav") as source:
    audio_text = r.record(source)
    
    try:
        text = r.recognize_google(audio_text, language="en-US")
        print(f"Transcripción: {text}")
    except:
        print("No se pudo transcribir el audio.")
