import sounddevice as sd
import pvporcupine
import pyaudio
import struct

# Replace with your access key
access_key = r"GJtuxYjiBSMWPSVqtNKwnozW9dWkkps6VTmgROSlRbdljHsMbwlD/w=="

# Path to the wake word .ppn file
keyword_path = r"./Wake word detection/Hey-Sprout_en_raspberry-pi_v3_0_0.ppn"

# Initialize Porcupine
porcupine = pvporcupine.create(access_key=access_key, keyword_paths=[keyword_path])

# Audio stream setup with automatic resampling
pa = pyaudio.PyAudio()
print("Sampling rate:", porcupine.sample_rate)

try:
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        input_device_index=1,  # Verify this index
    )

    print("Listening for wake word...")

    while True:
        pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        result = porcupine.process(pcm)
        if result >= 0:
            print("Wake word detected!")
            # Call your intent processing function here
            # intent.getIntent()

except KeyboardInterrupt:
    print("Stopping...")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if audio_stream:
        audio_stream.close()
    porcupine.delete()
    pa.terminate()
