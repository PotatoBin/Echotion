import pyaudio
import wave
import sys

def stream_audio(output_file_path, record_seconds=5):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1 if sys.platform == 'darwin' else 2
    RATE = 22050 // 4

    with wave.open(output_file_path, 'wb') as wf:
        p = pyaudio.PyAudio()
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

        print('Recording...')
        for _ in range(0, RATE // CHUNK * record_seconds):
            wf.writeframes(stream.read(CHUNK))
        print('Done')

        stream.close()
        p.terminate()