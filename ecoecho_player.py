import subprocess

# Set up FFmpeg
ffmpeg_cmd = [
    'ffmpeg',
    '-i', 'tcp://<primary_raspberry_pi_ip>:6969',
    '-f', 'alsa',
    'hw:0,0'
]

# Start FFmpeg
ffmpeg_process = subprocess.Popen(ffmpeg_cmd)

# Wait for the process to finish
ffmpeg_process.wait()
