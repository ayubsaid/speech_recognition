import speech_recognition as sr
from gtts import gTTS

recognizer = sr.Recognizer()

languages = ["en-US", "ru-RU", "uz-UZ"]  # List of language codes to recognize

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic)
            audio = recognizer.listen(mic)

            for lang in languages:
                text = recognizer.recognize_google(audio, language=lang)
                text = text.lower()
                print(f'Recognized ({lang}): {text}')

                # Generate speech from the recognized text
                language = lang.split("-")[0]  # Extract the language code
                speech = gTTS(text=text, lang=language, slow=False, tld="com.au")
                speech.save("textTOspeech.mp3")

                print("Speech generated and saved as textTOspeech.mp3")

    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        continue
