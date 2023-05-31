import speech_recognition as sr

recognizer = sr.Recognizer()

languages = ["en-US", "fr-FR", "es-ES", "ru-RU", "en-GB"]  # List of language codes to recognize

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            for lang in languages:
                text = recognizer.recognize_google(audio, language=lang)
                text = text.lower()
                print(f'Recognized ({lang}): {text}')

    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        continue
