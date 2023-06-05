from gtts import gTTS

language = 'en'
text = 'Hello, world I am a generator speech from the text, if you want to test it let me know!'

speech = gTTS(text=text, lang=language, slow=False, tld="com.au" )
speech.save("textTOspeech.mp3")
