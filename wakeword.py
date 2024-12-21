import sounddevice as sd
import pvporcupine
import pyaudio
import struct
import numpy as np
import scipy.signal

# Replace with your access key
access_key = r"GJtuxYjiBSMWPSVqtNKwnozW9dWkkps6VTmgROSlRbdljHsMbwlD/w=="

# Path to the wake word .ppn file
keyword_path = r"./Wake word detection/Hey-Sprout_en_raspberry-pi_v3_0_0.ppn"

# Initialize Porcupine
porcupine = pvporcupine.create(access_key=access_key, keyword_paths=[keyword_path])

# Audio stream setup with the device's native sample rate
pa = pyaudio.PyAudio()
native_sample_rate = 44100  # Your device's native sample rate

try:
    audio_stream = pa.open(
        rate=native_sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        input_device_index=1,  # Verify this index
    )

    print("Listening for wake word...")

    while True:
        # Read audio data at the native sample rate
        pcm = audio_stream.read(int(porcupine.frame_length * (native_sample_rate / porcupine.sample_rate)),
                                exception_on_overflow=False)
        pcm = struct.unpack_from("h" * int(porcupine.frame_length * (native_sample_rate / porcupine.sample_rate)), pcm)

        # Resample the audio data to match Porcupine's required sample rate
        pcm_resampled = scipy.signal.resample(pcm, porcupine.frame_length)

        # Convert the resampled audio data to the correct format
        pcm_resampled = np.int16(pcm_resampled).tolist()

        result = porcupine.process(pcm_resampled)
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
