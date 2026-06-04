import json
import queue
import sounddevice as sd

from vosk import Model
from vosk import KaldiRecognizer

MODEL_PATH = "models/vosk-model-small-en-us-0.15"

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

model = Model(MODEL_PATH)

recognizer = KaldiRecognizer(model, 16000)

def listen():

    print("Listening...")

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype='int16',
        channels=1,
        callback=callback
    ):

        while True:

            data = q.get()

            if recognizer.AcceptWaveform(data):

                result = json.loads(
                    recognizer.Result()
                )

                text = result.get("text", "")

                if text:
                    print("You:", text)
                    return text