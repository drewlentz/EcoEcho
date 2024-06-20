import pyaudio
import subprocess

# Set up PyAudio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

# Open the microphone stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Set up FFmpeg
ffmpeg_cmd = [
    'ffmpeg',
    '-f', 's16le',
    '-ar', '44.1k',
    '-ac', '1',
    '-i', '-',
    '-f', 'mp3',
    '-b:a', '128k',
    '-bufsize', '128k',
    'tcp://0.0.0.0:6969'
]

# Start FFmpeg
ffmpeg_process = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)

# Read audio from the microphone and write it to FFmpeg
while True:
    audio_data = stream.read(CHUNK)
    ffmpeg_process.stdin.write(audio_data)

# Clean up
stream.stop_stream()
stream.close()
p.terminate()
ffmpeg_process.terminate()
