# .\porcupine_env\Scripts\activate
# Console for API key and model: https://console.picovoice.ai

import pvporcupine
import pyaudio
import struct
import intent
import stt

# Replace with your access key
access_key = r"GJtuxYjiBSMWPSVqtNKwnozW9dWkkps6VTmgROSlRbdljHsMbwlD/w=="

# Path to the wake word .ppn file
keyword_path = r"./Wake word detection/Hey-Sprout_en_raspberry-pi_v3_0_0.ppn"

# Initialize Porcupine
porcupine = pvporcupine.create(access_key=access_key, keyword_paths=[keyword_path]) # [keyword_path]

# Audio stream setup
pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length,
    input_device_index=1
)

print("Listening for wake word...")

try:
    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        result = porcupine.process(pcm)
        if result >= 0:
            print("Wake word detected!")
            intent.getIntent()
except KeyboardInterrupt:
    print("Stopping...")
finally:
    audio_stream.close()
    porcupine.delete()
    pa.terminate()
