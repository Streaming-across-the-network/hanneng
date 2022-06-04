import ffmpeg 
import sys

sys.path.append(r'C:\Users\Hanneng\Videos\VR\implement\ffmpeg-5.0.1-full_build\bin')

stream = ffmpeg.input(r"C:\Users\Hanneng\Videos\VR\video\landscape.mp4")

stream = stream.trim(start = 50, duration = 15)
stream = stream.filter('fps', fps= 40, round= 'up' ).filter('scale', w= 1920, h= 1080)

stream = ffmpeg.output(stream, r'C:\Users\Hanneng\Videos\VR\video\try.mp4')

ffmpeg.run(stream)