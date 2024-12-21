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

# Audio stream setup with automatic resampling
pa = pyaudio.PyAudio()
print("Sampling rate:",porcupine.sample_rate)
audio_stream = pa.open(
    rate=41000,  # Set the actual sampling rate of the microphone
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=int(41000 * (1/porcupine.sample_rate)),  # Calculate frames per buffer based on the desired sampling rate
    input_device_index=1,
    input_host_api_specific_stream_info={
        pyaudio.paPlugIn,
        pyaudio.paHostApiTypeId,
        'plughw:2,0',  # Use pluggable hardware device for automatic resampling
        audio_stream.get_device_info_by_index(1).maxInputChannels,
        audio_stream.get_device_info_by_index(1).maxOutputChannels,
        41000,  # Actual sampling rate of the microphone
        None,
        0,
        pyaudio.paStream,
        True,
        None
    }
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
