import pyaudio
import wave
import os
import time
import threading
import tkinter as tk
import random

def record(self):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100,
                        input=True, frames_per_buffer=1024)
    frames = []
    start = time.time()

    while self.recording:
        data = stream.read(1024)
        frames.append(data)
        passed = time.time() - start

        secs = passed % 60
        mins = passed // 60
        hours = mins // 60
        self.label.config(text=f'{int(hours):02d}:{int(mins):02d}:{int(secs):02d}')

    stream.stop_stream()
    stream.close()
    audio.terminate()

    exists = True
    i = 1
    while exists:
        if os.path.exists(f'recording{i}.wav'):
            i += 1
        else:
            exists = False

    # Save the recording without noise reduction
    sound_file = wave.open(f'recording{i}.wav', 'wb')
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()


